---
note_type: concept
search_stage: evaluation
---

# Semi-Supervised Labeling

#search-eng

## Overview

Semi-supervised learning uses both labeled and unlabeled examples. Unlabeled data can help when its structure supplies useful information about the prediction task. It does not necessarily require human labels specifically: what matters is the labeled set's quality and meaning.

Two practical approaches are self-training and graph-based label propagation.[^semi] In search, both require care because relevance belongs to a query–item pair. Product similarity alone does not imply equal relevance for every query.

## Self-Training

Train an initial supervised classifier, predict labels for the unlabeled pool, accept a selected subset as pseudo-labels, and retrain.

For example, a confidence rule might accept $\hat y=\arg\max_c p_c(x)$ when $\max_c p_c(x)\ge\tau$.

The threshold $\tau$ is a selection policy, not a guarantee of label accuracy.

Confidence can be wrong under domain shift or poor [[Probability Calibration|calibration]].

Evaluate pseudo-label quality on an independent audit sample, and keep their provenance distinct from verified labels.[^semi]

## Label Propagation

Build a graph whose nodes are examples and whose edges express a chosen similarity. A simple teaching update for class-score vectors is

$$
F_i^{(t+1)}=\sum_j S_{ij}F_j^{(t)},\qquad \sum_jS_{ij}=1,
$$

where $S$ is a nonnegative row-normalised similarity matrix.

After each update, a hard-clamping method restores labeled nodes to their known labels.

This illustrates the averaging mechanism; library algorithms differ in normalisation and clamping.

Scikit-learn distinguishes `LabelPropagation` from regularised, softly clamped `LabelSpreading`.[^semi]

### Inspect one propagation step

An unlabeled node connects to a positive labeled node with weight 0.8 and a negative labeled node with weight 0.2.

One averaging step gives class scores `[0.8,0.2]` in positive/negative order.

Those numbers reflect the chosen graph.

If the strong edge joins a waterproof boot to a water-resistant trainer for a query requiring waterproofing, the graph can propagate the wrong label.

The graph is part of the model, not independent evidence that the prediction is correct.

## Assumptions and Failure Modes

The central assumption is that nearby or connected examples tend to share labels under the target task. Negation, compatibility, and hard constraints can break that assumption. A cluster of similar product descriptions can contain both relevant and irrelevant items for the same query.

Disconnected unlabeled regions may have no path to a reliable label. Wrong seed labels can contaminate their neighbourhoods. Self-training can repeatedly reinforce confident errors, especially for rare classes. Adding more unlabeled data can therefore hurt if the representation or task assumptions are wrong.

Distinguish transductive evaluation, where the unlabeled evaluation inputs participate in the graph, from inductive evaluation on genuinely new inputs. Disclose the setting and keep evaluation labels hidden. A graph built using test labels would invalidate the evaluation.

## Exercise

Construct a graph for four query–product pairs, including a hard-constraint mismatch.

Try a title-similarity edge and an edge that also respects the constraint.

Explain how the propagated labels differ and what held-out evidence would justify either graph.

## Search Connections

- [[Search Engineering]] — Learning map.
- [[Data Labeling]] and [[Judgement List]] — Verified seed labels and provenance.
- [[Search Evaluation]] — Evaluation boundaries.
- [[Active Learning]] — Asking an annotator for a label instead of inferring it.

## References & Useful Links

[^semi]: [Scikit-learn: Semi-supervised learning](https://scikit-learn.org/stable/modules/semi_supervised.html) — Self-training, calibration, similarity graphs, label propagation, and label spreading. Documentation checked 26 September 2026.
