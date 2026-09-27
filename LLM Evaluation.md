---
note_type: concept
search_stage: evaluation
tags:
  - "search-eng"
---

LLM evaluation measures whether a system built on a large language model gives correct, grounded, safe, and useful outputs. For search and [[Retrieval-Augmented Generation|retrieval-augmented generation]] (RAG), it extends [[Search Evaluation]]: the ranked list is now consumed by a model, and the final output is free text rather than a list of documents.

The core discipline does not change. Fix a versioned test set, define each metric's unit and denominator, keep stages separate, and report what the evaluation does not establish. "The answers look good" is not an evaluation result.

## Separate the Questions

| Layer | Question | Unit |
|---|---|---|
| Retrieval | Did the needed evidence reach the prompt? | Query, labelled passage |
| Grounding | Is each claim supported by the provided evidence? | Claim |
| Citation | Does each citation support its sentence? | Citation or sentence |
| Answer quality | Is the answer correct, complete, and relevant? | Answer |
| Abstention | Does the system decline when evidence is missing? | Query |
| Safety | Does it resist injection and refuse disallowed actions? | Test case |
| Operations | Latency, tokens, cost, error rate | Request |

Keep these distinct in reports. A system can be perfectly faithful to irrelevant passages, or correct while citing the wrong source.

## Build the Test Set

Include several query types, and label each one before running the system:

- **Representative:** sampled from real or realistic traffic.
- **Ambiguous:** several plausible interpretations; record the expected behaviour, such as asking a clarifying question.
- **Unanswerable:** the collection does not contain the answer; the correct behaviour is to abstain.
- **Adversarial:** attempts at [[Prompt Injection|prompt injection]], requests for secrets, or out-of-scope actions.
- **Regression cases:** every production failure, once fixed.

Version the set, along with the model name and version, prompt, retrieval settings, and date of each run, so results can be reproduced. Label retrieval evidence with the conventions in [[Judgement List]]; measure labeller consistency with [[Annotation Agreement]].

## Metric Definitions

Notation for one answer:

- $C$: claims in the answer; $C_s$: claims supported by the retrieved passages.
- $R$: citations in the answer; $R_s$: citations that support the sentence they are attached to.
- $N$: sentences that need a citation; $N_c$: those with at least one supporting citation.

**Faithfulness (groundedness)**

$$
\text{faithfulness} = \frac{C_s}{C}
$$

**Citation precision**

$$
\text{citation precision} = \frac{R_s}{R}
$$

**Citation recall**

$$
\text{citation recall} = \frac{N_c}{N}
$$

Across a test set, also track:

- **Correct abstention rate** on unanswerable queries: the share where the system declined.
- **False abstention rate** on answerable queries: the share where it declined although the evidence was present.

State the denominators explicitly. If an answer has no claims because the system abstained, exclude it from faithfulness and count it under abstention instead.

## Worked Example

Inputs from one evaluation run:

- One answer with 5 claims, 4 supported by the retrieved passages.
- The same answer has 6 citations, 5 of which support their sentence.
- 4 sentences need citations; 3 have a supporting citation.
- Across the test set: 10 unanswerable queries, with abstention on 7; 40 answerable queries, with abstention on 4.

**Step 1 — faithfulness**

$$
\frac{4}{5} = 0.80
$$

**Step 2 — citation precision**

$$
\frac{5}{6} \approx 0.83
$$

**Step 3 — citation recall**

$$
\frac{3}{4} = 0.75
$$

**Step 4 — correct abstention rate**

$$
\frac{7}{10} = 0.70
$$

**Step 5 — false abstention rate**

$$
\frac{4}{40} = 0.10
$$

**Interpretation.** One claim in five lacks support, so this answer needs review even though most of its citations are valid. The system answers 3 of 10 unanswerable questions, a risk if users act on those answers, while declining 1 in 10 answerable ones. Raising the abstention threshold would likely trade one error for the other; report both rates together.

## Model-Graded Evaluation

Using a strong model as a judge scales evaluation, but it is a measurement instrument with known biases. Zheng et al. studied LLM-as-a-judge and identified **position**, **verbosity**, and **self-enhancement** biases, as well as limited reasoning ability. In their benchmarks, strong judges such as GPT-4 agreed with human preferences over 80% of the time, about the same level as agreement between humans.[^judge] That result is for their tasks and judges, not a guarantee for yours.

Practical safeguards:

- **Calibrate against humans:** label a sample by hand, and report judge–human agreement before trusting judge scores.
- **Control position:** for pairwise comparisons, evaluate both orders and count only consistent verdicts.
- **Score small units:** judge individual claims against given passages rather than asking for one overall quality score.
- **Pin the judge:** record the judge model, version, and prompt; changing them changes the metric.
- **Treat scores as diagnostics:** use them to find cases for manual review, not as the only acceptance gate.

Ragas proposes reference-free metrics for RAG, which assess context relevance, faithfulness, and answer quality without human-written reference answers.[^ragas] Reference-free does not mean assumption-free: the metrics still depend on the model that computes them.

## Offline Checks and Online Outcomes

Offline metrics answer "is it grounded and correct on this test set?". Online experiments answer "does it help users?". Keep them separate, as with [[AB Testing]]:

- Offline: faithfulness, citation correctness, abstention, retrieval recall.
- Online: task completion, follow-up rate, escalations to a human, user feedback.
- Serving: latency percentiles, token usage, cost per request, and error rate; see [[Tail Latency]] and [[Monitoring - MLOPS|monitoring]].

## Common Pitfalls

- **Tuning on the test set:** keep a held-out split, as in [[Cross Validation]].
- **One aggregate score:** a single average hides a rise in unsupported answers on a small but important slice.
- **Changing several things at once:** a new prompt, model, and chunking rule in one run cannot be attributed.
- **Ignoring variance:** sampled decoding can change outputs between runs; repeat runs or use deterministic settings for regression tests.

## Exercise

A new prompt raises average judge-rated quality from 4.1 to 4.4 out of 5, while faithfulness falls from 0.92 to 0.85. Should you ship it? What would you check first?

> [!example]- Exercise solution
> Not yet. The judge may prefer longer, more confident answers (verbosity bias), which could explain both a higher quality score and more unsupported claims.
>
> Check first:
>
> 1. **Answer length:** compare average length between prompts.
> 2. **Manual review:** read a sample of answers whose faithfulness dropped, and confirm the unsupported claims by hand.
> 3. **Abstention:** check whether the new prompt answers more unanswerable questions.
> 4. **Judge agreement:** confirm judge–human agreement on this sample.
>
> Ship only if the faithfulness drop is explained and acceptable for the use case.

## References & Useful Links

[^judge]: [Zheng et al. (2023), Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena](https://arxiv.org/abs/2306.05685) — Biases of model judges and reported agreement with human preferences.
[^ragas]: [Es et al. (2023), Ragas: Automated Evaluation of Retrieval Augmented Generation](https://arxiv.org/abs/2309.15217) — Reference-free evaluation dimensions for RAG.
