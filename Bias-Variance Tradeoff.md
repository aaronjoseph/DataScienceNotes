Theoretical results of statistics and Machine Learning is the fact that a model's generalization errors can be expressed as the sum of 3 erros

- Bias
	- This generalization error is due to the wrong assumptions. A high-bias model is most likely to underfit the training data
	- It also means the model cannot model the training data nor generalize to new data
	- This will also have poor performace to training data
	- A model is said to be biased if it consistently under or over-predicts the target variables
- Variance
	- This is caused due to the models sensitivity to small variations in the training data. A model with high degree of freedom is likely to have high variance and thus overfit the data
	- Models with high variance are highly sensitive to change in training data, meaning to say, slight changes in the training data will affect the model 
- Irreducible Error
	- This is due to the noisiness of the data. This can be handled by data cleaning

### Bias Variance Trade-off

Increasing model complexity will increase variance and reduce bias.
Decreasing model complexity will increase bias and reduce variance.
Hence called Bias-Variance Tradeoff
