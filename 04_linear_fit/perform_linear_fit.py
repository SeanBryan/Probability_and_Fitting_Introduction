import numpy as np
import matplotlib.pyplot as pl
import pandas as pd

# read in data from file
df = pd.read_csv('../03_generating_mock_data/04_linear_fit_data.csv')

# unpack these to individual variables
x = np.array(df['x'])
y = np.array(df['y'])

# following Garcia "Numerical Methods for Physics" Chapter 5.1
# calculate a y = mx+b fit
# assuming equal sigma=1 error bars
# use Garcia 5.11
N = len(x)
m = (N*np.sum(x*y) - np.sum(y)*np.sum(x)) / \
    (N*np.sum(x**2) - (np.sum(x))**2)
b = (np.sum(y)*np.sum(x**2) - np.sum(x)*np.sum(x*y)) / \
    (N*np.sum(x**2) - (np.sum(x))**2)

# calculate the best-fit model assuming these values
y_predicted = m*x + b

# assume (this is a significant approximation!) that our model is conceptually correct
# in this case, the only difference between the model and data would be noise
# calculate the noise level by calculating the standard deviation between model and data
measured_noise = np.std(y_predicted - y)

# using this noise level
# calculate the error on each parameter
# use Garcia 5.10 to calculate S
S = N/measured_noise**2
# use Garcia 5.11 to calculate the error on each parameter
error_on_b = np.sqrt(np.sum(x**2) / (S*np.sum(x**2) - np.sum(x)**2))
error_on_m = np.sqrt(S / (S*np.sum(x**2) - np.sum(x)**2))

# make a plot of everything
pl.ion()
f = pl.figure()
gs = f.add_gridspec(4,1)
ax1 = f.add_subplot(gs[0:3,:])
ax1.errorbar(x,y,yerr=measured_noise,fmt='*',label='Simulated Data')
ax1.plot(x,y_predicted,'-',label='Best-Fit Model: y = mx + b\nm = '+str(m)[0:5]+' +/- '+str(error_on_m)[0:5]+'\nb = '+str(b)[0:4]+' +/- '+str(error_on_b)[0:3])
ax1.plot(x,(m+error_on_m)*x + b,':',label='Slope = Nominal + Error')
ax1.plot(x,m*x + (b+error_on_b),':',label='Offset = Nominal + Error')
ax1.legend()
ax1.grid('on')
#ax1.set_xlabel('x value [arb]')
ax1.set_ylabel('y value [arb]')
ax2 = f.add_subplot(gs[3,:])
ax2.plot(x,y_predicted - y,'*')
ax2.set_ylabel('error [arb]')
ax2.set_xlabel('x value [arb]')
ax2.grid('on')
f.suptitle('Linear Fitting of Simulated Data')
pl.tight_layout()
# save figure
# pl.savefig('linear_fit.png',dpi=600)