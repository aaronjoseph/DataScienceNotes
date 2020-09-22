<a href = "https://arxiv.org/pdf/1709.01907.pdf"> Paper </a>

When [[LSTM]]'s are provided with numerous dimensions, it is able to model complex nonlinear feature interactions -> which is relevant for complex extreme events forecasting

There is a need to model uncertainity to the predictions, especially in the context of anomaly detection. 

Bayesian Neuaral Networks can be used as a framework to provide uncertainty, under 3 types
- Model uncertainty
- Inherent Noise
- Model Misspecification

Advantages of LSTM's
- Is end-to-end in nature
- Any modification, so as to add exogenous variables is easier due to the model architecture
- Other models will require frequent re-tuning  and manual feature extractio, which is prohibitive to large scale systems with millions of time-series

Bayesian Neural Networks
- Bayesian Neural Network introduce uncertain to the model

Model Design
1. Encoder-Decoder 
	1. This is used to capture inherent patterns in time series, which is learned during pre-training step
2. Prediction Network 
	1. This takes input from both Encoder-Decoder Network and other external features to guide the predictions

