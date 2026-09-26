---
note_type: concept
search_stage: ranking
---

# Learning to Rank

#search-eng

## Core Idea

Learning to rank trains a scoring or ordering model for documents **within a query context**. Typical data contains a query ID, candidate document, query–document features, and a relevance grade. Candidate generation remains a separate constraint: the model cannot rank an item it never receives (see [[Candidate Generation]]).

## Objective Families

| Family | Training comparison | Example intuition |
|---|---|---|
| Pointwise | Individual query–document label | Predict a relevance grade or probability |
| Pairwise | Two documents for the same query | Prefer a more relevant document over a less relevant one |
| Listwise / metric-aware | A query's candidate list or ranking-sensitive changes | Emphasise errors affecting the evaluated ordering |

For grades A=3, B=1, C=0 under one query, pair preferences include A>B, A>C, and B>C. Do not construct a preference between documents from unrelated queries solely by comparing their grades.

NDCG is not directly differentiable through discrete sorting. LambdaMART-style approaches use ranking-sensitive gradient constructions; an objective name does not mean ordinary gradient descent through the final NDCG calculation.

## Training Contract

1. Fix label meaning, feature availability time, and query grouping.
2. Split by the intended generalisation target: queries, users, or time.
3. Fit transformations within training data and preserve group boundaries.
4. Select on held-out query metrics; test once on a separate set.
5. Evaluate the serving pipeline's actual candidate distribution and feature freshness.

[[Light GBM]] supplies contiguous group sizes; [[XGBoost]] supports aligned sorted `qid` values. Check the library's objective and label requirements. Click labels need [[Click Bias|bias analysis]].

## Engagement Features

Product-search rankers often use behavioural counts as features: clicks, product-page views, add-to-cart events, and orders, for a query–item pair or an item alone, over several windows such as 1, 3, 7, and 30 days.

- **Key them precisely.** Query–item features need the same query normalisation at training and serving time, for example lowercase and trim followed by a hash. Restrict lookups to the recalled candidates to bound cost.
- **Measure coverage.** Record how many candidates had features for each query. If 30 of 120 candidates have query–item metrics, coverage is 25%, and the model is mostly scoring on other features for that query.
- **Distinguish missing from zero.** XGBoost treats missing values (by default `NaN`) as missing and learns a default branch direction for them; 0 is an ordinary value.[^1] Filling unavailable features with 0 at serving time when training used `NaN`, or the reverse, changes predictions. Use one convention everywhere.
- **Respect time.** Each window must end before the label's event time, or the feature leaks the label; see [[Data Leakage]].
- **Expect feedback loops.** Engagement reflects past ranking and exposure. Highly ranked items gather more clicks and stay highly ranked; see [[Click Bias]]. New items and new queries have no history.
- **Degrade deliberately.** If the feature store is unavailable, choosing neutral values and continuing is a product decision. Log it, because the ranker then behaves differently.

For online comparison of two rankers, [[Interleaving]] is often more sensitive than an [[AB Testing|A/B test]]; confirm important launches with an A/B test.

## A Pairwise Loss Makes the Preference Concrete

For documents $d_i$ and $d_j$ under the same query, with $d_i$ preferred, write their scores as $s_i$ and $s_j$. A pairwise logistic loss is

$$
\ell_{ij}=\log(1+\exp(-(s_i-s_j))).
$$

Compare three score margins under the same loss:

**Tied scores:** $s_i-s_j=0$.

$$
L=\ln(1+e^0)=\ln2\approx0.6931
$$

**Correct ordering:** $s_i-s_j=2$.

$$
L=\ln(1+e^{-2})\approx0.1269
$$

**Reversed ordering:** $s_i-s_j=-2$.

$$
L=\ln(1+e^2)\approx2.1269
$$

The loss encourages a useful ordering rather than a particular absolute score.

Metric-aware methods weight or construct updates using the importance of ranking changes.[^pairwise]

### Build the training unit correctly

For Q1, grades A=3, B=1, C=0 yield three strict preferences. For Q2, D=3 and E=3 yield no strict grade preference between D and E. Do not manufacture an A>D preference from row order: they belong to different queries and their grades are equal anyway.

A train/validation split by query keeps these comparison groups intact. A time split asks a different question and requires features reconstructed as they were available at each request time.

## Check the Serving Feature Contract

A ranker trained with missing engagement values can respond differently to a real count of zero. Log feature coverage and the missing-value convention. An item with no impressions, an observed item with zero clicks, and a failed feature-store lookup describe three different states, even when an implementation later maps some of them to the same model input.

Before comparing algorithms, establish that feature names, units, windows, and preprocessing match between training and serving. A better offline loss does not compensate for a feature contract that changes at deployment.

## Exercise

Compare the same ranker on two candidate generators.

Report candidate recall separately from [[NDCG]], and explain why a higher ranking score on an easier candidate set does not establish a better whole search system.

## References & Useful Links

- [LightGBM ranker](https://lightgbm.readthedocs.io/en/latest/pythonapi/lightgbm.LGBMRanker.html) — Grouped ranking interface.

[^1]: [XGBoost FAQ: How to deal with missing values](https://xgboost.readthedocs.io/en/stable/faq.html) — Missing values and learned default branch directions in tree boosters; `gblinear` treats missing as zero.

[^pairwise]: [XGBoost: Learning to rank objectives](https://xgboost.readthedocs.io/en/stable/tutorials/learning_to_rank.html) — Pairwise logistic loss, ranking-sensitive gradients, and query grouping.
