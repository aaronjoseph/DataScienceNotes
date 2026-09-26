---
note_type: concept
search_stage: retrieval
---

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

## Work from Counts to a Query Score

Fix the vocabulary, TF transform, IDF formula, and vector normalisation first. Compute each document's weighted vector using the same vocabulary and corpus statistics; encode the query compatibly, then use a stated scoring function such as [[Cosine Similarity]]. TF-IDF supplies weights, while the similarity function turns two vectors into a score.

> [!example]- Compare a repeated rare term with a common term
> Take $N=100$ and raw-count TF. `boots` occurs in 10 documents and twice in D1, so its weight is $2\ln10\approx4.6052$. `red` occurs in 50 documents and once in D1, so its weight is $\ln2\approx0.6931$.
>
> These are coordinates of D1's vector, not final relevance probabilities. If the query contains only `red`, the boots coordinate contributes nothing to a raw dot product but contributes to the document norm in cosine scoring. This is why normalising the final vector changes retrieval behaviour.

## Implementation Differences That Change Scores

For scikit-learn's default smoothed IDF, the documented expression is

$$\operatorname{idf}(t)=\ln\frac{1+N}{1+\operatorname{df}(t)}+1.$$

It uses raw counts by default and applies L2 normalisation to each final vector.[^2] Under this IDF, a term present in every document has weight 1 before multiplication by TF, rather than zero. Write the convention next to an example; otherwise two correct calculations can appear inconsistent.

An absent vocabulary term needs an explicit handling rule. The unsmoothed formula is undefined at $df=0$, but most fixed-vocabulary vectorizers simply do not create a coordinate for an unseen term. Inspect this boundary when a query becomes an all-zero vector.

## Practice

Recalculate the example using raw term counts. Explain why its score changes even though the document has not changed.

## References & Useful Links

[^1]: [Term frequency and weighting](https://nlp.stanford.edu/IR-book/html/htmledition/term-frequency-and-weighting-1.html) — Frequency-based term weights.
[^2]: [Scikit-learn text feature extraction](https://scikit-learn.org/stable/modules/feature_extraction.html#text-feature-extraction) — TF-IDF implementation conventions.

[^3]: [Inverse document frequency](https://nlp.stanford.edu/IR-book/html/htmledition/inverse-document-frequency-1.html) — Corpus rarity and the basic IDF formula.
