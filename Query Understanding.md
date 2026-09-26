---
note_type: concept
search_stage: query_understanding
---

# Query Understanding

#search-eng

## Purpose

Query understanding turns an expressed query into retrieval decisions while preserving the user's intent. It can include language detection, spelling correction, token analysis, entity extraction, synonym expansion, and interpretation of constraints. More rewriting is not automatically better.

## Distinguish the Operations

- **Text analysis:** [[Tokenization]], case handling, [[Stemming and Lemmatization]], and [[Stopwords]] affect indexed and searched terms.
- **Entity interpretation:** recognise a product type, brand, size, or identifier with uncertainty and context. See [[Named Entity Recognition]]; routing by query type is covered in [[Query Intent Classification]].
- **Expansion:** add alternatives while controlling precision loss.
- **Constraint handling:** decide whether an attribute is mandatory or a preference; make that a product rule rather than a silent model guess.

Index and query analysis should be compatible, not necessarily identical. Preserve original text and the applied transformation for diagnosis. Query-time synonyms can support changes without the same reindexing implications as index-time expansion; verify the engine's exact behaviour.

## Worked Scenario

For `red waterproof hiking boots size 9`, extract candidate attributes, then ask whether size is expressed in a known sizing system and whether red is a hard constraint. Blindly expanding boots to every shoe type can hurt precision. For an identifier such as `AB-123`, punctuation or stemming changes may destroy the match.

## Query Rewriting

A rewrite replaces or augments the user's query before retrieval. Common sources:

| Source | Example | Main risk |
|---|---|---|
| Spelling correction | `hedphones` → `headphones` | Correcting a valid brand or model name |
| Curated rewrite map | Exact normalised query → replacement | Stale entries; silent coverage gaps |
| Synonym expansion | `tv` also matches `television` | Precision loss from loose synonyms |
| Relaxation | Drop a term after zero results | Returning results that ignore a hard constraint |
| Model-generated rewrite | Paraphrase from a language model | Changed identifiers, negation, or intent |

Practices:

- **Keep the original query.** Log the original, the rewrite, and its source for every request.
- **Decide the order.** Rewriting before [[Named Entity Recognition|NER]] changes which entities are found; rewriting after changes only retrieval text.
- **Key exact rewrite maps by the normalised query** and normalise the same way when writing and reading. Cached rewrites need a refresh path; see [[Search Caching]].
- **Make fallbacks visible.** A zero-result retry with a relaxed query should be flagged in the response and logs, so its quality can be measured separately.
- **Protect identifiers.** Route identifier-like queries away from rewriting; see [[Query Intent Classification]].

Evaluate each rewrite source separately: queries affected, change in zero-result rate, and judged quality on affected queries only. An aggregate over all traffic dilutes a harmful rewrite that affects few queries.

## Make the Interpretation Inspectable

Represent the interpretation as explicit fields: original text, normalised text, proposed rewrite, detected spans, linked catalogue values, route, hard filters, and soft preferences. For each decision, retain its source and version. This makes it possible to identify whether an error came from spelling correction, entity linking, policy, or retrieval.

An important invariant is that a rewrite should preserve explicit requirements. If the user says `not curved`, the transformed request must still express that exclusion. A fluent rewrite can violate this invariant. Likewise, `under 200` and `at most 200` need different numeric operators when interpreted literally.

> [!example]- Resolve an ambiguous price and size request
> For `red hiking boots size 9 under 200`, an inspectable plan might record product type `hiking boots`, colour `red`, size text `9`, and price operator `<`. The currency and sizing system require context; do not invent US sizing or a currency merely because a number was recognised.
>
> If red is mandatory, it belongs in eligibility. If the product deliberately treats red as a preference, record that policy and evaluate its effect. A broad fallback can help when interpretation is uncertain, but it must still respect explicit constraints that the system has accepted as hard requirements.

## Measure Decisions at Their Boundaries

Track route accuracy, entity span accuracy, catalogue-link accuracy, and filter correctness before looking at final relevance. Also measure downstream effects on the affected query slice. A parser can have high token accuracy while making a few costly hard-filter errors. Compare the intended plan with the plan actually sent to each retrieval channel; logging only the final query string hides these distinctions.

## Evaluation and Exercise

Create query cases with expected interpretations, including ambiguity, negation, typos, identifiers, and multilingual input. Track both parsing correctness and downstream retrieval quality. Compare the original query with any [[Decoder-Only Model (Transformers)|model-generated rewrite]] instead of treating fluency as fidelity.

Change only one analysis rule on the tiny collection in [[Search Engineering]]. Explain new matches and lost matches. Follow through [[Inverted Index]], [[Hybrid Retrieval]], and [[Search Evaluation]].

## References & Useful Links

- [Elasticsearch text analysis](https://www.elastic.co/docs/manage-data/data-store/text-analysis) — Index-time and search-time analysis.
