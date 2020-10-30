Neural networks are prone to overfitting. The concept of overfitting emerged in 2012.

Prior to dropouts, regularization methods such as L1 and L2 weight penalties were used, however did not completely solve this issue. This is due to `co-adaptation`

### Co-adaptation

The major pit-fall in the learning of large neural networks is co-adaptation, in such a network as we are training the neural network, since all weights are trained together, it is possible for some of the connection to have more predictive capability than the others.

In such scenario, as we iteratively train the model further, the powerful connections are learning more than while the weaker ones are ignored. Over multiple iteration, only a fraction of the nodes are being actively trained due to the strength of the connection. This phenomenon is called co-adaptation.

### Formulae Intuition 

https://towardsdatascience.com/simplified-math-behind-dropout-in-deep-learning-6d50f3f47275

