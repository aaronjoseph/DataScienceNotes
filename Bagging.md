Bagging - **B**ootstrap **Agg**regat**ing**  works on the idea that suitably large number of uncorrelated errors average out to zero 

Bagging can be decomposed into two stages :

- Bootstrapping
>`Bootstrapping` is a sampling technique in which we create subsets of observations from the original dataset, with replacement. 
- In statistics, we learn about the charactersitics of the population by taking samples
- Bootstrapping learns about the sample charactersitics by taking resamples and use the information to infer the population

- Aggregating
> Here the result of the models are aggregated to make final predictions. The core idea here is, that the model makes uncorrelated errors - This could be the case since the model is trained on different data

The models are created on the the sample data. Final predication is outputted, after considering all the values of the minor models.

---

### Algorithms 

- [[Random Forest]]
- [[Bagging Meta-Estimator]]