# BERT

#search-eng

## Core Idea

BERT means **Bidirectional Encoder Representations from Transformers**. Google researchers introduced it as a pretrained [[Encoder-Only Model (Transformers)|Transformer encoder]] whose token representations use left and right context. It is not simply two separate one-directional models joined together.

The original pretraining combines masked language modelling and next-sentence prediction. Fine-tuning adds task outputs for classification, sentiment analysis, token labelling, or extractive question answering. Extractive question answering selects an answer span; it is different from unrestricted text generation.

## Search Application

A query and document can be encoded together to score relevance, or an encoder can be trained to produce separately comparable [[Embeddings]]. The architecture alone does not establish a good retrieval distance. Preserve the checkpoint's [[Tokenization|tokenizer]], input format, truncation policy, and training objective.

## Exercise

Compare “river bank” with “bank account”. Explain why contextual token vectors can differ even when the word is the same. Then explain why averaging those vectors without retrieval training may still produce poor nearest neighbours. Continue with [[RoBERTa]] and [[Search Evaluation]].

## References & Useful Links

- [BERT paper](https://aclanthology.org/N19-1423.pdf) — Primary reference for the explanation above.
