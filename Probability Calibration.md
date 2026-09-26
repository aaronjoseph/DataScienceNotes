---
note_type: concept
search_stage: evaluation
---

# Probability Calibration

#search-eng

## Core Idea

A calibrated binary predictor's probability estimates match observed event frequencies: among predictions near 0.8, about 80% should be positive in the evaluated population. This is different from ranking positives ahead of negatives. A model can rank well while being overconfident.[^1]

A [[Softmax Function|softmax]] or sigmoid output is not automatically calibrated. Identify the event: relevance, click, and purchase are different targets. Calibration for clicks under one exposure policy does not make a score a probability of editorial relevance.

## Assess and Fit

Reliability diagrams compare average predicted probability with positive frequency in bins. Report bin counts and slices; small bins are noisy. Brier score and log loss assess probability predictions but also reflect factors beyond calibration alone.

Sigmoid and isotonic calibration learn mappings from model scores using suitable held-out or cross-validated predictions. Fitting the calibrator on the model's own training predictions can give optimistic results. Isotonic calibration is flexible but can overfit small datasets.[^1]

## Worked Example

Four items all receive probability 0.8, but labels are `[1,1,0,0]`. Their observed positive fraction is 0.5 and mean binary Brier score is:

$$
\frac{(0.8-1)^2+(0.8-1)^2+(0.8-0)^2+(0.8-0)^2}{4}=0.34.
$$

This one small group shows a discrepancy, not proof of population-wide miscalibration.

Predictions of 0.5 would score 0.25 on these labels, yet constant scores provide no useful ordering.

## Define the Probability Target

For a binary event $Y\in\{0,1\}$ and score $\hat p$, ideal calibration means

$$
P(Y=1\mid\hat p=p)=p.
$$

In finite data, bins approximate this relationship. Report how bins are chosen and how many observations they contain. A reliability curve averaged over all traffic can hide different behaviour for identifiers, rare queries, or new products.[^1]

The mean binary Brier score is

$$
\frac{1}{N}\sum_i(\hat p_i-y_i)^2.
$$

It rewards useful probability predictions, but its value also depends on discrimination and the outcome distribution, so it is not a pure calibration measure.

### Improve probability quality without changing the order

**Inputs:** two items have scores 0.9 and 0.8, with labels 1 and 0 respectively.

**1. Calculate the original Brier score.**

$$
\frac{(0.9-1)^2+(0.8-0)^2}{2}=\frac{0.01+0.64}{2}=0.325
$$

**2. Apply a strictly increasing mapping.**

The new scores are 0.7 and 0.6, so the item order is preserved.

**3. Recalculate the Brier score.**

$$
\frac{(0.7-1)^2+(0.6-0)^2}{2}=\frac{0.09+0.36}{2}=0.225
$$

NDCG on these two items is unchanged. This small calculation demonstrates the distinction; it is not enough data to fit or validate a calibrator.

## Keep Fitting and Assessment Separate

Fit the predictive model on training data, fit the calibration mapping on appropriate out-of-sample predictions, and assess both on untouched evaluation data. Cross-validation can create out-of-fold predictions, but it must preserve query groups or time boundaries where required. Isotonic mappings can create ties even when the original ranking had none.

Recheck after changes to the candidate generator, label prevalence, model, or exposure policy. A probability estimated among retrieved candidates describes that selected population; it should not automatically be interpreted for the entire catalogue.

## Search Exercise

A strictly increasing score mapping preserves ranking while changing probabilities.

Explain why [[NDCG]] may stay fixed even when log loss improves.

Then explain why changing training class weights or prevalence requires checking probability quality on representative traffic.

Connect [[Imbalanced Classification]], [[Active Learning]], and [[Click Bias]].

## References & Useful Links

[^1]: [Scikit-learn calibration guide](https://scikit-learn.org/stable/modules/calibration.html) — Reliability, calibration methods, and data separation.
