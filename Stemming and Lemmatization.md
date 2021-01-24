Stemming and Lemmatization are text normalization techniques in NLP, which is used to prepare text, words and documents for further processing.

Lemmatization takes more time than stemming

### Stemming

Stemming is the process of producing morphological variants of a root/base word. Stemming is a crude technique for cataloging related words, it essentially chops off letters from the end until the stem is reached.

Input | Stem-Word
--|--
History, Historical | Histori
Finally, Final, Finalized | Fina
Going, Goes, Gone | Go

#### Porter Stemmer

Porter stemmer is the most common and an effective stemming technique. The algorithm employs five phases of word reduction, each with its own set of mapping rules.

#### Snowball Stemmer

This offers slight improvements over the original Porter stemmer both in logic and speed. Also called as Porter2stemming algorithm. 

#### Lancaster Stemmer

This is the most aggressive stemming algorithm of the bunch.

---
### Lemmatization

> Lemma of a word is its dictionary or canonical form

In contrast to stemming, lemmatization looks beyond word reduction and considers a language's full vocabulary to apply a morphological analysis to words. Lemmatization is considered to be more informative than stemming. Lemmatization looks at surrounding text to determine a given word's part of speech, it doesn't categorize phrases.

Also, it is harder to form lemmatizer for a new language than it is in a stemming algorithm.