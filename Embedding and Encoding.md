---
aliases: ["Embedding vs. Encoding - Understanding the Difference"]
---

# Embedding and Encoding

#search-eng

## Overview

Encoding is the broader act of representing information in another form. In machine learning, it often means turning categories or text into numerical inputs. An embedding is a vector representation, commonly learned so that useful relationships are reflected in its geometry.

## Compare the Representations

- [[Encoding]] covers categorical representations.
- [[Bag of Words]] represents token counts.
- [[TF-IDF]] weights counts using corpus statistics.
- [[Embeddings]] represents words, queries, or documents using a learned model.

These are different choices, not a universal progression from bad to good. In search, exact terms and identifiers can remain important even when a semantic model is available.

## Avoid Overinterpreting Geometry

The familiar word-vector analogy `king - man + woman ≈ queen` illustrates a relationship observed with some learned vectors. It is not an algebraic law that every embedding model must satisfy. [^1]

A compact vector can encode useful information, but a small number of dimensions alone does not prove semantic quality. Judge the representation against the intended task using [[Search Evaluation]].

## Practice

For a catalogue item, separate its ID, colour category, title tokens, and title embedding. Explain which comparisons are meaningful for each field.

## Embedded Reference

![[Embeddings]]

## References & Useful Links

[^1]: [Mikolov et al.: Word representations](https://arxiv.org/abs/1301.3781) — Learned word-vector relationships and their experimental context.
