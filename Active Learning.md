---
note_type: concept
search_stage: evaluation
---

# Active Learning

#search-eng

## Overview

Active learning chooses which unlabeled examples should be sent to an annotator next. The goal is to improve a model using a limited labeling budget. In pool-based learning, the learner selects from an existing unlabeled pool, receives labels, retrains, and repeats.[^survey]

For search, a useful example might be a query–product pair where two rankers disagree or an ESCI classifier is uncertain. Selection efficiency and evaluation representativeness are different goals: a deliberately difficult annotation batch is not automatically a representative test set.

## Active Learning Sampling techniques

| Strategy | Selection signal | Limitation |
|---|---|---|
| Margin sampling | Small gap between the two highest class probabilities | Can repeatedly select noisy or ambiguous cases |
| Entropy sampling | Uncertainty across the whole predicted distribution | Depends on the usefulness of model uncertainty |
| Query by committee | Disagreement among multiple models | Models can share the same blind spots |
| Cluster or diversity sampling | Coverage of different regions of the input space | Geometric diversity may not match task diversity |
| Region-based allocation | Reserve budget across chosen regions or slices | Requires a meaningful partition and allocation rule |

The first three are common model-based query strategies; diversity and region allocation can complement them.[^survey] Uncertainty sampling does not guarantee that rare classes will be found, especially if the model is confidently wrong about them.

## Make Uncertainty Concrete

For predicted probabilities $p_{(1)}(x)\ge p_{(2)}(x)$, margin sampling selects small values of

$$
m(x)=p_{(1)}(x)-p_{(2)}(x).
$$

Entropy sampling selects large values of

$$
H(x)=-\sum_c p_c(x)\log p_c(x),
$$

using $0\log0=0$. These quantify model uncertainty, not the guaranteed improvement from buying a label.

### Choose between two annotation candidates

Candidate A has class probabilities `[0.45,0.44,0.11]`; B has `[0.55,0.25,0.20]`. Their margins are 0.01 and 0.30, so margin sampling prefers A.

Before spending the budget, inspect whether A is an unreadable or inherently ambiguous example. Ten near-duplicate versions of A may add less information than a batch covering several distinct query types. A diversity constraint or a small random-sampling component can help explore outside the current boundary.

## A Search Annotation Loop

Start with a seed set covering important intents, train a baseline, and reserve a separate evaluation set. For each round, select a batch under a stated budget, annotate it with the current rubric, inspect disagreement, and retrain. Record the acquisition strategy and selection scores so later analysis can explain the resulting training distribution.

Compare against random selection with the same initial data, labeling effort, and evaluation protocol. Track quality versus annotation cost or time, not only versus number of examples; a difficult multi-attribute query may take much longer to label than an obvious irrelevant pair.

## Limitations and Exercise

An actively selected pool overrepresents the selection rule's preferred cases.

Avoid using its unweighted accuracy as an estimate of traffic-wide accuracy.

Protect the test set from repeated selection and tuning.

With a budget of 100 judgments, propose a batch mixing uncertain pairs, diverse intents, and an exploration sample.

Explain what you would measure to decide whether the next round is worth its annotation cost.

## Search Connections

- [[Search Engineering]] — Learning map.
- [[Data Labeling]] and [[Judgement List]] — Annotation contract and provenance.
- [[Search Evaluation]] — Independent assessment.
- [[Probability Calibration]] — Interpreting predicted confidence.

## References & Useful Links

[^survey]: [Burr Settles, Active Learning Literature Survey](https://burrsettles.com/pub/settles.activelearning.pdf) — Pool-based learning, uncertainty sampling, query by committee, diversity, and practical issues.
