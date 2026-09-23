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

Given relevance $\operatorname{sim}_1(d,q)$, item–item similarity $\operatorname{sim}_2$, selected set $S$, remaining candidates $R\setminus S$, and $\lambda\in[0,1]$, select greedily:

$$d^*=\arg\max_{d\in R\setminus S}\Bigl[\lambda\,\operatorname{sim}_1(d,q)-(1-\lambda)\max_{d'\in S}\operatorname{sim}_2(d,d')\Bigr].$$

$\lambda=1$ is pure relevance ranking; smaller values penalise redundancy more. This is the standard statement of MMR; only the paper's abstract was accessible for verification.[^1]

## Worked Example

Relevance: A 0.90, B 0.85, C 0.60. Similarity: $\operatorname{sim}(A,B)=0.95$, $\operatorname{sim}(A,C)=0.20$, $\operatorname{sim}(B,C)=0.30$. Use $\lambda=0.7$.

1. $S$ empty: A $=0.630$, B $=0.595$, C $=0.420$. Select A.
2. B $=0.595-0.3(0.95)=0.310$; C $=0.420-0.3(0.20)=0.360$. Select C.
3. Select B.

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

## Exercise

Rerun the worked example with $\lambda=0.9$ and $\lambda=0.5$. At what $\lambda$ does B return to second place?

## Open Questions

- #TODO Review intent-aware diversity metrics such as α-NDCG from a primary source before adding them here.

## References & Useful Links

[^1]: [Carbonell and Goldstein, "The use of MMR, diversity-based reranking for reordering documents and producing summaries", SIGIR 1998](https://doi.org/10.1145/290941.291025) — MMR combines query relevance with novelty to reduce redundancy. Abstract read; full text was not accessible.
[^2]: [Google Cloud: Query public index to get nearest neighbors](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search/query-index-public-endpoint) — Per-crowding-tag neighbour limits for result diversity. Accessed 23 September 2026.
