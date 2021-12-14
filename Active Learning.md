- This technique samples data intellegently
	- Herein, unlabelled data are sampled based on the most value that can be derived out of labelling it
- This is very useful in scenario wherein
	- There is constrained budget : you can only afford to label a few points
	- Imbalanced dataset : Help select rare classes for training
	- Target metrics : when baseline sampling strategy does not imporve selected metrics

## Active Learning Sampling techniques

**Margin Sampling** : Label points the current model is least confident in

**Cluster-based sampling** : sample from well-formed clusters to cover the entire space

**Query by committee** : Train an ensemble of models and sample points that generate disagreement

**Region based sampling** : Runs several active learning algorithms in different paritions of the space