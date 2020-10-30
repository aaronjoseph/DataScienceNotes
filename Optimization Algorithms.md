Neural networks are employed to solve big-data problems, however, since the process is highly empirical, there needs to be ways to ensure faster computation. Optimization algorithm ensures faster convergence.

---

### Notes on [[Gradient Descent]]

---

### Exponentially Weighted Averages

Exponentialy weighted average works on the following formulae

$$V_t = \beta V_{t-1} + (1-\beta)\theta_t$$

Here higher $\beta$ will ensure the new value will be dependent on more older values

### Gradient Descent with Momentum

Momentum helps accelerate SGD in the relevant direction. Idea here is that in gradient descent, oscillation is limited

Exponentially Weighted Average on Weights
$$v_{dW} = \beta v_{dW} + (1-\beta)dW$$
Exponentially Weighted Averages on Beta
$$v_{db} = \beta v_{db} + (1-\beta)db$$

The base equations above, $\beta$ can be considered as friction, while the product can be considered as momentum, second term can be analogous to acceleration

Final Update 

W = W - $\alpha v_{dw}$
b = b - $\alpha v_{db}$


### RMSProp - Root Mean Squared Propogation

This algorithm uses exponentially weighted averages. This algorithm is adaptive, allows for individual adjustment of the learning rate for each parameter of the model. 

The equations are built over Momentum equtions with some modifications - here you can go with larger $\alpha$ values for faster optimisation

Formulaes


Exponentially Weighted Average on Weights
$$S_{dW} = \beta S_{dW} + (1-\beta)dW^2$$
Exponentially Weighted Averages on Beta
$$S_{db} = \beta S_{db} + (1-\beta)db^2$$

W = W - $\alpha \frac{dw}{\sqrt{S_{dW}}}$
b = b - $\alpha \frac{db}{\sqrt{S_{db}}}$

> It is called root mean squared since we are squaring the values and then using square root in the update rule


### Adam - Adaptive Moment Estimation

Works on wide range of problems in deep-learning

It is an algorithm like RMSprop . works well in a wide range of applications. It takes advantage of the biggest pros of RMSProp and combine them with ideas known from momentum optimization.  

### AdaGrad

This is a gradient descent optimization technique. Adagrad adapts the learning rate specifically to individual features, that means that some of the weights in your dataset will have different learning rates than others. 

It is an optimizer with parameter specific learning rates, which are adapted relative to how frequently a parmet gets updated during training. The more update a parameter receives, the smaller the updates


### Nadam Optimization - Nesterov Accelerated Adaptive Moment Estimation

NADAM is Adam with Nesterov Momentum. Adam can be viewed as a combination of RMSProp and momentum

### Adadelta

Adadelta is an extension of Adagrad that seeks to reduce its aggressive, monotonically decreasing learning rate.


### Nesterov Accelerated Gradient