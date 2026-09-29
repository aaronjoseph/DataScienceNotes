---
aliases:
  - Jev
  - TypeSafe Jev
  - System One Model
tags:
  - "ai-engineering"
---

System One models are a class of AI models introduced by TypeSafe AI in September 2026. They read natural-language input and return **typed decisions with probabilities** instead of generated text. Jev is the first model in the class.[^blog][^docs-s1]

TypeSafe calls Jev "a frontier-intelligence function call": unstructured state goes in, typed probabilistic decisions come out.[^blog] You define the possible answers in advance, and the model returns a probability distribution over them.

> [!warning] Vendor claims
> Nearly everything below comes from TypeSafe's own blog and documentation, accessed on 29 September 2026. The speed, cost, and calibration claims have not been independently verified here, and the model architecture is not disclosed.

## Descriptive or Probabilistic?

Jev is **probabilistic**: every answer is a probability or a distribution over answers you specify. In the terms of [[Discriminative and Generative Models]], its interface is discriminative. It estimates the probability of each allowed answer given the input, and it cannot generate text, code, or explanations.[^docs-s1]

The name comes from Daniel Kahneman's *Thinking, Fast and Slow*, which contrasts fast, intuitive **System 1** judgements with slow, deliberate **System 2** reasoning. TypeSafe targets the fast kind: judgements a knowledgeable person could make in a few seconds.[^docs-s1][^docs-intro]

## The Interface

A request contains a **state** (the text or JSON to evaluate) and a set of **questions**. Every question is evaluated against the same state, in parallel and in isolation.[^docs-intro]

| Primitive | Asks | Returns |
|---|---|---|
| Choice | Which option from a list applies? | `choice`, `probabilities`, `confidence` |
| Score | Where does the state fall on a rubric of levels? | `score`, `probabilities`, `confidence` |
| Noul | Is this statement true? | `noul`, the probability of yes |

The documentation's Noul example asks two questions about the message "I have asked three times now. Can I please just talk to a real person?"[^docs-noul]

```json
{
  "state": "I have asked three times now. Can I please just talk to a real person?",
  "model": "jev-latest",
  "questions": {
    "is_human_escalation": {"type": "noul", "instructions": "Is the customer asking for a human agent?"},
    "is_repeat_contact": {"type": "noul", "instructions": "Has the customer contacted support about this before?"}
  }
}
```

The documented response gives 0.99 for `is_human_escalation` and 0.93 for `is_repeat_contact`.[^docs-noul] Code then applies thresholds, so the model never takes an action itself.

**Design rule from the docs:** ask atomic questions. Instead of "rate this startup pitch", ask separately about market size, feasibility, and differentiation, then combine the answers in code, where the weights are easy to change.[^docs-intro]

## Confidence

For Choice and Score answers, `confidence` summarises how concentrated the probability distribution is: 1 when all probability sits on one option, lower as it spreads out.[^docs-conf] For a Noul there is no separate confidence, because the single probability of yes already describes the whole distribution.[^docs-noul]

The documentation's interactive demo approximates confidence for $K$ options from the largest probability $p_{\max}$, clipped to the range 0 to 1:[^docs-conf]

$$
\text{confidence} \approx \frac{K\,p_{\max} - 1}{K - 1}
$$

It equals 0 for a uniform distribution and 1 for a certain one. TypeSafe computes the returned value itself, and the docs note that other measures may suit some tasks, which is why the full `probabilities` are also returned.

### Worked example: three options

**Inputs.** A Choice question with $K = 3$ options.

**Case 1 — clear winner, probabilities 0.90, 0.06, 0.04.**

$$
\frac{3 \times 0.90 - 1}{3 - 1} = \frac{1.7}{2} = 0.85
$$

**Case 2 — spread out, probabilities 0.40, 0.33, 0.27.**

$$
\frac{3 \times 0.40 - 1}{3 - 1} = \frac{0.2}{2} = 0.10
$$

**Case 3 — even split, all three at 1/3.**

$$
\frac{3 \times \tfrac{1}{3} - 1}{3 - 1} = 0
$$

**Interpretation.** Both of the first two cases choose the same option, but only the first is a safe basis for automatic action. The documentation suggests three paths: act automatically at high confidence, confirm or review at medium confidence, and route to a person or another system at low confidence. The thresholds should be stricter for costly or irreversible actions.[^docs-conf]

Confidence measures how concentrated the distribution is, not whether it is calibrated. Calibration means that among answers given probability 0.8, about 80% are correct, and it can only be checked across many labelled predictions. The docs say the same: calibration describes groups of predictions, not any single answer.[^docs-primer]

## Training: RLHF, RLVR, and RLCD

TypeSafe positions its training method against two established post-training approaches:[^blog][^docs-primer]

- **RLHF (reinforcement learning from human feedback):** fine-tunes a model on rankings of its outputs by human labellers, as in InstructGPT.[^instructgpt] It optimises for responses people prefer. Diogo Almeida, a co-founder of TypeSafe, is an InstructGPT co-author.
- **RLVR (reinforcement learning with verifiable rewards):** a name introduced in the Tulu 3 post-training work.[^tulu3] It rewards outputs that can be checked programmatically, such as maths answers.
- **RLCD (reinforcement learning for calibrated decisions):** TypeSafe's method. It returns decisions and probabilities instead of text, with the stated goal that higher probability means a higher chance of being correct.[^docs-primer]

TypeSafe argues that RLHF can reward sycophancy and confident-sounding hallucinations, and can cause "mode dropping", a narrowing of the output distribution.[^docs-primer] Read that as the company's position, not an established finding.

## Claimed Performance

| Claim | TypeSafe's statement |
|---|---|
| Latency | 70–500 ms end to end, against 3–329 s for frontier LLMs |
| Price | $0.042 per million input tokens; output tokens not charged |
| Headline gain | 193.6× faster and 444.6× cheaper, described as the high end of real-world gains |
| Type errors | 0%, guaranteed by construction rather than measured |
| Choice size | Up to 255 options; larger choices use a two-stage process |
| Input | Text only: strings, JSON objects, and arrays |

Sources: the announcement blog[^blog] and the System One documentation.[^docs-s1] The blog adds that its published evaluations were run from laptops on the US West Coast, and that it cannot prove its pricing is not subsidised.

## How They Evaluate, and the Caveats

TypeSafe's "workflow evals" run the same coded workflow with each model. They then compare the answers with the **average probabilities of two large frontier models**, used as the reference.[^blog] The blog lists its own caveats:

- The reference answers are other models' outputs, not ground-truth labels, and they lean towards OpenAI's and Anthropic's models.
- The workflows were written by TypeSafe's model-capabilities team, so some bias is possible.
- LLM hallucination rates in the comparison come from OpenRouter, which may route harder queries to stronger models.

**Assessment.** Agreement with a reference model measures imitation of that model, not accuracy or calibration. These results show that Jev tracks frontier models cheaply on TypeSafe's workflows; they do not show that its probabilities are calibrated on your task.

## Evaluate It on Your Own Task

1. **Label a test set** drawn from real traffic, including ambiguous and out-of-scope cases, as in [[LLM Evaluation]].
2. **Measure accuracy** at the thresholds you would actually use.
3. **Measure calibration** with reliability diagrams and Brier score, as in [[Probability Calibration]].
4. **Compare baselines:** an LLM with [[Structured Outputs]], a small fine-tuned classifier such as [[BERT]], and [[Logistic Regression]] on simple features.
5. **Measure p50 and p95 latency** from your own region, since averages hide slow requests ([[Tail Latency]]).
6. **Recheck after model updates.** The `jev-latest` alias can move to a new model version, so pin a version where possible.

## Search Connection

- **Routing and intent:** a Choice question over intents is a [[Query Intent Classification]] model you configure with instructions instead of training data.
- **Re-ranking:** the documentation's re-ranking cookbook asks one Noul per query–candidate pair and sorts candidates by the probability.[^docs-noul] This is pointwise scoring, similar in shape to a [[Cross-Encoder]]. Evaluate it with ranking metrics such as [[NDCG]], and budget for one question per candidate.
- **Guardrails:** Noul checks for injection or policy violations can gate LLM inputs and outputs; see [[Prompt Injection]].

## Why "Jev"?

The model is named after William Stanley Jevons. He observed that more efficient steam engines increased total coal use, an effect now called the Jevons paradox. TypeSafe expects cheaper machine intelligence to increase demand for it in the same way.[^blog]

## Limitations

- **No generation:** it cannot write replies, code, or explanations.
- **Atomic questions only:** tasks needing extended reasoning must be decomposed in code or escalated to a reasoning model.[^docs-intro]
- **Text input only:** no images, audio, or video at the time of writing.[^docs-s1]
- **Early access and vendor dependence:** closed model, undisclosed architecture, and pricing that may change.

## Exercise

A Choice question has four options with probabilities 0.70, 0.10, 0.10, and 0.10. Compute the demo confidence. Your system auto-acts above 0.75 and sends answers below 0.4 to a person. What happens to this answer?

> [!example]- Exercise solution
> **Step 1 — confidence with $K = 4$.**
>
> $$
> \frac{4 \times 0.70 - 1}{4 - 1} = \frac{1.8}{3} = 0.60
> $$
>
> **Step 2 — apply the policy.** 0.60 is between 0.4 and 0.75, so the answer falls in the middle band: ask the user to confirm, or queue it for review, rather than acting automatically.
>
> A 70% top probability sounds high, but with four options the remaining 30% is spread thinly, so the answer is less decisive than it first appears.

## Open Questions

- TODO: The blog's FAQ answers (why a new training algorithm was needed, whether Jev is "just a smaller LLM", public benchmark results, and training-data sources) did not load and remain unread.
- TODO: Check whether TypeSafe publishes reliability diagrams or calibration error on held-out labelled data.

## References & Useful Links

[^blog]: [TypeSafe AI — Introducing System One Models & Jev](https://typesafe.ai/blog/introducing-system-one-models-and-jev) — Announcement by founder Diogo Almeida: comparison with LLMs, RLCD, pricing and latency claims, workflow evals and their caveats, demos, and the origin of the names. Accessed 29 September 2026.
[^docs-intro]: [TypeSafe docs — Introduction](https://docs.typesafe.ai/) — State and questions; the Choice, Score, and Noul primitives; parallel, isolated evaluation; guidance on atomic questions.
[^docs-s1]: [TypeSafe docs — System One](https://docs.typesafe.ai/concepts/system-one) — Definition of the model class, how it differs from an LLM, text-only input, and the Kahneman naming.
[^docs-conf]: [TypeSafe docs — Confidence](https://docs.typesafe.ai/confidence) — Confidence derived from the probability distribution, the demo approximation formula, three action paths, and risk-scaled thresholds.
[^docs-noul]: [TypeSafe docs — Noul](https://docs.typesafe.ai/primitives/noul) — Yes/no questions, the example request and response, reading and thresholding values, and cookbooks including re-ranking.
[^docs-primer]: [TypeSafe docs — AI primer](https://docs.typesafe.ai/introduction/machine-learning-primer) — RLHF, RLVR, and RLCD; the calibration definition; TypeSafe's critique of RLHF.
[^instructgpt]: [Ouyang et al. (2022), Training language models to follow instructions with human feedback](https://arxiv.org/abs/2203.02155) — The InstructGPT RLHF method; author list includes Diogo Almeida.
[^tulu3]: [Lambert et al. (2024), Tulu 3: Pushing Frontiers in Open Language Model Post-Training](https://arxiv.org/abs/2411.15124) — Introduces Reinforcement Learning with Verifiable Rewards (RLVR).
