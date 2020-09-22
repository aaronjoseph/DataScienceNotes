Architecture of transformer network is quite complex. 

> Key advantage of transformers is that it doesn't use recursion.

What is meant here is that for processing text, attentions system processes the entire set of input, thereby attaining an infinite attention. In comparision to RNN's and LSTM's, where the input is processed sequentially, attentions processes it al-together. Attention creates an `attention matrix` - where each output is a weighted sum of inputs. Attention systems are able to map or capture relationships directly.

Attention system have another advantage - they can scale by parallelizing the process by use of GPU's. 