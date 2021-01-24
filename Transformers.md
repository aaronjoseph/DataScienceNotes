Transformers network comes with a architecture which is quite complex and is a form of [[Sequence Models|sequence model]].

### Key advantage of transformers

> Key advantage of transformers is that it doesn't use recursion.

What is meant here is that for processing text, attentions system processes the entire set of input, thereby attaining an infinite attention. In comparision to RNN's and LSTM's, where the input is processed sequentially, attentions processes it all together. Attention creates an `attention matrix` - where each output is a weighted sum of inputs. Attention systems are able to map or capture relationships directly.

Attention system have another advantage - they can scale by parallelizing the process by use of GPU's. 

### Challeges of RNN's and how transformers have an advantage

Challenges of RNNs | Transformer Networks
------- | ------------
Long range dependencies | Facilitate long range dependencies
Gradient vanishing and explosion | No gradient vanishing and explosion
Large # of training steps | Fewer training steps
Recurrence prevents parallel computing | No recurrence hence facilitates parallel computation

One key thing to note here is, RNN's have a lot of parameters, which makes training slow.

### Attention Mechanism

Mimics the retrival of a value $v_i$ for a query q based ona key $k_i$ in database