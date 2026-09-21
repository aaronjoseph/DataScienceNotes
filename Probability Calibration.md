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

$$\frac{(0.8-1)^2+(0.8-1)^2+(0.8-0)^2+(0.8-0)^2}{4}=0.34.$$

This one small group shows a discrepancy, not proof of population-wide miscalibration. Predictions of 0.5 would score 0.25 on these labels, yet constant scores provide no useful ordering.

## Search Exercise

A strictly increasing score mapping preserves ranking while changing probabilities. Explain why [[NDCG]] may stay fixed even when log loss improves. Then explain why changing training class weights or prevalence requires checking probability quality on representative traffic. Connect [[Imbalanced Classification]], [[Active Learning]], and [[Click Bias]].

## References & Useful Links

[^1]: [Scikit-learn calibration guide](https://scikit-learn.org/stable/modules/calibration.html) — Reliability, calibration methods, and data separation.
