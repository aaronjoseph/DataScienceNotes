# TF-IDF

#search-eng

## Overview

Term frequency–inverse document frequency weights a term using its occurrence in a document and its rarity across a collection. It extends [[Bag of Words]] counts; it is not itself a semantic understanding model. [^1]

## Formula and Conventions

One teaching convention is:

$$\operatorname{tfidf}(t,d)=\operatorname{tf}(t,d)\log\frac{N}{\operatorname{df}(t)}$$

Here $N$ is the document count and $\operatorname{df}(t)$ counts documents containing term $t$. Term frequency can be a raw count, a count divided by document length, or a sublinear transform. State which one is used. [^1][^3]

The original note used length-normalised frequency:

$$\operatorname{tf}(t,d)=\frac{\operatorname{count}(t,d)}{|d|}$$

Example: `boots` appears twice in a 10-token document and in 10 of 100 documents. With natural logarithms, its weight is $0.2\ln(10)\approx0.4605$. A term in all 100 documents has zero IDF under this particular formula.

Libraries can smooth IDF and normalise the final vector. Do not compare scores until these conventions match. [^2]

## Search Interpretation

Rare terms can be discriminative, but rarity is not proof of relevance: a typo or product code can also be rare. [[Cosine Similarity]] compares vector directions; [[BM25]] uses a different treatment of term frequency and document length.

## Practice

Recalculate the example using raw term counts. Explain why its score changes even though the document has not changed.

## References & Useful Links

[^1]: [Term frequency and weighting](https://nlp.stanford.edu/IR-book/html/htmledition/term-frequency-and-weighting-1.html) — Frequency-based term weights.
[^2]: [Scikit-learn text feature extraction](https://scikit-learn.org/stable/modules/feature_extraction.html#text-feature-extraction) — TF-IDF implementation conventions.

[^3]: [Inverse document frequency](https://nlp.stanford.edu/IR-book/html/htmledition/inverse-document-frequency-1.html) — Corpus rarity and the basic IDF formula.
