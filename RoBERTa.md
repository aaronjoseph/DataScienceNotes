---
note_type: concept
search_stage: foundations
tags:
  - "search-eng"
---

RoBERTa means **A Robustly Optimized BERT Pretraining Approach** (Liu et al., Facebook AI and the University of Washington, 2019). It is a careful replication study of [[BERT]]: the architecture and the masked-language-model objective stay the same, but the training procedure changes. The authors concluded that BERT had been significantly undertrained.[^roberta]

The practical lesson is that training recipe and data can matter as much as architecture. Two models with identical layers can differ substantially in quality.

## What Changed from BERT

| Setting | BERT | RoBERTa |
|---|---|---|
| Masking | Static: created once during preprocessing | Dynamic: a new mask each time a sequence is used |
| Next-sentence prediction | Yes | Removed |
| Input format | Segment pairs; short sequences for 90% of steps | Full sentences packed up to 512 tokens; full length throughout |
| Batch size | 256 sequences | 8,000 sequences |
| Tokenizer | 30K subword vocabulary | 50K byte-level BPE; no unknown tokens |
| Pretraining text | 16GB | 160GB |

The paper tests each change separately before combining them.[^roberta]

## The Four Experiments

### 1. Static versus dynamic masking

BERT's original implementation masked the data once. To avoid reusing the same mask every epoch, the training data was duplicated 10 times, so each sequence saw 10 different masks over 40 epochs; each mask was therefore seen four times.[^roberta]

Dynamic masking generates the mask whenever a sequence is fed to the model. For BERT-base, the medians over five seeds were:

| Masking | SQuAD 2.0 F1 | MNLI-m | SST-2 |
|---|---:|---:|---:|
| Static | 78.3 | 84.3 | 92.5 |
| Dynamic | 78.7 | 84.0 | 92.9 |

Dynamic masking was comparable or slightly better, and it avoids duplicating data. It matters more when training longer or on more data.

### 2. Input format and next-sentence prediction

The authors compared four ways of building inputs:

- **Segment-pair + NSP:** BERT's original format.
- **Sentence-pair + NSP:** pairs of single natural sentences.
- **Full-sentences:** contiguous sentences packed up to 512 tokens, possibly crossing document boundaries; no NSP.
- **Doc-sentences:** the same, but never crossing a document boundary; no NSP.

| Format | SQuAD 1.1 / 2.0 | MNLI-m | SST-2 | RACE |
|---|---:|---:|---:|---:|
| Segment-pair + NSP | 90.4 / 78.7 | 84.0 | 92.9 | 64.2 |
| Sentence-pair + NSP | 88.7 / 76.2 | 82.9 | 92.1 | 63.0 |
| Full-sentences | 90.4 / 79.1 | 84.7 | 92.5 | 64.8 |
| Doc-sentences | 90.6 / 79.7 | 84.7 | 92.7 | 65.6 |

Single sentences hurt performance, which the authors attribute to losing long-range context. Removing NSP matched or slightly improved results. Doc-sentences was slightly best, but it produces variable batch sizes, so RoBERTa uses full-sentences. The paper suggests BERT's original ablation may have removed the NSP loss while keeping the segment-pair format.[^roberta]

### 3. Larger batches

These three settings process the same number of sequences:

| Batch | Steps | Learning rate | Held-out perplexity | MNLI-m | SST-2 |
|---:|---:|---:|---:|---:|---:|
| 256 | 1M | 1e-4 | 3.99 | 84.7 | 92.7 |
| 2K | 125K | 7e-4 | 3.68 | 85.2 | 92.9 |
| 8K | 31K | 1e-3 | 3.77 | 84.6 | 92.8 |

Larger batches improved perplexity and end-task accuracy in this comparison and are easier to parallelise. RoBERTa trains with 8K-sequence batches. The authors also found training sensitive to Adam's epsilon and used $\beta_2=0.98$ for stability with large batches.[^roberta]

### 4. Byte-level BPE

BERT's vocabulary is built from characters after heuristic preprocessing. RoBERTa uses a byte-level byte-pair encoding (BPE) with 50K units, following GPT-2. Because the base symbols are bytes, any text can be encoded without an unknown token.[^roberta] See [[Tokenization#Subword Tokenizers for Transformers|subword tokenizers]].

The larger vocabulary adds about 15M parameters to the base model and 20M to the large model. Early experiments showed slightly worse results on some tasks, but the authors preferred a universal encoding.

## Worked Example: Checking the Numbers

**Step 1 — equal compute across batch sizes.** Count sequences processed:

$$
256 \times 1{,}000{,}000 = 256{,}000{,}000
$$

$$
2{,}048 \times 125{,}000 = 256{,}000{,}000
$$

$$
8{,}192 \times 31{,}250 = 256{,}000{,}000
$$

"2K" and "8K" are rounded labels; the paper's 31K steps is also rounded. The comparison changes how updates are grouped, not how much data is seen.

**Step 2 — why the vocabulary adds parameters.** The embedding matrix has one row per vocabulary entry. Moving from about 30K to 50K entries adds about 20K rows:

$$
20{,}000 \times 768 \approx 15.4\text{M}\quad(\text{base})
$$

$$
20{,}000 \times 1{,}024 \approx 20.5\text{M}\quad(\text{large})
$$

These match the paper's reported increases of about 15M and 20M.

## Combining the Changes: More Data, Longer Training

RoBERTa-large follows the BERT-large architecture: 24 layers, hidden size 1024, 16 heads, 355M parameters. The 100K-step run on BookCorpus and Wikipedia used 1,024 V100 GPUs for about a day.[^roberta]

The five pretraining corpora total over 160GB:

- BookCorpus and English Wikipedia: 16GB, BERT's original data.
- CC-News: 76GB of English news collected September 2016 – February 2019.
- OpenWebText: 38GB of web text from Reddit-shared links.
- Stories: 31GB of story-like CommonCrawl text.

Development results as each change accumulates:

| Configuration | Data | Steps | SQuAD 1.1 / 2.0 | MNLI-m | SST-2 |
|---|---:|---:|---:|---:|---:|
| RoBERTa | 16GB | 100K | 93.6 / 87.3 | 89.0 | 95.3 |
| + more data | 160GB | 100K | 94.0 / 87.7 | 89.3 | 95.6 |
| + longer | 160GB | 300K | 94.4 / 88.7 | 90.0 | 96.1 |
| + longer still | 160GB | 500K | 94.6 / 89.4 | 90.2 | 96.4 |
| BERT-large (reported) | 13GB | 1M | 90.9 / 81.8 | 86.6 | 93.7 |

Even the longest-trained model did not appear to overfit, and the authors expected further gains from more training.[^roberta]

## Using RoBERTa in Practice

- **Different tokenizer and special tokens.** BERT token IDs cannot be reused. Hugging Face's RoBERTa uses `<s>` and `</s>` instead of `[CLS]` and `[SEP]`, and the default vocabulary has 50,265 entries.[^hf-roberta]
- **No segment IDs.** RoBERTa does not use `token_type_ids`; separate the query and document with the separator token.[^hf-roberta]
- **Spaces matter.** The tokenizer treats a leading space as part of a word, so `Hello` and ` Hello` receive different IDs. Keep query and document formatting consistent between training and serving.[^hf-roberta]
- **Fine-tuning ranges in the paper:** for GLUE, batch size 16 or 32, learning rates 1e-5 to 3e-5, 6% warm-up, up to 10 epochs with early stopping.[^roberta]

## Interpretation and Limits

- The benchmark gains (GLUE, SQuAD, and RACE as of July 2019) are evidence for the tested setup, not a guarantee for every dataset, compute budget, or search application.
- RoBERTa inherits BERT's limits: a 512-token window and no left-to-right generation.
- The broader point: before crediting an architecture for a quality difference, control data size, training steps, batch size, and tokenizer.

A pretrained language-understanding checkpoint still needs task-appropriate adaptation and evaluation for [[Embeddings]] or relevance scoring.

## Exercise

For a fair BERT/RoBERTa reranking comparison, hold the candidate set and relevance labels fixed. Record each model's tokenizer, truncation, fine-tuning data, and serving cost. Which differences come from architecture, and which come from the training recipe? See [[Search Ranking]] and [[Tokenization]].

> [!example]- Exercise solution
> **Architecture:** almost nothing differs. Both are Transformer encoders with the same layer counts, hidden sizes, and heads for base or large.
>
> **Training recipe and data:** dynamic masking, no next-sentence prediction, full-length packed inputs, larger batches, a byte-level vocabulary, ten times more pretraining text, and longer training.
>
> **Serving differences:** RoBERTa's larger vocabulary slightly increases model size. Its tokenizer may split a query into a different number of tokens, which changes truncation and latency. Measure both on your own queries.
>
> **Fair comparison:** fine-tune both on the same labelled data, with the same candidate lists, maximum length, and tuning budget, and report the same metric, such as [[NDCG]]@10, on held-out queries.

## References & Useful Links

[^roberta]: [Liu et al. (2019), RoBERTa: A Robustly Optimized BERT Pretraining Approach](https://arxiv.org/html/1907.11692v1) — Masking, input-format, batch-size, and tokenizer experiments; data; hyperparameters; and results. The [PDF](https://arxiv.org/pdf/1907.11692) was the previously saved reference.
[^hf-roberta]: [Hugging Face Transformers — RoBERTa](https://huggingface.co/docs/transformers/model_doc/roberta) — Special tokens, absence of `token_type_ids`, vocabulary size, and leading-space behaviour.
