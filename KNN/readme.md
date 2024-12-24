# Logic behind the algo

1) We are using Euclidean distance to calculate the distance here
2) Paramter that can be passed is K i.e. Number of nrighbors to be considered

3) Let's look at how the predict function works

a) We predict the category individually for each data point

b) The _predict begins by calculating the distance of the point with respect to the train data

c) Then we calculate the indices of the top k shortest distances from the point being considered.

d) Then we get the category of these indices data points

e) Then based on all the categories that we got, we calculate the mode of it (most common)

f) This is the prediction for that datapoint and the same process is continued for the other individual test points.
