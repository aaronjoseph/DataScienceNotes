Sigmoid function is used for the two-class logistic regression whereas softmax function is used for multi-class logistic regression.

Suppose we plug a sigmoid function and a softmax function to the end of a neural network
- Sum of all sigmoid functions can be above or below 1, whereas, for softmax function, it is all interrelated, and the sum equals 1. Therefore, for softmax function, when value of one class goes down, the other increases

### Use Cases

`Sigmoid` 
Sigmoids are used, wherein there can be a possibility of more than 1 classes occuring for a given data-point, since summation of sigmoid output doesn't converge to 1.

`Softmax`
Given a case wherein, strictly speaking there can be only one class, softmax is the go-to function to be used

Both use the mathematical exponential term e, which equates to 2.71828.

[[Exponetial Constant - e| Interesting facts on the mathematical constant e]]

### Sigmoid 

Sigmoids are used when the following is true
- Multi-Label Classification (More than one right answer)
- Non-Exclusive outputs

When such is the case, wherein we have more than 1 right answer, sigmoid is applied to each element of the raw output, independently 

Sigmoid function has the form
$$\sigma(z_j) = \frac{e_j^z}{1+e_j^z}$$

### Softmax

Softmax's are preferred when
- Multi-Class Classification (Only one right answer)
- Mutually Exclusive Outputs

Softmax ensures the probability of all the outcomes comes out as 1
Softmax formulae looks as follows

$$softmax(z_j) = \frac{e_j^z}{\sum_{k=1}^{K}e_k^z}$$
