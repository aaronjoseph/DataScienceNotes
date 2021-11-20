Data Labeling is important since most of ML is supervised and Data Labeling solves this issue.

## Data Labeling

Methods

- Process Feedback (Direct Labeling)
- Human Labeling
- Semi-Supervised Labeling
- Active Learning
- Weak Supervision

## Process Feedback

Advantages 

- Training dataset continuous creation
- Labels evolve quickly
- Captures strong label signals

## Label Consistency

Label consistency is the practice of having consistent labels. This can be extended to two major areas of ML
- Big Data Labels
	- In big data, there are outlier data, which if mislabled will cause the algorithm to fail
- Small Data Labels
	- In small data, it is important that the data is clean and consistent

`Labeling disagreement`
- Quite often the labeler would disagree on the labels, causing Label Inconsistency
- To avoid this the following can be done
	- Use multiple labelers to label the same and use voting mechanism
	- Make use of Boderline label, wherein labels cannot be identified accurately
	- Discuss whenever there is a disagreement with MLE to come to an agreement
	- Standardize Labels : Here, different labels can be standardized
	- Merge Class : Whenever two classes are almost the same, it is best to classifiy it as the same

