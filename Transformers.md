### Links
- [Andrej Karapathy with Lex Fridman](https://www.youtube.com/watch?v=9uw3F6rndnA)
- [On building Transformers from Scratch](https://www.datacamp.com/tutorial/building-a-transformer-with-py-torch)
- [Formal Algorithms for Transformers - Paper (Deepmind)](https://arxiv.org/pdf/2207.09238)\
- [GPT-2 in Depth](http://jalammar.github.io/illustrated-gpt2/)
- [The Math behind Attention](https://www.youtube.com/watch?v=UPtG_38Oq8o)
- [Harvard NLP Annotated Transformers](https://nlp.seas.harvard.edu/2018/04/03/attention.html)

### Other papers 

![[Transformer Papers]]

---

Transformers are magnificent neural network architecture, since it's a general purpose differentiable computer.
* **Expressive**
	+ Can process sequential data with ease
	+ Allows for modeling of complex relationships between inputs and outputs
* **Optimizability**
	+ Via back-propagation and gradient descent
	+ Enables efficient training of large models
* **Efficiency**
	+ High parallelism compute graph enables fast processing of large datasets
	+ Scalable to large models and datasets

---

Transformers network comes with a architecture which is quite complex and is a form of [[Sequence Models|sequence model]]. This is used in [[Machine Translation]] and [[Language Model]] as well.

Paper - [PDF](https://arxiv.org/pdf/1706.03762.pdf)

### Uncovering the Architecture

![[Transformers-1.png]]



![[Transformers.png]]

>What is Input Embedding

When the Input Text comes in, the text is split into individual values, and each word get's assigned an input ID. After which it's assigned an embedding of vector size 512. It is referred as $d_{model}$ =512 in the paper

> Positional Encoding

Each word should carry some information regarding the position in the sentence. Model should be able to recognise the difference between words that are close and distant. Positional Encoding should offer a pattern that can be learned by the model. Positional encoding value is computed only once.

> Q,K,V 

In attention-based models, such as Transformers, three essential components are used to compute the output.These components are derived from database terminology and are commonly referred to as:

**• Q (Query)**: represents the query or question being asked. 
	The query is a representation of the current word used to score against all the other words (using their keys). We only care about the query of the token we’re currently processing.
**• K (Key)**: corresponds to the key or column in a table that is relevant to the query.
	Key vectors are like labels for all the words in the segment. They’re what we match against in our search for relevant words
**• V (Value)**: stands for value, which corresponds to the actual data values stored in the database.
	Value vectors are actual word representations, once we’ve scored how relevant each word is, these are the values we add up to represent the current word.

These components are used to compute attention scores and ultimately determine the importance of each input element with respect to the current query.

> Single Head Attention

Self Attention allows the model to relate words to each other. 
$$Attention(Q,K,V) = softmax(\frac{QK^T}{\sqrt{d_{k}}})V$$

Self-Attention is permutation invariant. Self-Attention requires no parameters. 


> Multi head Attention


$$Attention(Q,K,V) = softmax(\frac{QK^T}{\sqrt{d_{k}}})V$$
$$head_i = Attention(QW_{i}^{Q}, KW_{i}^{K}, VW_{i}^{V})$$


> Layer Normalization

[[Layer Normalization]]

---

> Self Attention vs Masked Self Attention

Traditional self-attention mechanisms enable a given token to attend to tokens to its right. In contrast, masked self-attention blocks impose an added constraint, preventing the current token from attending to any tokens that appear to its right.


![[Masked_SA&SA.png]]

---
### Key advantage of transformers

> Key advantage of transformers is that it doesn't use `recursion`.

- In text procession, attention system processes the entire set of input
	- This leads to infinite attention
	- Attention creates an `attention matrix` - where each output is a weighted sum of inputs. Attention systems are able to map or capture relationships directly.
- Attention system have another advantage - they can scale by parallelising the process by use of GPU's. 

### Challeges of RNN's and how transformers have an advantage

| Challenges of RNNs                     | Transformer Networks                                 |
| -------------------------------------- | ---------------------------------------------------- |
| Long range dependencies                | Facilitate long range dependencies                   |
| Gradient vanishing and explosion       | No gradient vanishing and explosion                  |
| Large # of training steps              | Fewer training steps                                 |
| Recurrence prevents parallel computing | No recurrence hence facilitates parallel computation |

One key thing to note here is, [[RNN]]'s have a lot of parameters, which makes training slow.

---

## Working of Attention Model

> Fundamentally, the attention model get rid of `recurrence`.

> The main reason this model works is reduction of path-length and computation steps `computation steps can cause the network to lose information`

### Attention                            

An attention function can be described as mapping a query `decoder - output` and a set of key-value pairs `encoder - input` to an output, where the query, keys, values, and output are all vectors. The output is computed as a weighted sum of the values, where the weight assigned to each value is computed by a compatibility function of the query with the corresponding key

### Scaled Dot-Product Attention

The input consists of queries and keys of dimension $dk$, and values of dimension $dv$. We compute the dot products of the query with all keys, divide each by $\sqrt{dk}$, and apply a softmax function to obtain the weights on the values. In practice, we compute the attention function on a set of queries simultaneously, packed together into a matrix $Q$. The keys and values are also packed together into matrices $K$ and $V$. We compute the matrix of outputs as:
$$\text{Attention}(Q, K, V) = \text{softmax}(\frac{QKT}{\sqrt{dk}})V$$
The two most commonly used attention functions are additive attention, and dot-product (multiplicative)
attention. Dot-product attention is identical to our algorithm, except for the scaling factor of
$\sqrt{\frac{1}{dk}}$. Additive attention computes the compatibility function using a feed-forward network
with a single hidden layer. While the two are similar in theoretical complexity, dot-product attention is much faster and more space-efficient in practice, since it can be implemented using highly optimized matrix multiplication code. While for small values of $dk$ the two mechanisms perform similarly, additive attention outperforms dot product attention without scaling for larger values of $dk$. We suspect that for large values of $dk$, the dot products grow large in magnitude, pushing the softmax function into regions where it has extremely small gradients. To counteract this effect, we scale the dot products by $\sqrt{\frac{1}{dk}}$.

### Different Transformer Architectures

- [[Encoder-Only Model (Transformers)]]
- [[Encoder-Decoder Model (Transformers)]]
- [[Decoder-Only Model (Transformers)]]


--- 

