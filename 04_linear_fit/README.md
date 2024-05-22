# Linear fitting

In some cases, a process y depends linearly on a single input variable x, possibly with an overall offset. The entire model is y = mx + b. Given a dataset of x and y coordinates, there is a closed-form formula to obtain the best fit slope m, the best fit offset b, and the error on both parameters. Chapter 5.1 of Garcia's "Numerical Methods for Physics" discusses and derives these formulas, and this code implements them.

As shown below, when given data with error, the best-fit line explains the trend well. This plot also overplots lines that have been shifted by the error on the slope, and also by the error on the offset, to illustrate the range of trend lines that are still compatible with the noise in the data.


