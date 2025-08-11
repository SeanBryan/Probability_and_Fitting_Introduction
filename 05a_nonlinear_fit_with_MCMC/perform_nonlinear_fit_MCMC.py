import numpy as np
import matplotlib.pyplot as pl
import pandas as pd
import emcee

# read in data from file
df = pd.read_csv('../03_generating_mock_data/05_nonlinear_fit_data.csv')

# unpack these to individual variables
t = np.array(df['t'])
T = np.array(df['T'])
# make a companion array that is the error on each temperature datapoint
errT = np.ones_like(t)

# define function for the model in the form that curve_fit wants
def model_calc(t,Ti,T0,tau):
    # calculate model
    return (Ti - T0)*np.exp(-t/tau) + T0

# define the log likelihood function after https://emcee.readthedocs.io/en/stable/tutorials/line/
def log_likelihood(theta, x, y, yerr):
    Ti,T0,tau = theta
    model = model_calc(x,Ti,T0,tau)
    return -0.5 * np.sum((y - model) ** 2 / yerr**2)

# create rough initial guesses for the parameters
Ti_guess = T[0] # use the first data point as a guess for the start temperature
T0_guess = T[-1] # use the last data point as a guess for the end
tau_guess = np.max(t) - np.min(t) # use the total duration as a guess for the time constant

# use emcee to fit the data
# initial guess of parameters
pos = np.array([Ti_guess,T0_guess,tau_guess]) + + 1e-4 * np.random.randn(32, 3)
nwalkers, ndim = pos.shape

# set number of steps to take
Nsamples = 5000

sampler = emcee.EnsembleSampler(
    nwalkers, ndim, log_likelihood, args=(t, T, errT)
)
sampler.run_mcmc(pos, Nsamples, progress=True)

flat_samples = sampler.get_chain(discard=int(np.round(0.1*Nsamples)), thin=15, flat=True)

# unpack the "average" best-fit parameters
Ti = np.mean(flat_samples[:,0])
T0 = np.mean(flat_samples[:,1])
tau = np.mean(flat_samples[:,2])

# find the errors on each parameter
error_on_Ti = np.std(flat_samples[:,0])
error_on_T0 = np.std(flat_samples[:,1])
error_on_tau = np.std(flat_samples[:,2])

# calculate the best-fit model
T_predicted = model_calc(t,Ti,T0,tau)

# plot everything
pl.ion()
f = pl.figure()
gs = f.add_gridspec(4,1)
ax1 = f.add_subplot(gs[0:3,:])
ax1.errorbar(t,T,yerr=errT,fmt='*',label='Simulated Data')
ax1.plot(t,T_predicted,'-',label='Best-Fit Model\nTi = '+str(Ti)[0:5]+' +/- '+str(error_on_Ti)[0:4]+'\nT0 = '+str(T0)[0:4]+' +/- '+str(error_on_T0)[0:4]+'\ntau = '+str(tau)[0:5]+' +/- '+str(error_on_tau)[0:4])
ax1.plot(t,model_calc(t,Ti+error_on_Ti,T0,tau),':',label='Ti = Nominal + Error')
ax1.plot(t,model_calc(t,Ti,T0+error_on_T0,tau),':',label='T0 = Nominal + Error')
ax1.plot(t,model_calc(t,Ti,T0,tau+error_on_tau),':',label='tau = Nominal + Error')
ax1.legend()
ax1.grid('on')
#ax1.set_xlabel('x value [arb]')
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

# make corner plot
import corner

fig = corner.corner(flat_samples,labels=['Ti','T0','tau'],truths=[30,10,25])