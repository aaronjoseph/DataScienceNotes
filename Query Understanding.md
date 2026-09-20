# Query Understanding

#search-eng

## Purpose

Query understanding turns an expressed query into retrieval decisions while preserving the user's intent. It can include language detection, spelling correction, token analysis, entity extraction, synonym expansion, and interpretation of constraints. More rewriting is not automatically better.

## Distinguish the Operations

- **Text analysis:** [[Tokenization]], case handling, [[Stemming and Lemmatization]], and [[Stopwords]] affect indexed and searched terms.
- **Entity interpretation:** recognise a product type, brand, size, or identifier with uncertainty and context.
- **Expansion:** add alternatives while controlling precision loss.
- **Constraint handling:** decide whether an attribute is mandatory or a preference; make that a product rule rather than a silent model guess.

Index and query analysis should be compatible, not necessarily identical. Preserve original text and the applied transformation for diagnosis. Query-time synonyms can support changes without the same reindexing implications as index-time expansion; verify the engine's exact behaviour.

## Worked Scenario

For `red waterproof hiking boots size 9`, extract candidate attributes, then ask whether size is expressed in a known sizing system and whether red is a hard constraint. Blindly expanding boots to every shoe type can hurt precision. For an identifier such as `AB-123`, punctuation or stemming changes may destroy the match.

## Evaluation and Exercise

Create query cases with expected interpretations, including ambiguity, negation, typos, identifiers, and multilingual input. Track both parsing correctness and downstream retrieval quality. Compare the original query with any [[Decoder-Only Model (Transformers)|model-generated rewrite]] instead of treating fluency as fidelity.

Change only one analysis rule on the tiny collection in [[Search Engineering]]. Explain new matches and lost matches. Follow through [[Inverted Index]], [[Hybrid Retrieval]], and [[Search Evaluation]].

## References & Useful Links

- [Elasticsearch text analysis](https://www.elastic.co/docs/manage-data/data-store/text-analysis) — Index-time and search-time analysis.
