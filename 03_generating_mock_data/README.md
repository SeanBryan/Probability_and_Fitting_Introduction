# Generating Mock Data

When developing a new data analysis algorithm, or when developing a new instrument or experiment, it is useful to have access to data early in the process that looks similar to real data that the instrument will produce when in operation. It is also useful to have access to data where the underlying ground truth is known (since it was decided by the user who produced the simulated data) to verify that the data analysis algorithm is able to produce estimates that agree with the ground truth.

In this section, we generate several mock datasets that we will use in the later linear, non-linear, and generalized linear fitting algorithms introduced in subsequent sections.

To illustrate linear fitting, we generate data that consists of x and y datapoints with errorbars on the y values. After choosing the x values by hand, and after choosing the ground-truth parameter values for the slope m and offset b, we generate the y data. Then we add noise to the data, before saving it to a file for later analysis and plotting the data for visualization.

![Linear Data wth Noise](line_data_with_noise.png?raw=true)

To illustrate non-linear fitting, we generate data of a warm object cooling down over time. After choosing the time values, and after choosing ground truth values for the initial temperature, final temperature, and the time constant of the cooling, we generate the temperature vs time data. We then add noise before saving it to a file for later analysis and plotting the data for visualization.

![Temperature Data wth Noise](temperature_data_with_noise.png?raw=true)

To illustrate general linear models, we generate data reflecting a large number of homes that each have several factors that will influence the sale price of the home. We select ground-truth values for the extent to which each factor influences the home price, then we generate the actual home prices. To reflect the fact that other unknown factors will also impact a home price, we add additional Gaussian variation, and an overall offset, before saving the data to a file for later analysis and plotting the data for visualization.

![Temperature Data wth Additional Variation](home_price_data.png?raw=true)

# Questions

1) Read the code carefully. What patterns do you see across the three different mock data generation processes? What elements of generating the mock data are the same in all three cases? For each case, what is unique about that case?

2) What assumptions are made in each of the three cases? Do you agree with each of these assumptions? Why or why not?

3) Look at the ground-truth values selected for each of the three cases. What factors go into selecting these? Do you agree with the values? Why or why not?
