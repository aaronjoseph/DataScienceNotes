---
aliases: ["Tokenization - NLP"]
---

# Tokenization

#search-eng

## Overview

Tokenization splits input into units used by later processing. Units may be words, characters, or subwords. A token is an occurrence; a vocabulary entry represents a token type. Search analysis must decide how punctuation, identifiers, whitespace, and language boundaries affect those units. [^1]

## Search Example

For `USB-C charger 65W`, compare these deliberately chosen policies:

- Preserve identifiers: `usb-c`, `charger`, `65w`.
- Split punctuation: `usb`, `c`, `charger`, `65w`.

Neither policy is universally best. Test whether each matches the catalogue's language and the user's intent. Store exact identifiers separately when exact matching is required. Lowercasing is normalisation, not the act of splitting itself.

## Vocabulary and Unknown Tokens

A word-level model with a fixed vocabulary may map unseen words to `UNK`. Keeping only frequent vocabulary entries reduces vocabulary size but does not recover the distinctions between unknown words. Subword approaches reduce this problem; use the tokenizer expected by the [[Embeddings|embedding model]]. [^2]

Index and query analysis must be compatible, though not necessarily identical. Test the full analysis output before diagnosing a ranking problem.

## Related Notes

- [[Inverted Index]] — Consumes analysed terms.
- [[N-Grams]] — Represents adjacent token sequences.
- [[Stemming and Lemmatization]] and [[Stopwords]] — Optional transformations, not mandatory steps for every search field.

## Practice

Write expected tokens for `C++`, `AB-123`, `size 9.5`, and a query in another language. Compare each with the terms actually indexed.

## References & Useful Links

[^1]: [Tokenization in information retrieval](https://nlp.stanford.edu/IR-book/html/htmledition/tokenization-1.html) — Token boundaries and language-dependent decisions.
[^2]: [Hugging Face: Tokenizers](https://huggingface.co/learn/llm-course/en/chapter2/4) — Word/subword tokenization, unknown tokens, and model-compatible preprocessing.
