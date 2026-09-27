> [!note] Main note
> [[Tokenization]] is the fuller, reviewed note on this topic and lists `Tokenization - NLP` as an alias. This page keeps the original summary; see [[Tokenization#Subword Tokenizers for Transformers|subword tokenizers]] for how Transformer models split text.

Tokenization is a key first step in most text-processing pipelines.

Tokenization splits a phrase, sentence, paragraph, or entire document into smaller units, such as words, subwords, or characters. Each of these units is called a token. Tokenization usually comes before optional steps such as [[Stemming and Lemmatization]], because those operate on individual tokens.

Most deep-learning models for text, including [[Transformers]], [[RNN|RNNs]], and [[LSTM|LSTMs]], take sequences of token IDs as input.

Tokenization can be used to build a vocabulary, from which the $K$ most frequent tokens can be extracted.

> In the context of natural language processing tasks, tokenization involves breaking down a given text, such as 'My grandma makes the best apple pie,' into a sequence of individual units of meaning, referred to as tokens. This process enables the representation of the original text as a series of discrete elements that can be analyzed and manipulated by algorithms 

### Drawbacks of Tokenization

OOV (out of vocabulary) refers to new words encountered at test time that are not part of the vocabulary.

- A common workaround for word-level tokenizers is to keep the top $K$ most frequent words and replace rarer words in the training data with an unknown token (`UNK`). The model then learns one representation shared by all unknown words. This keeps the vocabulary small, but every unknown word looks the same to the model, so distinctions between them are lost.
- Subword tokenizers, such as the byte-pair encoding used by many Transformer models, largely avoid this problem by splitting rare words into known pieces.