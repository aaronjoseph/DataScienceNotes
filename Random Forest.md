Random Forest is an ensemble learning method that constructs multiple decision trees during training and outputs the mode of the classes (classification) or mean prediction (regression) of the individual trees. This approach enhances predictive accuracy and controls overfitting.Random-Forest is basically [[Bagging| bagging technique]].

**Key Characteristics of Random Forest:**

1. **Ensemble Technique**: Combines the predictions of several decision trees to improve overall model performance.
2. **Random Sampling (Bagging)**: Each tree is trained on a random subset of the training data, selected with replacement (bootstrap sampling).
3. **Feature Randomness**: At each split in a tree, a random subset of features is considered, promoting diversity among trees and reducing correlation.

**How the Random Forest Algorithm Works:**
1. **Bootstrap Sampling**: From the original dataset containing _N_ instances, create _B_ bootstrap samples by randomly selecting _N_ instances with replacement.
2. **Tree Construction**: For each bootstrap sample, grow an unpruned decision tree:
	1. At each node, select _m_ features randomly from the total _M_ features (_m_ << _M_).
	2. Determine the best split among the _m_ features.
	3. Split the node into child nodes.
	4. Repeat until the maximum depth is reached or further splitting is not possible.
3. **Aggregation**:
	1. **For Classification**: Each tree votes for a class, and the class with the majority votes is the final prediction.
	2. **For Regression**: The predictions from all trees are averaged to produce the final output.

