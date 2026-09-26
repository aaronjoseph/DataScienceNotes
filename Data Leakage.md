---
note_type: concept
search_stage: foundations
---

# Data Leakage

#search-eng

## Overview

Data leakage occurs when model development uses information unavailable at the intended prediction time or lets evaluation information influence fitting and selection. It can make validation look unrealistically good, not merely improve training accuracy. [^1]

## Two Main Routes

- **Leaky predictors:** Future outcomes, target-derived fields, or identifiers that reveal information unavailable in real use.
- **Leaky validation:** Overlapping examples, preprocessing fitted before the split, or repeated tuning against the supposed test set.

High accuracy or strong correlation is a reason to investigate, not proof of leakage.

## Preserve the Original Scaling Example

If [[Feature Scaling|StandardScaler]] learns its mean and standard deviation from all rows before splitting, evaluation data influence the transformation.

Fit imputers, scalers, and feature selection only on each training split; transform validation/test data with those fitted objects.

Pipelines help enforce this within [[Cross Validation]]. [^1]

## Search-Specific Checks

Illustrative examples:

- A click feature for a request must not include clicks occurring after that request.
- Repeated query–document pairs across splits can exaggerate generalisation.
- A query-level split and a time-based split answer different deployment questions; choose intentionally.
- Do not repeatedly tune against the final [[Judgement List|evaluation judgment set]].

A pipeline cannot repair an invalid split or a feature whose definition already leaks the target.

## Two Clocks for Every Feature

**Event time** says when something happened. **Availability time** says when the serving system could read it.

Both matter when reconstructing a historical request.

For a request at time $t_q$, a permissible historical feature can be written as

$$
x(q,t_q)=f\left(\{e:\ t_{\mathrm{event}}(e)<t_q,\ t_{\mathrm{available}}(e)\le t_q\}\right).
$$

The inequality convention depends on the feature contract; the essential rule is that the replay must use only information actually available then. Versioned snapshots or joins that select the most recent available record at the request time help enforce that rule.

### An old event can still leak

A search arrives at 10:00. A purchase happened at 09:55, but the ingestion pipeline publishes it at 10:05. A retrospective join using only purchase time includes it; the live ranker could not. Exclude it from the 10:00 feature reconstruction.

A click at 10:01 may be a legitimate **label** for the 10:00 search if the label window is defined accordingly. It cannot also be a historical click-count **feature** for that same search. Separate the feature cutoff from the outcome observation window.

## Audit the Entire Fitting Procedure

Split raw examples before learning vocabulary, imputation values, scaling parameters, feature selection, or calibration. Refit those operations inside each training fold. A fixed externally specified transformation differs from a transformation whose parameters were estimated from the evaluation data.[^1]

For [[Learning to Rank]], inspect query groups, duplicate products, temporal overlap, and target-derived aggregates as well as the final model. Document which overlap is allowed by the intended prediction task; overlap is a design question, not automatically a defect in every setting.

## Practice

For every ranking feature, write its event time, availability time, and data source. Identify which values could actually have been obtained when the historical request arrived.

## References & Useful Links

[^1]: [Scikit-learn: Common pitfalls and data leakage](https://scikit-learn.org/stable/common_pitfalls.html#data-leakage) — Splits, preprocessing, and pipelines.
