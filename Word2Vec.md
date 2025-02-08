To understand skipgram and CBOW better - https://jalammar.github.io/illustrated-word2vec/

Word2Vec is a framework for learning word embeddings. This algorithm is capable of understanding the semantic similarity of words using cosine similarity.

Word2Vec has two different models
- CBOW - Continuous Bag of Words
- Skip-Gram Model

In the CBOW model, the distributed representations of context are combined to predict the word in the middle. Wile in the skip-gram model, the distributed representation of the input word is used to predict the context.

- Skip Gram works well with a small amount of the training data, represents well even rare words or phrases
- CBOW - several times faster to train than the skip-gram, slightly better accuracy for the frequent words

### **Skip-Gram Model Overview**

The **Skip-Gram model** in **Word2Vec** is designed to predict surrounding context words given a target word. It operates as follows:

- **Word Encoding**: Each word is represented using **one-hot encoding**, where only one position in the vector is set to `1` and the rest are zeros.
    
- **Training Process**:
    
    - The input is a **one-hot vector** representing the target word.
    - The **hidden layer** acts as a lookup table that learns the dense vector (word embedding) for the word, without any activation functions applied.
    - The **output layer** uses a **softmax function**, converting raw scores into a **probability distribution** over all possible context words in the vocabulary.

#### **How It Works**:

1. **Target Word**: Given a target word, the model predicts words in its surrounding context.
2. **Context Window**: The number of words before and after the target word (defined by the context window) are predicted.

For example, in the sentence "The cat sat on the mat" with a context window size of 2, if "cat" is the target word, the model will predict the context words: "The", "sat", "on", and "the".
### **Summary**:

- **Skip-Gram** predicts the surrounding words (context) given a target word.
- Input is **one-hot encoded**, and output is a **probability distribution** across the vocabulary.
- The hidden layer learns dense vector embeddings, enabling the model to capture the relationships between words.

### Continuous Bag of Words (CBOW)

- **CBOW** is one of the models in Word2Vec used to predict a word given its context (neighboring words).
- It works by taking the surrounding words (context words) of a target word and using them to predict the target word itself.

**Example**: In the sentence "The cat sat on the mat", if "cat" is the target word, CBOW tries to predict "cat" from its context words "The", "sat", "on", "the", and "mat".

**How it works**:

- The context words are transformed into a vector representation (such as through one-hot encoding).
- These vectors are averaged or summed together and then passed through a neural network.
- The network predicts the target word.

**Characteristics**:

- CBOW is useful when context matters more than the individual words.
- It learns relationships between context words to predict the target word.


### **Difference Between Skip-Gram and CBOW**

- **CBOW**:
    - Predicts the **target word** based on the context (surrounding words).
    - Better at learning **syntactic relationships** (e.g., word order, grammar).
    - Faster to train because it sums over the context words and averages the resulting vectors.
- **Skip-Gram**:
    - Predicts **context words** given a target word.
    - Better at capturing **semantic relationships** (meaning and analogy tasks).
    - Computationally slower compared to CBOW because it needs to predict multiple words (all words in the context window) for each target word.

### Why is CBOW faster to train than Skip-Gram?

- **CBOW** averages the context word vectors and predicts a single word, making it computationally lighter.
- **Skip-Gram**, on the other hand, has to predict multiple context words for each target word, which increases the number of calculations required.