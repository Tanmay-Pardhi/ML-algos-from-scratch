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
