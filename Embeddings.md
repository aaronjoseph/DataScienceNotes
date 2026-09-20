# Embeddings

#search-eng

## Overview

An embedding represents an item as a learned vector. Search can encode a query and document into a compatible vector space and retrieve nearby documents. The training objective determines which relationships the representation captures. [^1]

## Word, Sentence, and Document Representations

[[Word2Vec]] learns word representations. A sentence encoder represents a larger text unit. Do not assume that averaging arbitrary word vectors or pooling an unfine-tuned [[BERT]] model produces a good search model.

In asymmetric search, a short question may retrieve a longer passage. Use the model's intended query/document encoding paths, prompts, and similarity function. Precomputed document vectors must remain compatible with the query encoder. [^1]

## Illustrative Search Example

`footwear for rainy trails` and `waterproof hiking boots` share little exact wording but may be close under a suitable retrieval model. Conversely, a related item can still violate `size 9` or an exact brand constraint. Test semantic retrieval against a [[Judgement List]] rather than treating similarity as correctness.

## Practical Checklist

Record model/version, tokenizer, input fields, truncation, vector dimensions, normalisation, and scoring convention. Changing an encoder can require re-encoding the corpus; equal dimensions alone do not establish compatibility.

## Related Notes

- [[Embedding and Encoding]] — Representation vocabulary.
- [[Cosine Similarity]] — One scoring option.
- [[Search Ranking|Ranking]] — Retrieval versus joint query-document scoring.
- [[BM25]] — Lexical baseline for comparison.

## Practice

Compare lexical and embedding results for an exact identifier, a synonym query, and a query with a hard constraint. Label their failures separately.

## Further Study

- [[Approximate Nearest Neighbours]] — Index vectors and measure approximation separately from relevance.

## References & Useful Links

[^1]: [Sentence Transformers semantic search](https://www.sbert.net/examples/sentence_transformer/applications/semantic-search/README.html) — Symmetric/asymmetric retrieval and query/document encoding.
