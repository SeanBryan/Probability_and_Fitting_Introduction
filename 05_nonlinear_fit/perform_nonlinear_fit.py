import numpy as np
import matplotlib.pyplot as pl
import pandas as pd

# read in data from file
df = pd.read_csv('../03_generating_mock_data/05_nonlinear_fit_data.csv')

# unpack these to individual variables
t = np.array(df['t'])
T = np.array(df['T'])

# use the curve_fit function in scipy to perform non-linear fitting
from scipy.optimize import curve_fit

# define function for the model in the form that curve_fit wants
def model_curvefit(t,Ti,T0,tau):
    # calculate model
    return (Ti - T0)*np.exp(-t/tau) + T0

# create rough initial guesses for the parameters
Ti_guess = T[0] # use the first data point as a guess for the start temperature
T0_guess = T[-1] # use the last data point as a guess for the end
tau_guess = np.max(t) - np.min(t) # use the total duration as a guess for the time constant

# use curvefit to fit the data
# assuming equal sigma=1 errorbars
popt,pcov = curve_fit(model_curvefit,t,T,sigma=np.ones_like(t),p0=(Ti_guess,T0_guess,tau_guess))

# unpack the best-fit parameters
Ti = popt[0]
T0 = popt[1]
tau = popt[2]

# calculate the best-fit model
T_predicted = model_curvefit(t,Ti,T0,tau)

# assume (this is a significant approximation!) that our model is conceptually correct
# in this case, the only difference between the model and data would be noise
# calculate the noise level by calculating the standard deviation between model and data
measured_noise = np.std(T_predicted - T)

# redo the fit assuming errorbars at this level
# note that this should not affect the best-fit parameter values
# but this will let us determine errors on these parametres
popt,pcov = curve_fit(model_curvefit,t,T,sigma=measured_noise*np.ones_like(t),p0=(Ti,T0,tau))

# find the errors on each parameter
error_on_Ti = np.sqrt(pcov[0,0])
error_on_T0 = np.sqrt(pcov[1,1])
error_on_tau = np.sqrt(pcov[2,2])

# plot everything
pl.ion()
f = pl.figure()
gs = f.add_gridspec(4,1)
ax1 = f.add_subplot(gs[0:3,:])
ax1.errorbar(t,T,yerr=measured_noise,fmt='*',label='Simulated Data')
ax1.plot(t,T_predicted,'-',label='Best-Fit Model\nTi = '+str(Ti)[0:5]+' +/- '+str(error_on_Ti)[0:4]+'\nT0 = '+str(T0)[0:4]+' +/- '+str(error_on_T0)[0:4]+'\ntau = '+str(tau)[0:5]+' +/- '+str(error_on_tau)[0:4])
ax1.plot(t,model_curvefit(t,Ti+error_on_Ti,T0,tau),':',label='Ti = Nominal + Error')
ax1.plot(t,model_curvefit(t,Ti,T0+error_on_T0,tau),':',label='T0 = Nominal + Error')
ax1.plot(t,model_curvefit(t,Ti,T0,tau+error_on_tau),':',label='tau = Nominal + Error')
ax1.legend()
ax1.grid('on')
#ax1.set_xlabel('Time [min]')
ax1.set_ylabel('Temperature [K]')
ax2 = f.add_subplot(gs[3,:])
ax2.plot(t,T_predicted - T,'*')
ax2.set_ylabel('Error [K]')
ax2.set_xlabel('Time [min]')
ax2.grid('on')
f.suptitle('Non-linear Fitting of Simulated Data')
pl.tight_layout()
# save figure
# pl.savefig('nonlinear_fit.png',dpi=600)
