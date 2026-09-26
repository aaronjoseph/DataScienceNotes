---
aliases: ["Cosine Similarity & Cosine DIstance"]
note_type: concept
search_stage: foundations
---

# Cosine Similarity

#search-eng

## Overview

Cosine similarity compares the directions of two nonzero vectors. It can compare [[TF-IDF]] vectors or [[Embeddings]], but the meaning of “similar” depends on how those vectors were constructed. [^1]

$$
\operatorname{cos}(a,b)=\frac{a\cdot b}{\|a\|_2\|b\|_2}.
$$

The numerator is the dot product:

$$
a\cdot b=\sum_i a_i b_i.
$$

$$
\|a\|_2=\sqrt{\sum_i a_i^2}
$$

Its mathematical range is $[-1,1]$; for nonnegative TF-IDF vectors it lies in $[0,1]$. The formula is undefined for a zero vector; check how your library handles that case. [^1]

## Worked Example

**Inputs:** $a=(1,1)$ and $b=(2,0)$.

**1. Calculate the dot product.**

$$
a^\top b=1\times2+1\times0=2
$$

**2. Calculate each norm.**

$$
\|a\|_2=\sqrt{1^2+1^2}=\sqrt2
$$

$$
\|b\|_2=\sqrt{2^2+0^2}=2
$$

**3. Divide by the product of the norms.**

$$
\operatorname{cos}(a,b)=\frac{2}{\sqrt2\times2}=\frac{1}{\sqrt2}\approx0.7071
$$

For $c=(2,2)$, similarity with $a$ is 1: the directions match even though the vectors are not identical.

## Cosine Distance

A common dissimilarity is $1-\operatorname{cos}(a,b)$, giving 0.2929 in the first example.

This is subtraction, not inverse proportionality.

Similarity 0 means orthogonality, not a universal statement that two documents have unrelated meanings.

## Search Considerations

For unit-normalised vectors, cosine similarity equals the dot product. With unnormalised vectors, norms affect dot-product ranking. Match the model's intended scoring method before indexing; a similarity score is not automatically a probability of relevance.

## Why Normalisation Changes the Comparison

Normalise each vector separately:

$$
\hat a=\frac{a}{\|a\|_2}
$$

$$
\hat b=\frac{b}{\|b\|_2}.
$$

Then cosine is simply $\hat a^\top\hat b$.

Multiplying either original vector by a positive constant does not change this value.

A raw dot product, in contrast, rewards both alignment and magnitude; whether magnitude is useful depends on the representation and training objective.

> [!example]- Derive the link with Euclidean distance
> For unit vectors,
>
> $$
> \|\hat a-\hat b\|_2^2=\|\hat a\|_2^2+\|\hat b\|_2^2-2\hat a^\top\hat b=2-2\cos(a,b).
> $$
>
> Therefore maximising cosine and minimising squared Euclidean distance give the same ordering over these normalised vectors. This equivalence does not hold for arbitrary unnormalised vectors.
>
> In the practice example, $a=(1,1)$ and $b=(100,100)$ have dot product 200 but cosine 1. The large magnitude changes the first score while preserving direction.

## Edge Cases and Thresholds

Specify a zero-vector policy before normalisation: reject it, use a fallback, or follow a documented library convention. Also check finite values and dimensions before comparing vectors. Numerically tiny deviations outside the mathematical range can occur through floating-point rounding; do not interpret them as stronger-than-perfect similarity.

The quantity $1-\cos(a,b)$ is a useful dissimilarity but does not generally satisfy the triangle inequality.

For directions at 0°, 45°, and 90°, the two adjacent distances sum to about 0.5858, smaller than the end-to-end distance 1.

An indexing method requiring a metric needs its own compatibility check.

## Practice

Compare $a$ with $(100,100)$ using dot product and cosine. Which score changes with magnitude?

## References & Useful Links

[^1]: [Scikit-learn cosine similarity](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.cosine_similarity.html) — Normalised dot product and implementation behaviour.
