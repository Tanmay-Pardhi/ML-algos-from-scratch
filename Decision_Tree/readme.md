1. To create a tree we will first need to create nodes, For classification we need to divide our original data into nodes
2. Internal nodes do not have any value since their task is to only split the data while leaf node contains value i.e. the end result
3. Each node consists of <br/>
    1. feature - The column based on which the splitting will occur
    2. Threshold - Defines the specific value of the feature that is used to create the split. EX: >5 <5 etc.
    3. Left
    4. Right
    5. Value
    6. Function is_leaf_node - Checks if the current node is a leaf (a terminal node with a final output) or an internal node (still needing further splits).

4. Parameters -
   1. min_samples_split - Specifies the minimum number of samples required to split an internal node. <br/>
      Why - <br/>
      1. This parameter prevents the tree from overfitting by stopping the growth of the tree when there are very few samples at a node. If a node has fewer samples than this value, it becomes a leaf node instead of being further split. This can also improve computational efficiency.
   2. max_depth - Specifies the maximum depth of the tree. <br/>
     Why - <br/>
         1. Limiting the depth of the tree helps prevent overfitting, as overly deep trees can memorize the training data rather than generalizing. It also reduces computation time and memory usage. If the depth of the tree exceeds this value, further splitting is halted.
   3. n_features - Determines the number of features to consider when finding the best split at each node. <br/>
      Why - <br/>
      1. By default, decision trees evaluate all features to find the best split at every node. However, this can sometimes lead to overfitting because the tree might heavily rely on specific features that perfectly split the training data but do not generalize well. <br/>
      2. The n_features parameter introduces randomness by limiting the number of features considered for splitting at each node. This is especially useful in ensemble methods like Random Forest, where trees are trained on subsets of features to improve generalization. <br/>
   5. root - The root is the topmost node and serves as the reference for traversing the tree during prediction. <br/>
      Why - <br/>
      1. Once the tree is trained using fit(), the root node stores the entire tree structure, including all splits, thresholds, and child nodes. <br/>
      2. During prediction (predict), traversal begins from the root node to navigate through the tree based on the features of the input data. <br/>


Fitting - <br/>

1. The process to train the decision tree starts by specifying the num_features = X.shape[1] just like the other algo or the minimum of n_features param or shape[1]
2. Next, we recursively grow the tree from the root.
3. grow_tree Method (Recursive Tree Construction) <br/>
    The heart of this function is to check if the stopping criterias are met or not <br/>
       1. depth >= self.max_depth: If the current depth of the tree exceeds the maximum depth (max_depth), stop growing the tree. <br/>
       2. n_labels == 1: If all the data points in the current subset belong to the same class, stop. This means the node is pure. <br/>
       3. n_samples < self.min_samples_split: If the current subset has fewer than the minimum number of samples required to split further, stop. <br/>
   If any of these conditions are met, the node is turned into a leaf node, and the most common label in y is returned as the value for the leaf node. <br/> <br/>
   If none of the stopping conditions are met, we randomly choose a subset of features (n_features) to consider for the next split. This helps introduce randomness into the tree, and it's particularly useful in ensemble methods like Random Forest. <br/>

   The function then proceeds to find the best feature and threshold to split the data<br/>
    The _best_split method evaluates all the possible splits based on the features selected in feat_idxs and calculates which split maximizes information gain<br/>

   Once the best feature and threshold are identified, the dataset is split into two subsets<br/>
   _split function divides the data into left and right subsets based on whether the feature value is less than or equal to the threshold (best_thresh) or greater than the threshold.<br/>

   After splitting the data, the function recursively grows the left and right child nodes<br/>

   After constructing both child nodes, a Node is created with the best feature index, threshold, left child, and right child. This node becomes part of the tree.<br/>

4. _best_split Method (Finding the Best Feature and Threshold)<br/>
    The aim is to find split such that the information gain from the split is maximum<br/>
   1. Set best_gain as -1 and split_idx and split_thr as None
   2. For each feature_idx:
       1. Take all samples in it and take all unique samples as threshold
       2. Now for each individual threshold
          1. Calculate information gain
          2. If inf gain greater than best_gain
          3. Set best_gain as new gain, set split_idx as the current index and set split_thr as current thr val
5. information_gain Method
   1. Based on the split_thr value split the X_column into left and right
   2. Using the y values calculate the parent entropy
   3. Information gain = parent entropy - child entropy
