---
note_type: concept
search_stage: foundations
tags:
  - "search-eng"
---

BERT means **Bidirectional Encoder Representations from Transformers**. Researchers at Google AI Language introduced it as a pretrained [[Encoder-Only Model (Transformers)|Transformer encoder]] (Devlin et al., 2019). It reads the whole input at once, so each token's vector depends on the words to its left and right. The model is pretrained once on unlabelled text, then fine-tuned for a task by adding a small output layer.[^bert]

## Why BERT Mattered

Before BERT, pretrained language representations were mostly one-directional:

- **OpenAI GPT** used a left-to-right Transformer: each token sees only earlier tokens.
- **ELMo** concatenated separately trained left-to-right and right-to-left LSTMs, a shallow combination of two one-directional views.

BERT argued that deep bidirectional context matters for tasks such as question answering, where a word's meaning depends on both sides. An ordinary language model cannot simply condition on both sides: in a multi-layer network each word could indirectly "see itself". BERT's solution is the masked language model described below.[^bert]

"Bidirectional" therefore means every layer uses both sides jointly. It is not two separate one-directional models joined together.

## Architecture

| Model | Layers $L$ | Hidden size $H$ | Heads $A$ | Parameters |
|---|---:|---:|---:|---:|
| BERT-base | 12 | 768 | 12 | 110M |
| BERT-large | 24 | 1024 | 16 | 340M |

The encoder is almost identical to the original [[Transformers|Transformer]] encoder.[^bert] BERT-base was deliberately sized like OpenAI GPT so the two could be compared; the key difference is bidirectional rather than causal self-attention.

The Hugging Face default configuration, matching `bert-base-uncased`, also sets a feed-forward size of 3072, GELU activation, dropout 0.1, and 512 position embeddings.[^hf-bert]

> [!example]- Where do 110 million parameters come from?
> Using the Hugging Face configuration (vocabulary 30,522, 512 positions, 2 segment types, $H=768$, feed-forward 3072):
>
> 1. **Embeddings,** including one LayerNorm:
>
>    $$
>    (30{,}522 + 512 + 2) \times 768 + 2 \times 768 \approx 23.8\text{M}
>    $$
>
> 2. **One encoder layer:** four attention projections, two feed-forward matrices, their biases, and two LayerNorms $\approx 7.09$M.
>
> 3. **Twelve layers:** $12 \times 7.09\text{M} \approx 85.1$M.
>
> 4. **Pooler:**
>
>    $$
>    768 \times 768 + 768 \approx 0.59\text{M}
>    $$
>
> The total is about 109.5M, which the paper rounds to 110M. About a fifth of the parameters are in the embedding tables.

## Input Representation

### Special tokens and segments

- **Tokenizer:** WordPiece with a 30,000-token vocabulary; the uncased Hugging Face checkpoint has 30,522 entries.[^bert][^hf-bert]
- **`[CLS]`:** always the first token. Its final hidden vector, $C$, is the aggregate representation for classification.
- **`[SEP]`:** separates two segments and ends the sequence.
- **Segment embedding:** marks each token as belonging to segment A or B (`token_type_ids` 0 or 1 in Hugging Face).
- **"Sentence":** in the paper this means any contiguous span of text, not necessarily a grammatical sentence.

### Three embeddings are summed

$$
E_i = E_{\text{token}}(x_i) + E_{\text{segment}}(s_i) + E_{\text{position}}(i)
$$

Position embeddings are learned and absolute, with 512 positions. Hugging Face recommends padding on the right for this reason.[^hf-bert]

### Example: a query–document pair

For the query `red hiking boots` and the title `waterproof leather hiking boot`, the packed input looks like this:

```text
token:     [CLS]  red  hiking  boots  [SEP]  waterproof  leather  hiking  boot  [SEP]
segment:     0     0     0       0      0        1          1        1      1     1
position:    0     1     2       3      4        5          6        7      8     9
```

This layout is illustrative. The real WordPiece split depends on the vocabulary: a rare word may become several pieces such as `flight ##less`.

## Pretraining

BERT was pretrained on BooksCorpus (800M words) and English Wikipedia (2,500M words), using only text passages. The authors emphasise a document-level corpus, so that long contiguous sequences can be extracted.[^bert]

### Task 1: Masked language modelling

1. Choose 15% of WordPiece positions at random.
2. For each chosen position:
   - 80% of the time, replace it with `[MASK]`: `my dog is hairy` → `my dog is [MASK]`.
   - 10% of the time, replace it with a random token: `my dog is apple`.
   - 10% of the time, leave it unchanged: `my dog is hairy`.
3. Predict the original token at every chosen position with a cross-entropy loss. Other positions do not contribute to this loss.

`[MASK]` never appears during fine-tuning. Mixing the three replacements reduces that mismatch and means the model cannot tell which tokens will be tested, so it must keep a useful representation of every token.[^bert]

### Task 2: Next sentence prediction

For each pair of segments, 50% of the time segment B really follows A (`IsNext`). Otherwise B is a random segment from the corpus (`NotNext`). The vector $C$ predicts the label.[^bert]

```text
[CLS] the man went to [MASK] store [SEP] he bought a gallon [MASK] milk [SEP]           → IsNext
[CLS] the man [MASK] to the store [SEP] penguin [MASK] are flight ##less birds [SEP]    → NotNext
```

BERT's own ablation found that removing next-sentence prediction (NSP) hurt QNLI, MNLI, and SQuAD 1.1. [[RoBERTa]] later found that removing it matched or slightly improved results with a different input format. Treat NSP's value as recipe-dependent.[^bert][^roberta]

### Training recipe

- **Batch:** 256 sequences × 512 tokens, about 128,000 tokens per batch.
- **Length:** 1,000,000 steps, roughly 40 epochs over 3.3 billion words.
- **Optimiser:** Adam, learning rate $10^{-4}$, 10,000 warm-up steps, linear decay, weight decay 0.01.
- **Regularisation:** dropout 0.1 on all layers; GELU activation.
- **Sequence length:** 128 tokens for 90% of steps, then 512 for the final 10%, because attention cost grows quadratically with length.
- **Hardware:** BERT-base took 4 days on 16 TPU chips; BERT-large took 4 days on 64.[^bert]

## Worked Example: Counting the Masks

Inputs:

- One sequence of 512 tokens.
- Masking rate 15%.
- Replacement split 80% / 10% / 10%.

**Step 1 — positions selected for prediction**

$$
512 \times 0.15 = 76.8
$$

About 77 positions contribute to the loss; the other 435 do not.

**Step 2 — positions replaced by `[MASK]`**

$$
76.8 \times 0.8 = 61.44
$$

**Step 3 — random replacements, and positions left unchanged**

$$
76.8 \times 0.1 = 7.68 \text{ each}
$$

Random replacement touches only $0.15 \times 0.1 = 1.5\%$ of all tokens, which the authors argue is small enough not to harm language understanding.[^bert]

**Interpretation.** A left-to-right model receives a training target at every position; the masked model receives one at about 15% of positions. The paper found that the masked model converged slightly more slowly but outperformed the left-to-right model in accuracy almost immediately.[^bert]

## Fine-Tuning

All parameters are updated during fine-tuning; only a small output layer is new.[^bert]

| Task type | Input | Output used | Example |
|---|---|---|---|
| Single-text classification | `[CLS] text [SEP]` | $C$ | Sentiment |
| Pair classification | `[CLS] A [SEP] B [SEP]` | $C$ | Entailment, relevance |
| Token labelling | `[CLS] text [SEP]` | Every token vector $T_i$ | [[Named Entity Recognition]] |
| Extractive question answering | `[CLS] question [SEP] passage [SEP]` | Start and end scores | SQuAD |

### Classification head

For $K$ labels, the only new parameters are $W \in \mathbb{R}^{K\times H}$. The model is trained with the standard classification loss on $\operatorname{softmax}(CW^{\top})$.[^bert]

### Extractive question answering

Fine-tuning learns a start vector $S$ and an end vector $E$. The probability that passage token $i$ starts the answer is:

$$
P_i^{\text{start}} = \frac{e^{S\cdot T_i}}{\sum_j e^{S\cdot T_j}}
$$

The predicted span maximises the following score, subject to $j \ge i$:[^bert]

$$
S \cdot T_i + E \cdot T_j
$$

For SQuAD 2.0, where some questions have no answer, "no answer" is represented as a span that starts and ends at `[CLS]`. A threshold chosen on development data decides when to abstain.

Extractive question answering selects a span from the passage. It cannot write an answer that is not in the text.

### Recommended hyperparameter ranges

- Batch size 16 or 32.
- Adam learning rate $5\times10^{-5}$, $3\times10^{-5}$, or $2\times10^{-5}$.
- 2 to 4 epochs.

Small datasets were more sensitive to these choices. BERT-large fine-tuning was sometimes unstable on small datasets, so the authors ran several random restarts and kept the best development result.[^bert]

### Using frozen features

BERT can also be used without fine-tuning. On CoNLL-2003 named-entity recognition, concatenating the top four hidden layers came within 0.3 F1 of full fine-tuning.[^bert] This is useful when you want to compute representations once and train many cheaper models on top.

## A Note on `pooler_output`

Hugging Face's `BertModel` returns `last_hidden_state`, one vector per token, and `pooler_output`. The pooler output is the `[CLS]` vector passed through a linear layer and tanh whose weights were trained on the NSP objective.[^hf-bert] It is not automatically a good sentence embedding.

## Search Applications

- **Cross-encoder reranking:** feed `[CLS] query [SEP] document [SEP]` and fine-tune $C$ to predict relevance. Every query token can attend to every document token. See [[Cross-Encoder]].
- **Bi-encoder retrieval:** encode query and document separately, pool each into one vector, and compare them with a dot product or [[Cosine Similarity|cosine similarity]]. This needs retrieval-specific training, such as the contrastive training in [[Dense Retrieval]]; a raw pretrained checkpoint is not trained for it.
- **Query understanding:** token classification for entities ([[Named Entity Recognition]]) and sequence classification for intent ([[Query Intent Classification]]).

Preserve the checkpoint's [[Tokenization|tokenizer]], casing (`uncased` or `cased`), input format, and truncation policy. With a 512-token limit, long documents must be truncated or split into passages, so decide explicitly which part of each document the model sees.

## Limitations & Common Pitfalls

- **Not a text generator:** BERT predicts masked tokens and classifies; it is not trained to generate left to right. Compare [[Decoder-Only Model (Transformers)|decoder-only models]].
- **Length limit:** anything beyond 512 positions is invisible unless you split the text.
- **Serving cost:** each forward pass runs 110M–340M parameters. For reranking, cost grows with the number of query–document pairs.
- **Benchmarks are not your task:** the paper's gains on GLUE, SQuAD, and SWAG do not guarantee gains on your queries. Evaluate on your own [[Judgement List|relevance judgments]].
- **Casing and accents:** the uncased tokenizer lowercases and strips accents, which can merge distinct identifiers.

## Exercise

1. Compare "river bank" with "bank account". Explain why BERT's final vectors for `bank` can differ, whereas a [[Word2Vec]] vector cannot.
2. Explain why averaging those token vectors without retrieval training may still produce poor nearest neighbours.
3. A product description has 700 WordPiece tokens. Propose two ways to score it with a 512-token cross-encoder, and name one risk of each.

> [!example]- Exercise solution
> 1. Every BERT layer mixes in surrounding tokens through self-attention, so `bank` next to `river` and `bank` next to `account` produce different contextual vectors. Word2Vec stores one vector per word type, whatever the context.
>
> 2. Masked-token training teaches vectors to predict missing words, not to place relevant query–document pairs close together. Averaged vectors can be dominated by frequent tokens or surface overlap. Retrieval needs an objective that pulls relevant pairs together and pushes irrelevant pairs apart.
>
> 3. **Truncate** to the first tokens that fit: simple, but details later in the text are lost. **Split into overlapping passages** and aggregate, for example by taking the highest passage score: the whole text is covered, but each document costs several forward passes and needs an aggregation rule.

Continue with [[RoBERTa]] for the improved training recipe and [[Search Evaluation]] for measuring a BERT reranker.

## References & Useful Links

[^bert]: [Devlin et al. (2019), BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding](https://arxiv.org/html/1810.04805v2) — Architecture, input representation, masked language modelling, next-sentence prediction, training recipe, fine-tuning, and ablations. The published version is the [NAACL PDF](https://aclanthology.org/N19-1423.pdf).
[^hf-bert]: [Hugging Face Transformers — BERT](https://huggingface.co/docs/transformers/model_doc/bert) — Configuration defaults, special tokens, padding side, `pooler_output`, and task heads.
[^roberta]: [Liu et al. (2019), RoBERTa](https://arxiv.org/abs/1907.11692) — Replication study that re-examined next-sentence prediction.
