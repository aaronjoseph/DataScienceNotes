# Named Entity Recognition

#search-eng

## Overview

Named entity recognition (NER) labels spans of text with entity types. Classic NER finds people, organisations, and locations. In product search, the same technique is often called **query tagging**: it finds brands, product types, attributes, sizes, and prices in the query so the system can turn them into filters or ranking signals.

NER is usually framed as **token classification**: every token receives a label.[^1] It is one component of [[Query Understanding]] and a common input to [[Query Intent Classification]].

## Mechanics

### BIO tagging

Each token is tagged `B-` (beginning of an entity), `I-` (inside the same entity), or `O` (outside any entity).[^1]

| Token | `sony` | `wireless` | `noise` | `cancelling` | `headphones` | `under` | `200` |
|---|---|---|---|---|---|---|---|
| Tag | B-brand | B-feature | B-feature | I-feature | B-type | B-price_op | B-price |

The entity schema here is illustrative. Define the schema from the catalogue's filterable attributes.

### Subword alignment

Transformer tokenisers split words into subwords, so labels must be realigned. A common convention labels only the first subword of each word and assigns `-100` to other subwords and special tokens, so the loss ignores them.[^1] See [[Tokenization]] and [[BERT]].

### Evaluation

Most tokens are `O`, so token accuracy looks deceptively high. Evaluate at the **entity level** with precision, recall, and F1, as the `seqeval` framework does.[^1] Then measure the downstream effect on retrieval, because a correct tag can still become a harmful filter.

## From Entities to Retrieval Decisions

NER output is not yet a query plan. Several further decisions are needed:

1. **Normalise and link.** Map the surface form to a catalogue ID: `hp` to a brand ID, `tv` to a product-type ID. Entity linking is a separate step from span detection.
2. **Whitelist.** Only approved entity types become filters; others are ignored or used as soft signals.
3. **Gate by catalogue state.** Discard product types that are no longer active.
4. **Choose hard or soft.** `under 200` becomes a numeric filter; a colour might be a ranking boost instead of a filter. This is a product decision.
5. **Hedge.** Keep a broader recall channel that does not apply NER-derived filters; see [[Candidate Generation]].
6. **Derive context.** An entity such as `refurbished` or `open box` can change which conditions are eligible.

## Worked Example

Query: `sony wireless headphones under 200`.

- Filters: `brand = sony`, `product_type = headphones`, `price <= 200`.
- In a vector index these become token restricts plus a numeric restrict with `LESS_EQUAL`; see [[Filtered Vector Search]].

Now suppose the model tags `wireless` as a product type and it links to "wireless earbuds". The filtered channel searches only earbuds, and over-ear headphones never enter the pool. A later ranker cannot recover them. A broad channel that converts the predicted type into a deny list or drops it can still retrieve them.

## Failure Modes

- **Little context.** Queries are short and lack grammar; `apple` can be a brand or a fruit.
- **Multiple types.** `tv and soundbar` needs per-type handling, not one merged filter.
- **Negation.** `laptop without touchscreen` must not become `feature = touchscreen`. The [[ESCI]] dataset sampled negation queries as hard cases.[^2]
- **Units and numbers.** `65` can mean inches, watts, or a model number.
- **Over-filtering.** Every extra hard filter shrinks the candidate pool; monitor zero-result and low-result rates.
- **Latency.** A model call on the critical path adds to [[Tail Latency]]. Cache results per session or normalised query, keyed so that a changed query cannot reuse stale entities.

## Exercise

Tag `samsung 55 inch qled tv not curved` with BIO labels. Decide which entities become hard filters, which become soft signals, and which you would ignore. Then name the recall channel that protects each hard filter against a tagging error.

## References & Useful Links

[^1]: [Hugging Face: Token classification](https://huggingface.co/docs/transformers/tasks/token_classification) — NER as token classification, BIO labels, subword label alignment, and entity-level `seqeval` metrics.
[^2]: [Reddy et al., "Shopping Queries Dataset", 2022](https://arxiv.org/abs/2206.06588) — Hard product queries sampled for negations, parse patterns, and price patterns.
