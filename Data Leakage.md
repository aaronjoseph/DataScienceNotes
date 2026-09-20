# Data Leakage

#search-eng

## Overview

Data leakage occurs when model development uses information unavailable at the intended prediction time or lets evaluation information influence fitting and selection. It can make validation look unrealistically good, not merely improve training accuracy. [^1]

## Two Main Routes

- **Leaky predictors:** Future outcomes, target-derived fields, or identifiers that reveal information unavailable in real use.
- **Leaky validation:** Overlapping examples, preprocessing fitted before the split, or repeated tuning against the supposed test set.

High accuracy or strong correlation is a reason to investigate, not proof of leakage.

## Preserve the Original Scaling Example

If [[Feature Scaling|StandardScaler]] learns its mean and standard deviation from all rows before splitting, evaluation data influence the transformation. Fit imputers, scalers, and feature selection only on each training split; transform validation/test data with those fitted objects. Pipelines help enforce this within [[Cross Validation]]. [^1]

## Search-Specific Checks

Illustrative examples:

- A click feature for a request must not include clicks occurring after that request.
- Repeated query–document pairs across splits can exaggerate generalisation.
- A query-level split and a time-based split answer different deployment questions; choose intentionally.
- Do not repeatedly tune against the final [[Judgement List|evaluation judgment set]].

A pipeline cannot repair an invalid split or a feature whose definition already leaks the target.

## Practice

For every ranking feature, write its event time, availability time, and data source. Identify which values could actually have been obtained when the historical request arrived.

## References & Useful Links

[^1]: [Scikit-learn: Common pitfalls and data leakage](https://scikit-learn.org/stable/common_pitfalls.html#data-leakage) — Splits, preprocessing, and pipelines.
