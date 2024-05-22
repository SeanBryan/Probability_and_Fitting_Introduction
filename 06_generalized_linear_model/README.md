# General Linear Models

Often a process depends on a broad range of inputs, making the process appear very complex and variable at first glance. However, if the contribution of each of the inputs is linear, the process can be explained by a very simple model called a general linear model.

These models have three key advantages. The first is that they are readily explainable. In this example, we consider a model of home prices that depend on the square footage, distance to downtown, number of parks near the home, and the age of the home. The model is explainable as "every additional square foot adds X dollars to the home price, but every additional mile from downtown subtracts Y dollars from the home price" and so on for each of the other factors. This explainability means users can both qualitatively and quantitatively evaluate results from the model, yielding insights and driving decisions. In contrast, a non-linear model such as a neural network can not explain its conclusions, which limits the ability of users to evaluate results, which in turn limits the ability to confidently make decisions from the results.

The second key advantage is robustness. For example, if a linear model is given data that, without the user's knowledge, has a 10% error, due to linearity at most the output of the model will be wrong by 10%. However, with a non-linear model such as a neural network, a 10% error on the input can create an in principle unbounded error on the output. Especially if the data was near a threshold, and the 10% error pushed the model over its threshold, non-linear models can be very fragile.

Finally, the third key advantage of general linear models is that they are straightforward to train. Given a data set, a single short linear algebra formula yields the best-fit model parameters, and another short formula lets a user use these model parameters to predict an outcome when given a new data point. Neural networks on the other hand have extremely high compute requirements both to estimate the best-fit model, and when using the model to predict an outcome with a new data point.

Generalized linear models have some disatvantages. Due to their robustness, they actually perform well even when applied to problems with some non-linear processes. They perform even better if the user is able to rescale the input data in a way that (even partially) linearizes the problem. Still, when faced with a highly non-linear problem, model mismatch error grows which limits applicabiliy.

# Home Price Model

In this example, we consider a model for home prices. Each home has aspects that are known in advance of putting a home on the market for sale. In this example we assume that each home has a known square footage, a known distance to downtown, a known area of parks located near (less than 2 miles) from the home, and a known age of the home. The goal is to take these known aspects of each home, and predict the actual value of the home when it is sold in the future. Pricing models such as these have a broad range of applications. One application would be if an individual owner was considering selling their home, or was considering making a bid on a home, this model could guide both the buyer and seller towards a reasonable price. Another application would be for an investor to use the model on a broad range of homes currently on the market, and use the results to identify homes that are listed for sale much higher or much lower than the model sugggests is their true value.

To build this model, the code loads in the parameters of each home. In this case, we assume that this dataset is historical home sale data, and therefore we assume we know the actual price each of these homes last sold for. We use the framework of general linear models to create a best-fit model that maps each of the home parameters onto a predicted price. For comparison, we also perform a simple y = mx + b fit only on the square footage data. The results are plotted below.

![Home Price Model](home_price_model.png?raw=true)

# Questions

1) Read the code carefully. Does the process of loading in the data make sense? How about the process of constructing the A matrix? After reading Chapter 5.1 of the Garcia book (available in the ASU library or possibly in a PDF online), does the formula that maps the A matrix onto the best-fit parameters make sense?

2) Does the simple y = mx + b model make sense?

3) Looking at the above plot, by eye find the home with approximately 1800 square feet that costs approximately $520,000. Using the simple y = mx + b model, is that home listed at a price above, at, or below the price you would expect it to sell for? Using the full model, is that home listed at a price above, at, or below the price you would expect it to sell for? Did you get the same answer in both cases? Which model would you rather use to buy or sell this house? Why?
