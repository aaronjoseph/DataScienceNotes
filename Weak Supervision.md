---
note_type: concept
search_stage: evaluation
---

# Weak Supervision

#search-eng

## Overview

Weak supervision creates training signals from sources that are cheaper or more scalable than individually verified labels, but may be noisy, incomplete, or biased. Examples include rules, dictionaries, historical decisions, and other model outputs. It is useful when unlabeled examples are plentiful and experts can express repeatable heuristics.

Snorkel represents sources as labeling functions, models their outputs, and produces probabilistic training labels for a downstream model.[^snorkel] It does not make a heuristic true merely because the heuristic is encoded in a framework.

## Labeling Functions Can Abstain

For classes $\mathcal Y$, a labeling function is

$$
\lambda_j(x)\in\mathcal Y\cup\{\bot\},
$$

where $\bot$ means abstain.

With $N$ examples and $m$ functions, their outputs form an $N\times m$ label matrix.

Abstention preserves the difference between “this rule has no evidence” and “this example is negative”.

For a search relevance task, a strict identifier-equality rule might vote Exact only after required constraints have been checked. A known incompatible model number might vote Irrelevant. A loose token-overlap rule should be treated as weak evidence and may need to abstain on ambiguous matches.

### Why three votes need not be three independent opinions

Suppose rules A, B, and C all test the same brand field with slightly different string handling. All three vote Exact for a brand match, while rule D flags the wrong product type.

A simple majority chooses Exact, even though the first three votes share essentially one source of evidence. The disagreement should prompt a review of rule dependencies and the rubric. A brand match alone does not establish that the product fulfils the query.

## Combine Sources and Train a Model

Snorkel's original approach models source accuracies and dependencies from their agreement patterns, under statistical assumptions, then passes probabilistic labels to a discriminative model.[^snorkel] Inspect coverage, conflicts, and correlations rather than assuming every label source contributes independent information.

For binary soft label $\tilde y_i\in[0,1]$ and predicted probability $p_i$, one possible training loss is

$$
\ell_i=-\tilde y_i\log p_i-(1-\tilde y_i)\log(1-p_i).
$$

This preserves uncertainty in the target. It does not guarantee that the estimated soft label is calibrated or correct. The downstream model may generalise beyond rule coverage, but it may also reproduce systematic source mistakes.

## A Practical Search Workflow

Write a relevance rubric and a small independently judged development set first. Add interpretable labeling functions, inspect the examples each covers, and audit disagreements. Version functions and the label-combination method. Train on the weakly labeled pool and evaluate on a separately judged set that the rules were not repeatedly tuned against.

Keep labels derived from clicks distinguishable from editorial relevance. Also check whether a rule uses future events or information unavailable at serving time; weak labels and ranking features have different allowable data boundaries.

## Exercise

Write two rules that can abstain for `usb-c charger 65w`, then give a counterexample to each.

State which rule errors a label model could plausibly detect from disagreement and which shared errors would require human review.

## Search Connections

- [[Search Engineering]] — Learning map.
- [[Data Labeling]] and [[Judgement List]] — Label meaning and independent judgments.
- [[Search Evaluation]] — Measuring downstream quality.
- [[Click Bias]] and [[Data Leakage]] — Biased and unavailable signals.

## References & Useful Links

[^snorkel]: [Ratner et al., Snorkel: Rapid Training Data Creation with Weak Supervision, 2017](https://arxiv.org/html/1711.10160v1) — Labeling functions, probabilistic labels, source accuracies, dependencies, and downstream training.
