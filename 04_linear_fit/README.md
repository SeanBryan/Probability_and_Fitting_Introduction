# Linear fitting

In some cases, a process y depends linearly on a single input variable x, possibly with an overall offset. The entire model is y = mx + b. Given a dataset of x and y coordinates, there is a closed-form formula to obtain the best fit slope m, the best fit offset b, and the error on both parameters. Chapter 5.1 of Garcia's "Numerical Methods for Physics" discusses and derives these formulas, and this code implements them.

As shown below, when given data with error, the best-fit line explains the trend well. This plot also overplots lines that have been shifted by the error on the slope, and also by the error on the offset, to illustrate the range of trend lines that are still compatible with the noise in the data.

![Linear Model](linear_fit.png?raw=true)

# Questions

1) Read through the code carefully. Does loading the data make sense? Does using the formulas to estimate the slope and offset make sense?

2) To determine the noise level, the code makes a key assumption. What is this assumption? What is a situation where you think this would be a valid assumption? What is another situation where this assumption could lead to an incorrect conclusion?

3) Find the lines on the plot, and the corresponding lines of code, that are shifted by the error on the slope and offset. Does the amount of the shift in the line surprise you? Is it larger, about the same size, or smaller than you expected? What was the basis of your initial estimate? Do you have an explanation of the actual shift as shown on the plot?

4) Go to the board, or on scratch paper, and sketch the only leftmost and rightmost data points on an xy axis. Add their error bars to your drawing. Given these two data points, draw what you believe would be the best-fit line. Then draw what you believe would be the best fit line shifted by one error bar on the slope. Then draw what you believe would be the best-fit line shifted by one error bar on the offset. Make a copy of the code and re-run it to analyze only these two data points. Does the result agree with your expectation? Why or why not?
