Tokenization is a key and mandatory aspect of working with text data.

Tokenization is essentially splitting a phrase, sentence, paragraph or an entire text document into smaller units, such as individual words or terms. Each of these smaller units are called tokens. Tokenization is the first step for [[Stemming and Lemmatization]].

Most DL techniques such as transformers, RNN's & LSTM's use tokens as input.

Tokenization can be used to develop a vocabulary and then K frequently occuring words can be extracted. 

> In the context of natural language processing tasks, tokenization involves breaking down a given text, such as 'My grandma makes the best apple pie,' into a sequence of individual units of meaning, referred to as tokens. This process enables the representation of the original text as a series of discrete elements that can be analyzed and manipulated by algorithms 

### Drawbacks of Tokenization

OOV - Out of Vocabulary, refers to the new words which are encountered at testing and are not part of the vocabulary
- A small trick to rescue word tokenizers from OOV is to form vocabulary with the Top K Frequenct Words and replace the rare words in training data with unknown tokens (UNK). This will help the model to learn the representation of OOV words in terms of UNK tokens