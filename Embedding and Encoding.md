---
aliases: ["Embedding vs. Encoding - Understanding the Difference"]
note_type: concept
search_stage: foundations
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

## What Information Does the Representation Preserve?

Consider a product with ID `P17`, colour `red`, title `red hiking boots`, and price 120. An integer code for the colour is a label: assigning red=1 and blue=2 does not establish that blue is twice red. A one-hot vector gives each category its own coordinate. A title count vector records lexical evidence, while a learned title embedding reflects the training objective.

These representations can coexist in one search system. Use IDs for equality and joins, typed numbers for price comparisons, lexical fields for exact words, and embeddings for learned similarity. Turning all fields into one text string does not guarantee that the resulting vector respects numeric or categorical constraints.

### Relate an embedding lookup to one-hot encoding

Define the inputs:

- $e_i\in\mathbb R^{|V|}$: a vector containing a single 1 at vocabulary position $i$.
- $W\in\mathbb R^{|V|\times d}$: a matrix of learned word vectors.

Their product is

$$
z_i=W^\top e_i\in\mathbb R^d.
$$

Multiplication selects row $i$ of $W$.

An implementation can look up that row directly without allocating the one-hot vector.

The ID-to-row mapping must be the same one used during training.

Two models can both output 384 numbers while using unrelated coordinate systems. Equal shape makes addition possible numerically; it does not make cross-model cosine similarity meaningful.

## Choose by the Question You Need to Answer

Ask whether the task needs equality, counting, ordering, similarity, or prediction. Then state the transformations and information they discard. Lowercasing can merge case distinctions; bag of words drops order; a fixed-length embedding compresses a variable-length text. Evaluate the resulting representation on actual queries, including cases where those discarded distinctions matter.

## Practice

For a catalogue item, separate its ID, colour category, title tokens, and title embedding. Explain which comparisons are meaningful for each field.

## Embedded Reference

![[Embeddings]]

## References & Useful Links

[^1]: [Mikolov et al.: Word representations](https://arxiv.org/abs/1301.3781) — Learned word-vector relationships and their experimental context.
