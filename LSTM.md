LSTM - Long Short Term Memory

LSTM's is a [[Sequence Models| sequence model]] which is capable of selectively control and regulate the flow of information.

LSTM's can handle long range dependencies. 

---

### Key Concepts

1. Maintain a seperatte cell state from what is outputted
2. Use gates to control the flow of information
	- Forget gate gets rid of irrelevant information
	- Store relevant information from current input
	- Selectively update cell state
	- Output gate returns a filtered version of the cell state
3. Backpropogation through time with uninterrupted gradient flow