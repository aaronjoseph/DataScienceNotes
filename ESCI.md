---
note_type: concept
search_stage: evaluation
---

# ESCI

#search-eng

## Overview

ESCI is a four-class relevance scheme for product search: **Exact, Substitute, Complement, Irrelevant**. Amazon introduced it with the Shopping Queries Dataset (Reddy et al., 2022) because binary relevance cannot express cases such as an iPhone charger for the query `iPhone`.[^1]

It is useful both as a labelling rubric for a [[Judgement List]] and as an output class for relevance models.

## The Four Labels

| Label | Definition (from the paper) | Paper's example |
|---|---|---|
| Exact (E) | Relevant and satisfies all query specifications | A water bottle matching material and size for `plastic water bottle 24oz` |
| Substitute (S) | Somewhat relevant; fails some aspect but works as a functional substitute | Fleece for `sweater` |
| Complement (C) | Does not fulfil the query but could be used with an exact item | Track pants for `running shoes` |
| Irrelevant (I) | Irrelevant, or fails a central aspect of the query | Socks for `telescope`; wheat bread for `gluten-free bread` |

"Fails a central aspect" is the hard boundary. Whether a mismatch is central is a rubric decision.

## Dataset Facts

All figures are from the paper and repository.[^1][^2]

- About 130,000 unique queries and 2.6 million manually labelled query–product judgements; English, Spanish, and Japanese; up to 40 results per query.
- Queries were deliberately sampled to be difficult: unusual click or price distributions, negations, and linguistically complex parses. They do not represent traffic.
- At least three annotators per pair, with majority vote. An audit found 91% agreement overall and more than 96% for the binary Exact versus not-Exact distinction. About half of the discrepancies were Irrelevant items judged as Substitutes.
- The large version's labels are imbalanced: 65.2% E, 21.9% S, 2.9% C, 10.0% I.
- Splits are by query: 70% train, 15% public test, 15% private test.

## Tasks and Metrics

1. **Ranking:** order products E, then S, then C, then I; evaluate with [[NDCG]] using gains 1.0, 0.1, 0.01, and 0.0.
2. **Four-class classification:** evaluated with micro-averaged F1.
3. **Substitute identification:** binary classification, evaluated with F1.[^1]

## Worked Example

The example applies the paper’s gains directly, with no additional exponential transform.

A system returns `[S, E, I, C]` for one query. With the ESCI gains and discount $1/\log_2(i+1)$:

$$
\mathrm{DCG@4}=\frac{0.1}{1}+\frac{1.0}{\log_2 3}+\frac{0}{2}+\frac{0.01}{\log_2 5}\approx0.7352.
$$

**Ideal ranking:** `[E, S, C, I]`.

$$
\mathrm{IDCG@4}\approx1.0681
$$

**Normalise the returned ranking's DCG:**

$$
\mathrm{NDCG@4}=\frac{\mathrm{DCG@4}}{\mathrm{IDCG@4}}\approx0.688.
$$

This uses the gains directly; a $2^{rel}-1$ gain formulation would give a different number. State the convention.

## Using ESCI in a Search Pipeline

- **Rubric:** write query-specific notes on what counts as central, then label with E/S/C/I; see [[Annotation Agreement]].
- **Model output:** a [[Cross-Encoder]] classifier can predict classes. One production system maps E and S to "best match" and C and I to "probable match". That mapping is a product decision.
- **Type-level filtering:** remove product types whose candidates are consistently low-relevance before final ordering.
- **Complements:** useful for accessory slots, but mixing them into core results for a product query can look irrelevant.

## Limitations and Pitfalls

- **Substitute versus Irrelevant** is the noisiest boundary.[^1]
- **Imbalance:** micro-F1 is dominated by Exact. Report per-class and macro metrics too; see [[Imbalanced Classification]].
- **Sampling bias:** hard-query sampling means offline scores do not transfer directly to traffic-weighted outcomes.
- **Gains are a choice:** 1.0/0.1/0.01 is the paper's convention, not a universal value of substitutes.

## Separate Class Prediction from Ranking Utility

Suppose a classifier outputs probabilities $p_E,p_S,p_C,p_I$ summing to 1. Under the paper's gains, an expected-gain ranking score would be

$$
s=p_E+0.1p_S+0.01p_C.
$$

This is one possible scoring rule, derived from the chosen gains. Taking the most likely class and sorting by class is a different rule and can discard uncertainty. Neither method makes an uncalibrated probability vector reliable; evaluate the served ranking and any thresholds on representative judgments.

> [!example]- Classify the bread exercise using an explicit rubric
> Suppose `gluten-free bread 500g` requires gluten-free ingredients but allows a modest pack-size substitution. A matching 500 g loaf is Exact; a 400 g gluten-free loaf may be Substitute. Gluten-free flour and a bread knife do not fulfil the loaf request and need a stated complement policy. A wheat loaf violating the dietary constraint is Irrelevant.
>
> If 500 g is a hard requirement, the smaller loaf's label may change. The example demonstrates why the central-versus-optional boundary belongs in the rubric. It is not a universal label assignment for every product catalogue.

## Interpret Benchmark Results in Their Setting

Keep the dataset's hard-query sampling and query-level splits in view. Its published annotation agreement concerns that collection and audit procedure; it does not certify a new team or label model. Similarly, gains that heavily favour Exact items encode one evaluation preference. If a product wants accessories in a separate slot, evaluate that slot's task independently rather than assuming the same ordering objective applies everywhere.

For a deployed classifier, report a confusion matrix and per-class quality as well as the aggregate. Confusing Substitute with Irrelevant can alter candidate filtering, while confusing Exact with Substitute can mostly affect ordering; trace the actual downstream policy.

## Exercise

Label five results for `gluten-free bread 500g`: a 500 g gluten-free loaf, a 400 g gluten-free loaf, a gluten-free flour, a wheat loaf, and a bread knife.

Then compute NDCG@5 for one ordering.

Which label was hardest, and what rubric sentence would resolve it?

## References & Useful Links

[^1]: [Reddy et al., "Shopping Queries Dataset: A Large-Scale ESCI Benchmark for Improving Product Search", 2022](https://arxiv.org/html/2206.06588v1) — Label definitions, sampling, annotation agreement, class distribution, tasks, and baselines.
[^2]: [amazon-science/esci-data](https://github.com/amazon-science/esci-data) — Dataset files, fields, loading code, and baseline scripts.
