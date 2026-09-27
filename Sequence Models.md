A sequence model works with ordered data, where the position of each element carries meaning: words in a sentence, frames of audio, clicks in a session, or values in a [[Time Series|time series]]. The input, the output, or both can be sequences. Predicting the next item of a sequence is one common task, but classifying a whole sequence or translating one sequence into another are sequence modelling too.

## Model Criteria

To model sequences, the important factors are:

1. **Handle variable-length sequences.** A query may have 2 tokens and a document 2,000; the same model must accept both.
2. **Track long-term dependencies.** In "the boots I bought last winter were not waterproof", `not` changes the meaning of `waterproof` several words later.
3. **Maintain information about the order.** "dog bites man" and "man bites dog" contain the same words.
4. **Share parameters across the sequence.** The same weights process every position, so something learned at position 3 also applies at position 30.

## Input–Output Shapes

| Shape | Example |
|---|---|
| One-to-many | Generating a caption from an image |
| Many-to-one | Classifying the sentiment or intent of a query |
| Many-to-many, same length | Tagging each token with an entity label |
| Many-to-many, different length | [[Machine Translation]], query rewriting |

[[RNN]] describes these shapes for recurrent networks; the same categories apply to [[Transformers]].

## Model Families

| Family | Handles order by | Long-range dependencies | Parallel across positions |
|---|---|---|---|
| [[N-Gram Model\|N-gram]] | Counting fixed windows of $n$ items | Only within $n-1$ items | Yes (counting) |
| [[RNN]] | Updating a hidden state step by step | Weak: [[Vanishing & Exploding Gradients\|vanishing gradients]] | No |
| [[LSTM]] | Gated cell state updated step by step | Better, still sequential | No |
| RNN encoder–decoder | Compressing the input into a vector, then generating | Limited by the fixed-length vector | No |
| RNN + attention | Letting the decoder look back at every input state | Much better | No |
| [[Transformers\|Transformer]] | Positional information plus self-attention | Any two positions directly connected | Yes, in training |

### The encoder–decoder step

Sutskever, Vinyals, and Le used one multilayer LSTM to map an input sentence to a fixed-size vector and another LSTM to decode the translation from it. On WMT'14 English–French they reported 34.8 BLEU, compared with 33.3 for a phrase-based statistical system. Reversing the word order of source sentences markedly improved results, because it created many short-range dependencies between source and target.[^seq2seq]

### The attention step

Bahdanau, Cho, and Bengio argued that the fixed-length vector was a bottleneck. Their model lets the decoder soft-search for the parts of the source sentence relevant to each target word.[^bahdanau] The [[Transformers|Transformer]] later removed recurrence altogether and kept only attention.

## Worked Example: Sequential Steps

Inputs: a sequence of $n = 100$ tokens and one layer.

**Step 1 — recurrent layer.** Each hidden state depends on the previous one:

$$
\text{sequential steps} = n = 100
$$

**Step 2 — self-attention layer.** All positions are computed together, but every pair is scored:

$$
\text{pairwise scores per head} = n^2 = 10{,}000
$$

**Interpretation.** The recurrent layer does less total work but must wait 100 steps. The attention layer does more total work, but that work is parallel, so it can run faster on GPUs for moderate $n$. As $n$ grows, the quadratic term eventually dominates, which is why long-context attention is a separate engineering problem.

## Exercise

Classify each task by input–output shape and say whether a causal (left-to-right) model is required:

1. Predicting the next search query in a session.
2. Labelling brand and colour tokens in `nike red running shoes`.
3. Rewriting `cheap lap top` as `affordable laptop`.

> [!example]- Exercise solution
> 1. **Many-to-one** per step, or many-to-many if predicting a whole next query. A causal model fits, because at prediction time future queries are unknown.
>
> 2. **Many-to-many, same length.** A bidirectional encoder is appropriate: `red` is easier to label as a colour when the model can also see `shoes`. See [[Named Entity Recognition]].
>
> 3. **Many-to-many, different length.** An [[Encoder-Decoder Model (Transformers)|encoder–decoder]] or a decoder-only model can do this. The input may be read bidirectionally, but the output must be generated left to right.

## References & Useful Links

[^seq2seq]: [Sutskever, Vinyals & Le (2014), Sequence to Sequence Learning with Neural Networks](https://arxiv.org/abs/1409.3215) — LSTM encoder–decoder, reported BLEU, and the effect of reversing source order.
[^bahdanau]: [Bahdanau, Cho & Bengio (2014), Neural Machine Translation by Jointly Learning to Align and Translate](https://arxiv.org/abs/1409.0473) — The fixed-length bottleneck and attention as soft search.
