---
aliases: ["Tokenization - NLP"]
note_type: concept
search_stage: query_understanding
---

# Tokenization

#search-eng

## Overview

Tokenization splits input into units used by later processing. Units may be words, characters, or subwords. A token is an occurrence; a vocabulary entry represents a token type. Search analysis must decide how punctuation, identifiers, whitespace, and language boundaries affect those units. [^1]

## Search Example

For `USB-C charger 65W`, compare these deliberately chosen policies:

- Preserve identifiers: `usb-c`, `charger`, `65w`.
- Split punctuation: `usb`, `c`, `charger`, `65w`.

Neither policy is universally best.

Test whether each matches the catalogue's language and the user's intent.

Store exact identifiers separately when exact matching is required.

Lowercasing is normalisation, not the act of splitting itself.

## Vocabulary and Unknown Tokens

A word-level model with a fixed vocabulary may map unseen words to `UNK`. Keeping only frequent vocabulary entries reduces vocabulary size but does not recover the distinctions between unknown words. Subword approaches reduce this problem; use the tokenizer expected by the [[Embeddings|embedding model]]. [^2]

Index and query analysis must be compatible, though not necessarily identical. Test the full analysis output before diagnosing a ranking problem.

## Design an Analysis Contract

Separate three decisions: where tokens begin and end, how their surface forms are normalised, and which tokens are retained. For a lexical field, write the expected index-time and query-time outputs together. For a model input, use the tokenizer and special-token conventions supplied with that model.[^1][^2]

An illustrative product can have an exact identifier field containing `AB-123`, a title field containing analysed words, and a numeric power field containing `65`. These fields support different operations: exact lookup, text retrieval, and numeric filtering. Splitting the title token `65W` does not by itself create a typed watts constraint.

### Trace a mismatch before adjusting ranking

Suppose the index stores `usb-c` as one token, while the query analyser emits `usb` and `c`. A simple exact-term match finds neither token in that indexed field. A synonym or multi-field strategy could deliberately bridge the representations; increasing the BM25 weight cannot create a missing term match.

For `size 9.5`, preserving the decimal matters if a later parser interprets sizes. For `C++`, removing punctuation can merge a programming language with an unrelated letter. For another writing system, whitespace may not identify word boundaries at all.

## Boundary Cases to Inspect

Check empty input, punctuation-only queries, case, accents, composed versus decomposed Unicode, and long text truncated by a model. Record both the original input and token output in a small diagnostic fixture. If the analysis pipeline changes, determine whether stored text or embeddings must be rebuilt; query-only changes cannot recover distinctions already erased at indexing time.

## Related Notes

- [[Inverted Index]] — Consumes analysed terms.
- [[N-Grams]] — Represents adjacent token sequences.
- [[Stemming and Lemmatization]] and [[Stopwords]] — Optional transformations, not mandatory steps for every search field.

## Practice

Write expected tokens for `C++`, `AB-123`, `size 9.5`, and a query in another language. Compare each with the terms actually indexed.

## References & Useful Links

[^1]: [Tokenization in information retrieval](https://nlp.stanford.edu/IR-book/html/htmledition/tokenization-1.html) — Token boundaries and language-dependent decisions.
[^2]: [Hugging Face: Tokenizers](https://huggingface.co/learn/llm-course/en/chapter2/4) — Word/subword tokenization, unknown tokens, and model-compatible preprocessing.
