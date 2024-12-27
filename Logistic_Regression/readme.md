The whole goal of the algo is to get a probability i.e. between 0 and 1 (inclusive) to predict a class based on that probability

So we need to find the right weights and the right bias

Parameters - Learning_Rate and num_iterations

Fitting -

Start by calulating the number of samples (rows) and number of features (columns/dependent vars)
Set weights as zero for each of the feature/column
Set bias as zero
For each num_iteration:
Start by calculating the linear prediction linear, linear = (X.weights) + bias (y=mx+c)
Next convert this linear prediction into probability by using the sigmoid function
Sigmoid function = 1/(1+e^-x) This will give us a value between 0 and 1
Next we will have to calculate the gradients for the weights and the bias
dw = (1/num_samples) * (X_transpose.(y_pred - y))
db = (1/num_samples) * Summation(y_pred - y)
Update weights and bias
weights = weights - learning_rate*dw
bias = bias - learning_rate*db
Prediction - For unseen data (X) Based on the finalized weights and bias first calculate the linear prediction
linear = (X.weights)+bias
y_pred = sigmoid(linear)
Next based on the value of y_pred if the value is less than equal to 0.5 then it is classified as 0 else 1