import numpy as np
from collections import Counter

def euclidean_distance(x1, x2):
    distance = np.sqrt(np.sum((x1-x2)**2))
    return distance

class KNN:
    def __init__(self, k=3):
        self.k = k

    def fit(self, X, y):
        self.X_train = X
        self.y_train = y

    def predict(self, X):
        predictions = [self._predict(x) for x in X]
        return predictions

    def _predict(self, x):
        # compute the distance
        distances = [euclidean_distance(x, x_train) for x_train in self.X_train]
    
        # get the closest k
        k_indices = np.argsort(distances)[:self.k]
        k_nearest_labels = [self.y_train[i] for i in k_indices]

        # majority voye
        most_common = Counter(k_nearest_labels).most_common()
        return most_common[0][0]


# Logic behind the algo

# 1) We are using Euclidean distance to calculate the distance here
# 2) Paramter that can be passed is K i.e. Number of nrighbors to be considered

# 3) Let's look at how the predict function works

# a) We predict the category individually for each data point

# b) The _predict begins by calculating the distance of the point with respect to the train data

# c) Then we calculate the indices of the top k shortest distances from the point being considered.

# d) Then we get the category of these indices data points

# e) Then based on all the categories that we got, we calculate the mode of it (most common)

# f) This is the prediction for that datapoint and the same process is continued for the other individual test points.
