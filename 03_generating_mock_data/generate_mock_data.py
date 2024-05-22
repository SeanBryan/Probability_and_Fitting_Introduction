import numpy as np
import matplotlib.pyplot as pl
import pandas as pd

###############################################################################################
# generate mock data for 04 - linear fit

# choose actual ground-truth parameters for the line to be generated
m = 3.7
b = -1.4

# choose x values
x = np.array([-6.7, -6.3, -3.2, -2.8, -0.9, -0.7, -0.5, 1.1, 2.5, 2.8, 3.3, 3.6, 4.0, 5.9])

# choose noise level
noise_level = 5.0

# generate true y-values
y = m*x + b

# add noise
y += noise_level*np.random.randn(len(y))

# save these to a plain text file using pandas
#            create pandas dataframe from a dictionary
#                                      save that dictionary to a CSV file
#                                                                      do not write a column for the '0,1,2,3,...' row index
pd.DataFrame.from_dict({'x':x, 'y':y}).to_csv('04_linear_fit_data.csv',index=False)

# make a plot of the results
pl.ion()
pl.figure()
pl.errorbar(x,y,yerr=noise_level,fmt='*')
pl.xlabel('x value [arb]')
pl.ylabel('y value [arb]')
pl.title('Simulated Line Data with Noise')
# save the figure
# pl.savefig('line_data_with_noise.png',dpi=600)



###############################################################################################
# generate mock data for 05 - non-linear fit

# choose ground truth values
# consider an object cooling, starting at a temperature Ti
Ti = 30 # C
# in an environment at temperature T0
T0 = 10 # C
# with a time constant of tau
tau = 25 # minutes

# simulate temperature-vs-time data with noise
# choose a range of times to measure
t = np.arange(0,120,1)

# calculate the temperature
T = (Ti - T0)*np.exp(-t/tau) + T0

# choose the noise level
noise_level = 1.0

# add noise
T += noise_level*np.random.randn(len(T))

# save these to a plain text file using pandas
pd.DataFrame.from_dict({'t':t, 'T':T}).to_csv('05_nonlinear_fit_data.csv',index=False)

# make a plot of the results
pl.figure()
pl.errorbar(t,T,yerr=noise_level,fmt='*')
pl.xlabel('Time [min]')
pl.ylabel('Temperature [deg C]')
pl.title('Simulated Non-Linear Cooling Data with Noise')
# save the figure
# pl.savefig('temperature_data_with_noise.png',dpi=600)


###############################################################################################
# generate mock data for 06 - generalized linear model

# choose ground truth values

# consider a simplified model of house prices where
# the price of the home (condo or single-family) depends linearly on several factors
# the price per square foot
dollars_per_square_foot = 400
# a longer commute from downtown makes the price less expensive
dollars_per_mile_from_downtown = -2000
# parks nearby (within 2 miles) makes the price higher
# say that 0.1 square miles of neighborhood parks, makes the price $10k higher
dollars_per_square_mile_of_nearby_parks = 10000 / 0.1
# older homes tend to be less expensive since they require more repairs
# say that a 10 year old home makes the price $25k lower
dollars_per_year_of_home_age = -25000 / 10

# generate a distribution of homes that each have their own unique combination of factors
Nhomes = 10000
square_footage = np.random.rand(Nhomes)*1200 + 800
miles_from_downtown = np.random.rand(Nhomes)*30
square_miles_of_nearby_parks = np.random.rand(Nhomes)*0.3
age_of_home = np.abs(np.random.randn(Nhomes))*25 # note that this makes more new homes than old homes

# square footage is usually rounded to the nearest square foot
square_footage = np.round(square_footage)

# generate the price of homes, assuming they followed this model perfectly
home_price = square_footage*dollars_per_square_foot +\
             miles_from_downtown*dollars_per_mile_from_downtown +\
             square_miles_of_nearby_parks*dollars_per_square_mile_of_nearby_parks+\
             age_of_home*dollars_per_year_of_home_age

# home prices do not follow this model exactly, there are many other unknown factors that drive a home price
# simulate this by adding random variation to the prices
# (note, this isn't "noise" since the true home price is not uncertain and is known to the exact penny at sale,
#  however, the factors driving this price are not fully known,
#  meaning there will be additional variation observed in the prices)
home_price += 10000*np.random.randn(Nhomes)

# add an overall offset to the prices, again capturing that there are unknown factors driving the price
home_price += 20000

# homes are sold to the nearest dollar, so round the prices
home_price = np.round(home_price)

# save the factors and the home prices to a csv file
pd.DataFrame.from_dict({'square_footage':square_footage,\
                        'miles_from_downtown':miles_from_downtown,\
                        'square_miles_of_nearby_parks':square_miles_of_nearby_parks,\
                        'age_of_home':age_of_home,\
                        'home_price':home_price}).to_csv('06_generalized_linear_fit_data.csv',index=False)

# plot the first few homes to illustrate the broad trends
pl.figure(figsize=(10,10))
pl.subplot(2,2,1)
pl.plot(square_footage[0:100],home_price[0:100]/1000,'.')
pl.xlabel('Square Footage [ft^2]')
pl.ylabel('Home Price [Thousands of USD]')
pl.grid('on')
pl.subplot(2,2,2)
pl.plot(miles_from_downtown[0:100],home_price[0:100]/1000,'.')
pl.xlabel('Distance from Downtown [mi]')
pl.ylabel('Home Price [Thousands of USD]')
pl.grid('on')
pl.subplot(2,2,3)
pl.plot(square_miles_of_nearby_parks[0:100],home_price[0:100]/1000,'.')
pl.xlabel('Nearby Parks [mi^2]')
pl.ylabel('Home Price [Thousands of USD]')
pl.grid('on')
pl.subplot(2,2,4)
pl.plot(age_of_home[0:100],home_price[0:100]/1000,'.')
pl.xlabel('Age of Home [yr]')
pl.ylabel('Home Price [Thousands of USD]')
pl.grid('on')
pl.gcf().suptitle('Simulated Home Price Data')
pl.tight_layout()
# save the figure
# pl.savefig('home_price_data.png',dpi=600)
