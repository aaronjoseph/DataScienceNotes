---
note_type: concept
search_stage: experiments
---

# Interleaving

#search-eng

## Overview

Interleaving compares two rankers online by merging their results into **one** list shown to the same user, then crediting each click to the ranker that contributed the clicked item. Each impression yields a paired preference: A wins, B wins, or tie.

Because both rankers are judged on the same query, user, and moment, much of the between-user noise in a standard [[AB Testing|A/B test]] cancels. Radlinski, Kurup, and Joachims found that none of eight absolute usage metrics (for example, clicks, reformulation rate, and abandonment) reliably reflected retrieval quality at their sample sizes. Paired interleaving tests did.[^1] Chapelle et al. later found interleaving much more sensitive than absolute click metrics on two commercial search engines and a scientific-literature system, often reducing the queries needed by over an order of magnitude.[^2]

## Team-Draft Interleaving

The algorithm follows the analogy of two captains picking teams:[^1]

1. In each round, if one ranker has contributed fewer items, it picks next; on a tie, a coin flip decides.
2. The picking ranker adds its highest-ranked item not already in the list and records it on its team.
3. Stop when either ranker has no unused items left.
4. Credit each click to the team that owns the clicked item. More credited clicks means a preference; equal counts mean a tie.

The random alternation ensures that a user who clicks at random produces equally many preferences for A and B in expectation. This fixes a bias the authors identified in the earlier Balanced Interleaving method.[^1]

```python
def team_draft(a, b, bits):
    interleaved, team_a, team_b = [], set(), set()
    bits = iter(bits)  # coin flips, fixed here for a reproducible example
    while any(x not in interleaved for x in a) and any(x not in interleaved for x in b):
        if len(team_a) < len(team_b) or (len(team_a) == len(team_b) and next(bits) == 1):
            pick = next(x for x in a if x not in interleaved)
            team_a.add(pick)
        else:
            pick = next(x for x in b if x not in interleaved)
            team_b.add(pick)
        interleaved.append(pick)
    return interleaved, team_a, team_b

def preference(clicks, team_a, team_b):
    ha = sum(c in team_a for c in clicks)
    hb = sum(c in team_b for c in clicks)
    return "A" if ha > hb else "B" if hb > ha else "tie"

ranked, ta, tb = team_draft(["a", "b", "c", "d"], ["b", "e", "a", "f"], bits=[1, 0, 1])
print(ranked, sorted(ta), sorted(tb))  # ['a', 'b', 'e', 'c', 'd'] ['a', 'c', 'd'] ['b', 'e']
print(preference(["b", "c"], ta, tb))  # tie
print(preference(["b", "e"], ta, tb))  # B
```

## Worked Example

With A = `(a, b, c, d)`, B = `(b, e, a, f)`, and coin flips `1, 0, 1`, the shown list is `(a, b, e, c, d)`. A owns `a, c, d`; B owns `b, e`.

- Clicks on `b` and `c`: one credit each, so a tie.
- Clicks on `b` and `e`: two credits for B, so B wins.

Item `b` is ranked highly by both rankers but credited only to B.

For these particular input lists, B always drafts `b`: either B picks first, or A picks `a` and B then picks `b`.

Fairness under a no-preference click model does not require every shared item to have equal ownership probability.

## Aggregating and Testing

- Aggregate per query or per user. In the arXiv study, a per-user vote was the majority of that user's click preferences.[^1]
- Test whether A's share of non-tie outcomes differs from 0.5, for example with a binomial test.[^1]
- Report the tie rate. Team-Draft produces a strict preference for any query with a single click, even when the two rankings are identical, which can add variance for very similar rankers.[^1]

## From Impressions to a Decision

Keep the displayed order, item ownership, randomisation choices, experiment version, and attributed clicks together in the impression record. Recomputing ownership from the two original rankings later is insufficient: shared items can be drafted by either team. Missing or delayed clicks also need a declared observation window.

After applying a predefined aggregation rule, count:

- $W_A$: independent units preferring A.
- $W_B$: independent units preferring B.
- $T$: ties.

Report both measures below.

**A's share of non-tie outcomes:**

$$
\hat p_A=\frac{W_A}{W_A+W_B}
$$

**Tie rate:**

$$
\text{tie rate}=\frac{T}{W_A+W_B+T}.
$$

If all outcomes are ties, the preference share is undefined.

Under the no-preference null, a binomial test compares non-tie outcomes with $p_A=0.5$.

Many impressions from one user are not automatically independent trials; choose user or query aggregation to match the experiment and account for remaining dependence.[^1]

### A preference share is not a success rate

**Inputs:** 1,000 aggregated units produce:

- 330 wins for A.
- 270 wins for B.
- 400 ties.

**A's non-tie preference share:**

$$
\frac{330}{330+270}=55\%
$$

**Tie rate:**

$$
\frac{400}{1000}=40\%
$$

This does not mean 55% of all users completed their task, nor that conversion increased by 5 percentage points.

For the exercise with flips `0, 1, 0`, the list is `b, a, c, e, f`; A owns `a, c`, while B owns `b, e, f`. Item `b` still belongs to B. Now make the two rankings identical: random draft choices can change which team owns each position, even though the rankers have equal quality.

## When to Use It

| Use interleaving for | Use an A/B test for |
|---|---|
| Fast relative comparison of two rankers | Absolute business outcomes: revenue, retention, successful sessions |
| Screening many candidate rankers before an A/B test | Changes that alter the page, latency, or result count |
| Small ranking differences needing sensitivity | Effects that need long-term or cross-session measurement |

A common workflow screens candidates with interleaving and confirms the winner with an A/B test. Interleaving measures preference within the result list, not whole-product impact.

## Limitations and Pitfalls

- **Clicks remain biased signals.** Position, presentation, and misleading snippets still affect clicks; see [[Click Bias]].[^1]
- **Both rankers must be served together.** Doubled candidate generation and reranking costs can matter; see [[Tail Latency]].
- **Presentation must be neutral.** Snippet or image quality that differs by ranker biases credit.[^1]
- **Business rules can mask differences.** If policy reorders the merged list, credit reflects the rules as well as the rankers; see [[Score Normalization#Business Ordering|business ordering]].
- **Domain.** The 2008 study used a scientific-literature search engine; the authors caution that other domains differ.[^1]

## Exercise

Trace `team_draft` with coin flips `0, 1, 0`.

Which team owns `b` now?

Then use identical input rankings and explain how a single click can produce a strict preference even though the two rankers are equally good.

The distinction is between a random individual outcome and an unbiased aggregate comparison under the method's assumptions.

## References & Useful Links

[^1]: [Radlinski, Kurup, and Joachims, "How Does Clickthrough Data Reflect Retrieval Quality?", CIKM 2008](https://www.cs.cornell.edu/people/tj/publications/radlinski_etal_08b.pdf) — Absolute metrics versus paired tests on arXiv, Team-Draft Interleaving algorithm, aggregation, and limitations.
[^2]: [Chapelle, Joachims, Radlinski, and Yue, "Large-Scale Validation and Analysis of Interleaved Search Evaluation", ACM TOIS 2012](http://www.cs.cornell.edu/people/tj/publications/chapelle_etal_12a.pdf) — Agreement with judgements, statistical efficiency, and interleaving variants on commercial search engines.
