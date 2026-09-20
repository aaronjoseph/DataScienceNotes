# Sampling

#search-eng

## Choose the Population and Unit

Sampling selects observations from a target population. A large sample can still be systematically biased. Define whether a search sample represents distinct queries, query requests, sessions, users, or documents; these answer different questions.

## Probability Designs

- **Simple random:** each population unit has equal selection probability in the basic design.
- **Systematic:** choose a random start and then every kth unit. Periodic ordering can distort representation.
- **Stratified:** sample within each stratum, such as language or query-frequency band. Allocation may be proportional or intentionally disproportionate; population estimates then need appropriate weights.
- **Cluster:** randomly select clusters, such as stores or users, and sample all or some units within them. Similarity within clusters affects uncertainty.

Stratification does not require equal group sizes. Convenience, voluntary-response, purposive, and snowball samples do not automatically support population-wide inference.

## Positional Split Example

```python
import pandas as pd
from sklearn.model_selection import StratifiedShuffleSplit
frame = pd.DataFrame({'value': range(20), 'label': [0]*12+[1]*8},
                     index=range(100, 120))
splitter = StratifiedShuffleSplit(n_splits=1, test_size=0.25, random_state=42)
train_pos, test_pos = next(splitter.split(frame[['value']], frame['label']))
train, test = frame.iloc[train_pos], frame.iloc[test_pos]
print(len(train), len(test))  # 15, 5
```

Splitters return positions, so use `.iloc`, not index-label lookup with `.loc`. Stratified sampling still does not account for repeated users or time.

## Search Exercise

Suppose 90% of requests are common queries and 10% are rare queries. If you label equal numbers from both strata, report either a deliberately balanced diagnostic or a correctly weighted traffic estimate. Do not silently call the balanced mean traffic performance. Hard negatives may aid training but are not a representative evaluation sample; see [[Judgement List]], [[Search Evaluation]], and [[Confidence Interval]].

## Existing Illustrations

![[Attachements/Pasted image 2.png]]

![[Pasted image 3.png]]

## References & Useful Links

- [Statistics Canada probability sampling](https://www150.statcan.gc.ca/n1/edu/power-pouvoir/ch13/prob/5214899-eng.htm) — Sampling designs.
- [StratifiedShuffleSplit](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.StratifiedShuffleSplit.html) — Stratified positional splits.
