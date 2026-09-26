---
note_type: concept
search_stage: ranking
---

# Search Result Diversification

#search-eng

## Overview

A list ranked purely by per-item relevance can be repetitive: ten colour variants of one phone, or only laptops for an ambiguous query. **Diversification** reorders or constrains results so the page covers more useful options while staying relevant. It evaluates the list as a set, not item by item.

Carbonell and Goldstein's Maximal Marginal Relevance (MMR) is the classic formulation: combine query relevance with novelty relative to what has already been selected, reducing redundancy while maintaining relevance.[^1]

## Mechanisms

| Mechanism | Where it acts | Example |
|---|---|---|
| Crowding | Retrieval | At most $m$ neighbours per crowding tag, such as parent product[^2] |
| Variant collapse | Merge | Group SKUs under their parent; show one with a variant picker |
| Type grouping | Routing and merge | For `tv and soundbar`, retrieve and rank per type, then merge |
| Slot quotas | Presentation | Reserve positions for categories or sources |
| Greedy reranking | Final ordering | MMR over the top candidates |

## MMR

Define the inputs:

- $\operatorname{sim}_1(d,q)$: query relevance.
- $\operatorname{sim}_2$: item–item similarity.
- $S$: the already selected items.
- $R\setminus S$: the remaining candidates.
- $\lambda\in[0,1]$: the relevance–redundancy tradeoff.

Select the next item greedily:

$$
d^*=\arg\max_{d\in R\setminus S}\Bigl[\lambda\,\operatorname{sim}_1(d,q)-(1-\lambda)\max_{d'\in S}\operatorname{sim}_2(d,d')\Bigr].
$$

$\lambda=1$ is pure relevance ranking; smaller values penalise redundancy more.

This is the standard statement of MMR; only the paper's abstract was accessible for verification.[^1]

## Worked Example

With the illustrative tradeoff, a less redundant result moves above a near duplicate.

**Inputs**

| Item | Relevance |
|---|---:|
| A | 0.90 |
| B | 0.85 |
| C | 0.60 |

Pairwise similarities:

- $\operatorname{sim}(A,B)=0.95$.
- $\operatorname{sim}(A,C)=0.20$.
- $\operatorname{sim}(B,C)=0.30$.

Use $\lambda=0.7$.

**1. Select the first item.**

With an empty selected set, use zero redundancy penalty:

- A scores 0.630.
- B scores 0.595.
- C scores 0.420.

Select **A**.

**2. Compare the remaining items after selecting A.**

B's score is

$$
0.595-0.3(0.95)=0.310.
$$

C's score is

$$
0.420-0.3(0.20)=0.360.
$$

Select **C**, which has the higher score.

**3. Select B**, the remaining item.

The order is A, C, B instead of A, B, C. B is nearly a duplicate of A, so the lower-relevance but different C moves up.

## When Not to Diversify

- **Identifier lookups** and navigational queries: the user wants one specific item.
- **Explicit constraints:** `iphone 15 128gb blue` should not be diversified into other colours.
- **Narrow catalogues:** penalising similarity may promote irrelevant items.

[[Query Intent Classification]] can decide whether diversification applies.

## Evaluation

- Keep a relevance metric such as [[NDCG]] and add set measures: distinct parents@k, distinct product types@k, duplicates@k.
- Check whether relevant items were pushed below the fold.
- Test on ambiguous and multi-type queries separately from specific ones.

## Limitations and Pitfalls

- **Wrong similarity:** embedding similarity may treat genuinely different sizes as duplicates, or different products with similar titles as distinct.
- **Crowding too early:** a retrieval crowding limit can remove the variant that a later filter would have kept.
- **Cost:** greedy MMR compares each remaining candidate with the selected set; limit it to the top of the list.

## Initialise and Interpret MMR Explicitly

The maximum similarity to an empty selected set is undefined.

A practical convention selects the most relevant item first, then applies MMR to subsequent slots; this agrees with setting the initial redundancy penalty to zero when $\lambda>0$.

At $\lambda=0$, specify a first-item and tie-breaking rule explicitly.

> [!example]- Solve the tradeoff in the worked example
> After A is selected, the difference between B's and C's MMR scores is
>
> $$
> \lambda(0.85-0.60)-(1-\lambda)(0.95-0.20)=\lambda-0.75.
> $$
>
> B therefore comes second when $\lambda>0.75$, C when $\lambda<0.75$, and they tie at 0.75. Thus 0.9 gives A, B, C, while 0.5 gives A, C, B.
>
> The threshold depends on both similarity scales. Rescaling relevance without adjusting the redundancy term changes the meaning of the same $\lambda$.

## Evaluate Repetition with Subtopic Judgments

Distinct-parent counts measure a structural property of the list; they do not prove that useful intents were covered.

Clarke et al. define a novelty-aware gain using binary judgments $J(d_i,t)$ for subtopic $t$ and the number $n_{t,i-1}$ of earlier results covering it:[^diversity]

**Novelty-aware gain at rank $i$:**

$$
G_i=\sum_t J(d_i,t)(1-\alpha)^{n_{t,i-1}}
$$

**Discount and sum those gains:**

$$
\alpha\text{-DCG@}k=\sum_{i=1}^k\frac{G_i}{\log_2(i+1)}.
$$

For $0\le\alpha<1$, repeated coverage of the same subtopic earns diminishing gain.

With $\alpha=0.5$, successive documents covering only that subtopic earn 1, 0.5, and 0.25 before rank discounting.

Normalised alpha-NDCG additionally needs a stated ideal-ranking procedure over the same judged universe.

This requires subtopic judgments, not just ordinary per-document relevance grades.

## Exercise

Rerun the worked example with $\lambda=0.9$ and $\lambda=0.5$. At what $\lambda$ does B return to second place?

## Open Questions

- #TODO Work through alpha-NDCG normalisation with a multi-intent product judgment set, including the ideal-ranking approximation used by the evaluator.

## References & Useful Links

[^1]: [Carbonell and Goldstein, "The use of MMR, diversity-based reranking for reordering documents and producing summaries", SIGIR 1998](https://doi.org/10.1145/290941.291025) — MMR combines query relevance with novelty to reduce redundancy. Abstract read; full text was not accessible.
[^2]: [Google Cloud: Query public index to get nearest neighbors](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search/query-index-public-endpoint) — Per-crowding-tag neighbour limits for result diversity. Accessed 23 September 2026.

[^diversity]: [Clarke et al., Novelty and Diversity in Information Retrieval Evaluation, SIGIR 2008](https://cormack.uwaterloo.ca/novelty.pdf) — Subtopic/nugget judgments, diminishing novelty gain, and discounted evaluation.
