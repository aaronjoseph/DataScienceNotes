# Cross Entropy Loss

#search-eng

## Definition

For target distribution q and predicted class distribution p:

$$H(q,p)=-\sum_{j=1}^{K}q_j\log p_j.$$

With a one-hot target in class c, this becomes $-\log p_c$. Classes can be words/tokens, image categories, or relevance labels. With natural logarithms, assigning probability 0.8 to the correct class gives loss about 0.2231; probability 0.2 gives about 1.6094.

## Binary, Multiclass, and Multilabel

- **Binary:** $-y\log p-(1-y)\log(1-p)$.
- **Multiclass:** one distribution across mutually exclusive classes, commonly produced by [[Softmax Function]].
- **Multilabel:** independent binary losses per label, typically using separate sigmoid outputs; labels do not have to sum to one.

Applications include classification, [[Logistic Regression]], token prediction, and recommendation framed as interaction classification. Some GAN discriminators use this loss, but not every GAN objective does. Speech systems may use token cross-entropy or different alignment objectives; the application name alone does not fix the loss.

## Implementation Pitfalls

PyTorch `CrossEntropyLoss` expects unnormalised logits, not softmax probabilities, and supports class-index or suitable probability targets. `BCEWithLogitsLoss` combines a sigmoid with binary cross-entropy for stability. Check shape, class axis, masks, weights, and reduction. Avoid applying softmax/sigmoid twice.

Differentiability and probability interpretation make these objectives useful, but they do not guarantee calibrated predictions or factual output.

## Exercise

A model improves token loss while search answers become less helpful. Explain why [[Language Model|language modelling]] performance and [[Search Evaluation|search quality]] can diverge.

## References & Useful Links

- [PyTorch CrossEntropyLoss](https://docs.pytorch.org/docs/2.8/generated/torch.nn.CrossEntropyLoss.html) — Primary reference for the explanation above.
- [PyTorch BCEWithLogitsLoss](https://docs.pytorch.org/docs/2.8/generated/torch.nn.BCEWithLogitsLoss.html) — Primary reference for the explanation above.
