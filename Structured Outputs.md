---
aliases:
  - Constrained Decoding
  - JSON Mode
note_type: concept
search_stage: serving
tags:
  - "search-eng"
  - "ai-engineering"
---

Structured outputs make a large language model (LLM) return data that matches a schema, such as a JSON object with fixed keys and allowed values, instead of free text. Code can then read the answer without fragile parsing. The same mechanism powers strict [[Tool Calling|tool calls]].

The key limit: a schema guarantees the **shape** of an answer, not its **truth**. A well-formed wrong answer is still wrong.

## Three Levels of Control

| Level | What you do | Guarantee |
|---|---|---|
| Prompt only | Ask for JSON in the instructions | None; parse, validate, retry |
| JSON mode | Enable a JSON-only output mode | Valid JSON, no schema |
| Schema-constrained | Supply a JSON Schema in strict mode | Output matches the supported schema subset |

OpenAI's documentation describes JSON mode as ensuring valid JSON, while Structured Outputs also ensures adherence to a supplied schema. It recommends Structured Outputs where supported. Strict schemas must mark every field as required and set `additionalProperties` to `false`; optional fields are expressed as a union with `null`.[^openai-so] Other providers use different names and limits, so check the provider you use.

## How Constrained Decoding Works

An autoregressive model produces one token at a time from a probability distribution over its vocabulary (see [[Language Model]]). Constrained decoding removes the tokens that would make the output invalid at each step.

Notation: $V$ is the vocabulary, $x_{<t}$ the tokens generated so far, and $A_t \subseteq V$ the tokens that keep the output valid at step $t$. The masked distribution renormalises the model's probabilities over the allowed set:

$$
\tilde{p}(v \mid x_{<t}) = \frac{p(v \mid x_{<t})\,\mathbf{1}[v \in A_t]}{\sum_{u \in A_t} p(u \mid x_{<t})}
$$

Here $\mathbf{1}[v \in A_t]$ is 1 for allowed tokens and 0 otherwise.

Willard and Louf frame this as transitions of a finite-state machine built from a regular expression or grammar. Indexing the vocabulary against that machine in advance makes the check cheap during generation.[^outlines]

## Worked Example: Masking a Label

A support router asks an LLM for `{"team": "billing" | "technical"}`. At the step where the value is chosen, suppose the model's next-token probabilities are:

- `billing`: 0.5
- `technical`: 0.2
- `Sure` (the start of a chatty reply): 0.3

**Step 1 — sum the allowed mass.**

$$
0.5 + 0.2 = 0.7
$$

**Step 2 — renormalise `billing`.**

$$
\tilde{p}(\texttt{billing}) = \frac{0.5}{0.7} \approx 0.714
$$

**Step 3 — renormalise `technical`.**

$$
\tilde{p}(\texttt{technical}) = \frac{0.2}{0.7} \approx 0.286
$$

**Interpretation.** The output is guaranteed valid, but 0.3 of the model's probability went to text it was not allowed to produce, and that mass was redistributed. The 0.714 is a statement about the masked decoder, not a calibrated probability that the ticket belongs to billing. Treat it as a score until you check it with [[Probability Calibration]].

## What the Guarantee Does Not Cover

- **Correctness:** OpenAI notes that Structured Outputs can still contain mistakes.[^openai-so]
- **Irrelevant input:** the model always tries to fit the schema, which can produce hallucinated values when the input has nothing to do with the task. Give it an explicit way out, such as a `null` or `"unknown"` value.[^openai-so]
- **Refusals and truncation:** a safety refusal or a hit output-token limit can end without a schema-conforming object, so handle those cases in code.[^openai-so]
- **Distribution distortion:** Park et al. show that token-by-token constrained decoding can distort the LLM's distribution, producing valid outputs whose likelihoods are not proportional to those the unconstrained model assigns.[^gad]
- **Authorisation and business rules:** a schema cannot tell whether an order ID belongs to the user. Validate in code, as in [[Tool Calling#Validate Every Call in Code|tool-call validation]].

## Choosing an Approach for Decisions

When software needs a decision rather than prose, such as a route, a label, or a yes/no check, there are several options:

1. **Structured outputs from a general LLM:** flexible; the whole generation cost is still paid, and confidence needs separate handling.
2. **A fine-tuned classifier:** for example a [[BERT]] model with a softmax head. Fast and cheap, but needs labelled data and retraining when labels change.
3. **Typed decision models:** [[System One Models]] such as TypeSafe's Jev return only a probability distribution over predefined answers, without generating text. Their speed and calibration claims come from the vendor and need checking on your own data.

In every case, evaluate on a labelled set with accuracy, calibration, and latency, as in [[LLM Evaluation]].

## Search Connection

Query understanding often converts a query into structured fields, such as intent, category, price range, or brand filters (see [[Query Understanding]] and [[Query Intent Classification]]). Schema constraints make the output parseable, but a hallucinated brand or category is still a wrong filter that can remove relevant results. Log the structured interpretation next to the raw query, and evaluate retrieval with and without the filters it produced.

## Exercise

A schema has `"category": {"enum": ["shoes", "bags", "unknown"]}`. For the query "gift for my dad", the model's next-token probabilities are 0.35 for `shoes`, 0.15 for `bags`, 0.10 for `unknown`, and 0.40 for tokens outside the enum. Compute the masked probability of `shoes`, and explain what the 0.40 tells you.

> [!example]- Exercise solution
> **Step 1 — allowed mass.**
>
> $$
> 0.35 + 0.15 + 0.10 = 0.60
> $$
>
> **Step 2 — masked probability of `shoes`.**
>
> $$
> \frac{0.35}{0.60} \approx 0.583
> $$
>
> The model put 40% of its probability outside the allowed labels, a sign that the query does not fit the taxonomy well. The masked decoder still commits to a category. A safer design treats a large discarded mass or a low top probability as a reason to choose `unknown` or skip the filter, and tunes that rule on labelled queries.

## References & Useful Links

[^openai-so]: [OpenAI API — Structured model outputs](https://developers.openai.com/api/docs/guides/structured-outputs) — JSON mode versus Structured Outputs, the supported schema subset, required fields and `additionalProperties`, refusals, truncation, and handling of mistakes and irrelevant input. Accessed 29 September 2026; details are provider-specific.
[^outlines]: [Willard and Louf (2023), Efficient Guided Generation for Large Language Models](https://arxiv.org/abs/2307.09702) — Guided generation as finite-state-machine transitions, with a vocabulary index for regular expressions and context-free grammars; implemented in the Outlines library.
[^gad]: [Park et al. (2024), Grammar-Aligned Decoding](https://arxiv.org/abs/2405.21047) — Shows that constrained decoding can distort the LLM's distribution, and proposes a sampler that matches the grammar-conditioned distribution. NeurIPS 2024.
