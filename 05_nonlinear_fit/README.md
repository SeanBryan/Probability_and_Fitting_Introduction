# Non-linear Fitting

Some processes are governed by models that are not linear in their parameters. In this example, we consider an object that starts at a temperature Ti, and cools asymtotically towards a temperature T0 with a decay rate of tau. The model takes the form

T(t) = (Ti - T0)*exp(-t/tau) + T0

This model is non-linear in the parameter tau, since increasing it by a percentage does not translate in to the same increase in the model output. This means that there does not exist a closed-form formula to estimate the best-fit parameters given a measured dataset.

As reviewed in Bevington and Robinson's book, and other places, non-linear fitting is a broad class of algorithms that estimate the best-fit value of the non-linear parameters in a model, given an input dataset. In this example, we use the curve_fit function built in to scipy. Reading the documentation page, linked below, is very useful since it contains a lot of features. The function asks the user to provide an initial guess value for each of the parameters. It calculates the model for these parameters, and in turn calculates the total mean squared error (MSE) between this model and the data. The function then tries changing each parameter value by a small amount, and evaluates whether the MSE improves or get worse. It then selects an adjustment for each of the parameters, and takes a step in that direction. This process is repeated until the function finds the best MSE, and it in turn reports the parameters as the best-fit parameters to the user.

In this example, we use curve_fit to fit our non-linear cooling model to mock data, and also to estimate the error on each of the parameters.

https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.curve_fit.html

As shown in the figure below, curve_fit finds a model that explains the observed data well.

![Non-linear Model](nonlinear_fit.png?raw=true)

# Questions

1) Read through the code. Does the process for loading the data make sense? How about the process of declaring a function in the format required by curve_fit? Does the call to curve_fit make sense?

2) Generating an initial guess for parameters by hand is tedious when analyzing many data sets automatically. Look at the procedure for generating the initial guess? What assumptions did I make here? Do you agree with them? What is a situation where this yields a good initial guess? What is a different situation where this would not yield an initial guess close enough for curve_fit to find a model?

3) Make a copy of the code, edit it to let you input an initial guess by hand, and re-run the code. Does the code still find a good fit? Change the initial guess in different ways until the code no longer is able to find a good fit. How much did you need to change it? Does this make you think that curve_fit is robust to incorrect initial guesses in this situation?
