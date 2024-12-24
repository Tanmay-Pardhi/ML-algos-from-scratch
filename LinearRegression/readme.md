The whole goal of the algo is to fix a line such that for any new dependent variables data point we can fix it and then get the independent variables based on it

So we need to find the right weights and the right bias

Parameters - Learning_Rate and num_iterations

Fitting - 
1) Start by calulating the number of samples (rows) and number of features (columns/dependent vars)
2) Set weights as zero for each of the feature/column
3) Set bias as zero
4) For each num_iteration:
    1) Calculate y_pred, y_pred = (X.weights) + bias (y=mx+c)
    2) Next we will have to calculate the gradients for the weights and the bias
    3) dw = (1/num_samples) * (X_transpose.(y_pred - y))
    4) db = (1/num_samples) * Summation(y_pred - y)
    5) Update weights and bias
    6) weights = weights - learning_rate*dw
    7) bias = bias - learning_rate*db

Prediction - 
For unseen data (X)
Based on the finalized weights and bias put it in the equation y_pred = (X.weights)+bias
