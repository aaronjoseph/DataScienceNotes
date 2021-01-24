LSTM - Long Short Term Memory

LSTM's is a [[Sequence Models| sequence model]] which is capable of selectively control and regulate the flow of information.LSTM's can handle long range dependencies. This model was developed after RNN's, however due to additional complexity in the model, this model is even slower than RNN's.

---

### Key Concepts

1. Maintain a seperatte cell state from what is outputted
2. Use gates to control the flow of information
	- Forget gate gets rid of irrelevant information
	- Store relevant information from current input
	- Selectively update cell state
	- Output gate returns a filtered version of the cell state
3. Backpropogation through time with uninterrupted gradient flow

---

### Challenges of LSTM

- LSTM's have downsides, it is still a recurrent network, so if a LSTM cell is called 1000 times, a long gradient path is created. While the addition of a long-term memory channel helps, there is a limit to how much it can hold
- [[Transfer Learning]] do not work on LSTM's
- This model is state-dependent and runs serially, therefore cannot be parallized or used on GPU's - this is where [[Transformers]] shine, where input sequence can be passed in parallel
