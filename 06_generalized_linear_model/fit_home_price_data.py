import numpy as np
import matplotlib.pyplot as pl
import pandas as pd

# load house price data
df = pd.read_csv('../03_generating_mock_data/06_generalized_linear_fit_data.csv')

# unpack these to individual variables
square_footage = np.array(df['square_footage'])
miles_from_downtown = np.array(df['miles_from_downtown'])
square_miles_of_nearby_parks = np.array(df['square_miles_of_nearby_parks'])
age_of_home = np.array(df['age_of_home'])
home_price = np.array(df['home_price'])

# following Garcia "Numerical Methods for Physics" Chapter 5.1
# form a matrix containing all of the different factors in the house price
# also include an overall offset term
# use Garcia 5.27
A = np.vstack((square_footage,\
               miles_from_downtown,\
               square_miles_of_nearby_parks,\
               age_of_home,\
               np.ones_like(square_footage)))

# find the linear fit parameters
# use Garcia 5.28
params = np.linalg.inv(A @ A.transpose()) @ A @ home_price

# unpack this array into named parameters
dollars_per_square_foot = params[0]
dollars_per_mile_from_downtown = params[1]
dollars_per_square_mile_of_nearby_parks = params[2]
dollars_per_year_of_home_age = params[3]
offset_dollars = params[4]

# calculate the best-fit model
predicted_home_price = square_footage*dollars_per_square_foot +\
                       miles_from_downtown*dollars_per_mile_from_downtown +\
                       square_miles_of_nearby_parks*dollars_per_square_mile_of_nearby_parks+\
                       age_of_home*dollars_per_year_of_home_age +\
                       offset_dollars

# for comparison, calculate a quick y = mx+b style fit
# only considering the square footage
# use Garcia 5.11
N = len(home_price)
m = (N*np.sum(square_footage*home_price) - np.sum(home_price)*np.sum(square_footage)) / \
    (N*np.sum(square_footage**2) - (np.sum(square_footage))**2)
b = (np.sum(home_price)*np.sum(square_footage**2) - np.sum(square_footage)*np.sum(square_footage*home_price)) / \
    (N*np.sum(square_footage**2) - (np.sum(square_footage))**2)
naive_predicted_home_price = m*square_footage + b

# plot the first few homes to get an idea of the trends
pl.ion()
f = pl.figure()
gs = f.add_gridspec(4,1)
ax1 = f.add_subplot(gs[0:3,:])
ax1.plot(square_footage[0:100],home_price[0:100]/1000,'k*',label='True Home Prices')
ax1.plot(np.nan,np.nan,'-') # placeholder to skip ahead in the color order
ax1.plot(square_footage[0:100],predicted_home_price[0:100]/1000,'.',label='Full Model Predicted Home Price\nRMS Error = '+str(int(np.round(np.std(home_price - predicted_home_price)/1000)))+' k$')
ax1.plot(square_footage[0:100],naive_predicted_home_price[0:100]/1000,'-',label='Simple Model Predicted Price\nRMS Error = '+str(int(np.round(np.std(home_price - naive_predicted_home_price)/1000)))+' k$')
ax1.legend()
ax1.grid('on')
#ax1.set_xlabel('Square Footage [ft^2]')
ax1.set_ylabel('Home Price [Thousands of USD]')
ax2 = f.add_subplot(gs[3,:])
ax2.plot(np.nan,np.nan,'-') # placeholder to skip ahead in the color order
ax2.plot(square_footage[0:100],(home_price[0:100] - predicted_home_price[0:100])/1000,'*',label='Full Model Predicted Home Price')
ax2.plot(square_footage[0:100],(home_price[0:100] - naive_predicted_home_price[0:100])/1000,'.',label='Simple Model Predicted Price')
#ax2.legend()
ax2.grid('on')
ax2.set_xlabel('Square Footage [ft^2]')
ax2.set_ylabel('Error [k$]')
f.suptitle('Home Prices vs Square Footage')
pl.tight_layout()
# save the figure
# pl.savefig('home_price_model.png',dpi=600)