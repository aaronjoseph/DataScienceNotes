Word2Vec is a framework for learning word vectors. This algorithm is capable of understanding the semantic similarity of words using cosine similarity.

Word2Vec is of two types
- CBOW - Continous Bag of Words
- Skip-Gram Model

In the CBOW model, the distributed representations of context are combined to predict the word in the middle. Wile in the skip-gram model, the distributed representation of the input word is used to predict the context.

- Skip Gram works well with a small amount of the training data, represents well even rare words or phrases
- CBOW - several times faster to train than the skip-gram, slightly better accuracy for the frequent words

### Skip-Gram Model Details

`Word Encoding` each word is encoded in a [[Encoding|one-hot encoding]] format, wherein for the position referencing to the word is coded as 1 and the rest is 0.

- In the training stage, the input is a one-hot vector
- There are no activation function in the next hidden layer
- The output layer is a [[Sigmoid and Softmax Functions| softmax]] classifier, which contrary to the word vector -one hot encoded, is a probability distribution

Here, the hidden layer plays an important role - serves the role of a lookup table.

### Continoues Bag of Words

This algorithm tries to predict the next set of words using the existing words.