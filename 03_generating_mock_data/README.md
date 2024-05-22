# Generating Mock Data

When developing a new data analysis algorithm, or when developing a new instrument or experiment, it is useful to have access to data early in the process that looks similar to real data that the instrument will produce when in operation. It is also useful to have access to data where the underlying ground truth is known (since it was decided by the user who produced the simulated data) to verify that the data analysis algorithm is able to produce estimates that agree with the ground truth.

In this section, we generate several mock datasets that we will use in the later linear, non-linear, and generalized linear fitting algorithms introduced in subsequent sections.

To illustrate linear fitting, we generate data that consists of x and y datapoints with errorbars on the y values.

![Linear Data wth Noise](line_data_with_noise.png?raw=true)
