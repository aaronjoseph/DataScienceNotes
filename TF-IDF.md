### Term Frequency - Inverse Document Frequency (TF-IDF)

Consider word-vectorizer for bag of words, the major issues with it is
- Words that are frequently occuring, will have high weightage (Need Normalization)

> TFIDF = TF * IDF

### Term Frequency 

TF - Term Frequency = Rep. of Words in Sentence / No of Words in sentence

### Inverse Term Frequency

IDF = $$log(\frac{NoofSentences}{No of Sentences Containing the word})$$


The key aspect of TF-IDF is
- Uncommon words in a document -> Higher tf-idf
- More common words in a document -> Almost zero tf-idf