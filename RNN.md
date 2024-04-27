RNN is the most basic model used for [[Sequence Models|sequence modeling]].

RNN's are used on sequential data. RNN can be scaled for large scale sequence, however, due to vanishing gradients, RNN's tend to forget due to large sequence - `long term dependencies` can have issues. Also, RNN's are slow to compute as well. Furthermore, it has difficulty in accessing information from a long time ago. 

---
![[Pasted image 8.png]]

In a **vanilla** recurrent neural network as the name suggests, the network applies a function $f_w$ which is parameterized on the previous state $h_{t-1}$ and the current input $x_t$  

---
### Disadvantages of RNN's

Vanilla RNN's have trouble with [[Vanishing & Exploding Gradients]] gradients during backprop -> hard to calculate deep layers
- Exploding Gradients can be fixed using gradient clipping (Gradient Thresholding)
- Vanishing Gradient, this can be fixed by 
	- Activation Function
	- Parameter Initialization
	- Network Architecture
		- [[LSTM]]'s 
		- GRU's
- Slow to train
	- It is quite slow and is hardware intense

---

### Solving Vanishing [[Gradient Descent]]  

1. Choice of Activation Function

Here, ReLU can be used as the derivative of ReLU stays 1 for x >0 and 0 other wise, this is a better choice than tanh and sigmoid derivative

2. Parameter Initialisation

Here, initialise weights to identity matrix. Initialise biases to zero. This, will prevent weights from shrinking to zero during backpropogation

3. Network Architecture

Here we can use complex recurrent unit with gates to control what information is passed through. Here [[LSTM]] or GRU's  can be utilized in this regard

