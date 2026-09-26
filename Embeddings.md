---
note_type: concept
search_stage: retrieval
---

# Embeddings

#search-eng

## Overview

An embedding represents an item as a learned vector. Search can encode a query and document into a compatible vector space and retrieve nearby documents. The training objective determines which relationships the representation captures. [^1]

## Word, Sentence, and Document Representations

[[Word2Vec]] learns word representations. A sentence encoder represents a larger text unit. Do not assume that averaging arbitrary word vectors or pooling an unfine-tuned [[BERT]] model produces a good search model.

In asymmetric search, a short question may retrieve a longer passage. Use the model's intended query/document encoding paths, prompts, and similarity function. Precomputed document vectors must remain compatible with the query encoder. [^1]

## Illustrative Search Example

`footwear for rainy trails` and `waterproof hiking boots` share little exact wording but may be close under a suitable retrieval model.

Conversely, a related item can still violate `size 9` or an exact brand constraint.

Test semantic retrieval against a [[Judgement List]] rather than treating similarity as correctness.

## Practical Checklist

Record model/version, tokenizer, input fields, truncation, vector dimensions, normalisation, and scoring convention. Changing an encoder can require re-encoding the corpus; equal dimensions alone do not establish compatibility.

## Related Notes

- [[Embedding and Encoding]] — Representation vocabulary.
- [[Cosine Similarity]] — One scoring option.
- [[Search Ranking|Ranking]] — Retrieval versus joint query-document scoring.
- [[BM25]] — Lexical baseline for comparison.

## Separate the Representation from the Index

Let $f_Q(q)\in\mathbb R^d$ and $f_D(x)\in\mathbb R^d$ encode a query and document.

A scoring function $s(f_Q(q),f_D(x))$ defines their ordering.

The vector index accelerates that scoring problem; it does not decide what the learned geometry ought to mean.

For a deployment change, therefore ask two questions. Do the vectors retrieve judged useful items when searched exactly? Does the approximate index recover those exact neighbours? The first concerns representation quality; the second concerns [[Approximate Nearest Neighbours|approximation]]. A perfect ANN index cannot repair a model that ranks the wrong meaning highly.

### Estimate storage before index overhead

For $N$ items with $d$ float32 coordinates, each coordinate takes 4 bytes.

**Raw vector storage:**

$$
\text{bytes}=4Nd
$$

**Example inputs:** one million vectors, each with 768 coordinates.

$$
4\times1{,}000{,}000\times768=3.072\times10^9\text{ bytes}
$$

That is **3.072 GB** in decimal units, before index overhead.

This excludes IDs, graph links, metadata, replicas, and temporary build memory. Quantisation can reduce storage but changes the accuracy and cost tradeoff. Doubling the number of chunks approximately doubles the raw vector storage if dimension and precision are fixed.

## Decide the Retrieval Unit

A long document can be represented as one item or several passages. Small passages can expose a precise answer but lose surrounding context; large passages can mix topics or exceed the encoder's input limit. These are design tradeoffs to evaluate, not a universal chunk-size rule. Preserve document and passage IDs so retrieval, deduplication, judgments, and final presentation use compatible units.

Start with a few manually checked queries. Inspect the encoded fields, truncation boundary, nearest neighbours, and hard-constraint violations before scaling to a full benchmark.

## Practice

Compare lexical and embedding results for an exact identifier, a synonym query, and a query with a hard constraint. Label their failures separately.

## Further Study

- [[Approximate Nearest Neighbours]] — Index vectors and measure approximation separately from relevance.

## References & Useful Links

[^1]: [Sentence Transformers semantic search](https://www.sbert.net/examples/sentence_transformer/applications/semantic-search/README.html) — Symmetric/asymmetric retrieval and query/document encoding.
