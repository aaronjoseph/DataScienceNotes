---
aliases: ["Cosine Similarity & Cosine DIstance"]
---

# Cosine Similarity

#search-eng

## Overview

Cosine similarity compares the directions of two nonzero vectors. It can compare [[TF-IDF]] vectors or [[Embeddings]], but the meaning of “similar” depends on how those vectors were constructed. [^1]

$$\operatorname{cos}(a,b)=\frac{a\cdot b}{\|a\|_2\|b\|_2},\qquad a\cdot b=\sum_i a_i b_i$$

$$\|a\|_2=\sqrt{\sum_i a_i^2}$$

Its mathematical range is $[-1,1]$; for nonnegative TF-IDF vectors it lies in $[0,1]$. The formula is undefined for a zero vector; check how your library handles that case. [^1]

## Worked Example

For $a=(1,1)$ and $b=(2,0)$, the dot product is 2 and the norms are $\sqrt2$ and 2. Similarity is $1/\sqrt2\approx0.7071$.

For $c=(2,2)$, similarity with $a$ is 1: the directions match even though the vectors are not identical.

## Cosine Distance

A common dissimilarity is $1-\operatorname{cos}(a,b)$, giving 0.2929 in the first example. This is subtraction, not inverse proportionality. Similarity 0 means orthogonality, not a universal statement that two documents have unrelated meanings.

## Search Considerations

For unit-normalised vectors, cosine similarity equals the dot product. With unnormalised vectors, norms affect dot-product ranking. Match the model's intended scoring method before indexing; a similarity score is not automatically a probability of relevance.

## Practice

Compare $a$ with $(100,100)$ using dot product and cosine. Which score changes with magnitude?

## References & Useful Links

[^1]: [Scikit-learn cosine similarity](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.cosine_similarity.html) — Normalised dot product and implementation behaviour.
