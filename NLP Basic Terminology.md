# NLP Basic Terminology

#search-eng

## Core Vocabulary

- **Corpus:** A collection of documents.
- **Token:** One occurrence produced by [[Tokenization]].
- **Vocabulary:** The distinct token types or indexed terms represented by the system.
- **Term frequency (TF):** Occurrences of a term within a document, or a stated transform of that count.
- **Document frequency (DF):** Number of documents containing a term.
- **Inverse document frequency (IDF):** A weight based on document rarity, not DF itself. A basic form is $\log(N/df(t))$ for a term present in a corpus of $N$ documents. [^1]

[[TF-IDF]] multiplies a TF weight by an IDF weight; it does not add them.

## Representation Vocabulary

[[Bag of Words]] uses vocabulary dimensions and ignores ordering. [[N-Grams]] represents adjacent units. [[Embeddings]] uses learned vectors, while [[Cosine Similarity]] is a way to compare vectors rather than a representation itself.

## Practice

In documents `red red boots` and `red shoes`, `red` has collection frequency 3 and document frequency 2. Its raw term frequency in the first document is 2. Explain why these counts answer different questions.

## References & Useful Links

[^1]: [Inverse document frequency](https://nlp.stanford.edu/IR-book/html/htmledition/inverse-document-frequency-1.html) — DF, rarity, and IDF weighting.
