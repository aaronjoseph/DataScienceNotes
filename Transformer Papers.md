A reading list for the transformer notes, in roughly the order the ideas build on each other. Each row says why the paper is worth reading; the links are in the references below.

**Before Transformers**

| Paper | Year | Why read it | Vault note |
|---|---:|---|---|
| Sequence to Sequence Learning with Neural Networks[^tp-seq2seq] | 2014 | LSTM encoder compresses a sentence into one vector; an LSTM decoder generates the translation | [[Sequence Models]] |
| Neural Machine Translation by Jointly Learning to Align and Translate[^tp-bahdanau] | 2014 | Introduces attention as soft search to avoid the fixed-length bottleneck | [[Machine Translation]] |

**The architecture and its main families**

| Paper | Year | Why read it | Vault note |
|---|---:|---|---|
| Attention Is All You Need[^tp-aiayn] | 2017 | Removes recurrence; defines scaled dot-product and multi-head attention | [[Transformers]] |
| BERT[^tp-bert] | 2019 | Bidirectional encoder pretrained with masked-token prediction | [[BERT]] |
| RoBERTa[^tp-roberta] | 2019 | Shows the training recipe matters as much as the architecture | [[RoBERTa]] |
| T5: Exploring the Limits of Transfer Learning[^tp-t5] | 2019 | Casts every text task as text-to-text with an encoder–decoder | [[Encoder-Decoder Model (Transformers)]] |
| BART[^tp-bart] | 2019 | Denoising encoder–decoder: BERT-like encoder, GPT-like decoder | [[Encoder-Decoder Model (Transformers)]] |
| Language Models are Few-Shot Learners (GPT-3)[^tp-gpt3] | 2020 | Tasks specified in the prompt, with no gradient updates | [[Decoder-Only Model (Transformers)]] |

**Training, decoding, and serving details**

| Paper | Year | Why read it | Vault note |
|---|---:|---|---|
| Layer Normalization[^tp-ln] | 2016 | Normalisation used in every Transformer block | [[Layer Normalization]] |
| On Layer Normalization in the Transformer Architecture[^tp-preln] | 2020 | Why Pre-LN trains more stably than Post-LN | [[Layer Normalization]] |
| The Curious Case of Neural Text Degeneration[^tp-nucleus] | 2019 | Nucleus (top-p) sampling | [[Decoder-Only Model (Transformers)]] |
| GQA: Grouped-Query Attention[^tp-gqa] | 2023 | Fewer key–value heads for faster decoding | [[Decoder-Only Model (Transformers)]] |
| PagedAttention / vLLM[^tp-vllm] | 2023 | KV-cache memory management for high-throughput serving | [[Decoder-Only Model (Transformers)]] |

**Using and questioning large models**

| Paper | Year | Why read it | Vault note |
|---|---:|---|---|
| Retrieval-Augmented Generation[^tp-rag] | 2020 | Combines a retriever with a generator | [[Retrieval-Augmented Generation]] |
| Lost in the Middle[^tp-lost] | 2023 | Models use information at the start and end of long contexts better than the middle | [[Retrieval-Augmented Generation]] |
| Attention is Not All You Need (rank collapse)[^tp-dong] | 2021 | Pure attention loses rank with depth; skip connections and MLPs prevent it | [[Research_Paper/Attention is not all you need]] |
| GPT-4 Can't Reason[^tp-gpt4] | 2023 | A position paper arguing that GPT-4 lacks reasoning ability, based on 21 hand-built problems; read it as one critical perspective, not a settled result | — |

## References & Useful Links

[^tp-seq2seq]: [Sutskever, Vinyals & Le (2014)](https://arxiv.org/abs/1409.3215) — Sequence to Sequence Learning with Neural Networks.
[^tp-bahdanau]: [Bahdanau, Cho & Bengio (2014)](https://arxiv.org/abs/1409.0473) — Neural Machine Translation by Jointly Learning to Align and Translate.
[^tp-aiayn]: [Vaswani et al. (2017)](https://arxiv.org/abs/1706.03762) — Attention Is All You Need.
[^tp-bert]: [Devlin et al. (2019)](https://arxiv.org/abs/1810.04805) — BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding.
[^tp-roberta]: [Liu et al. (2019)](https://arxiv.org/abs/1907.11692) — RoBERTa: A Robustly Optimized BERT Pretraining Approach.
[^tp-t5]: [Raffel et al. (2019)](https://arxiv.org/abs/1910.10683) — Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer.
[^tp-bart]: [Lewis et al. (2019)](https://arxiv.org/abs/1910.13461) — BART: Denoising Sequence-to-Sequence Pre-training.
[^tp-gpt3]: [Brown et al. (2020)](https://arxiv.org/abs/2005.14165) — Language Models are Few-Shot Learners.
[^tp-ln]: [Ba, Kiros & Hinton (2016)](https://arxiv.org/abs/1607.06450) — Layer Normalization.
[^tp-preln]: [Xiong et al. (2020)](https://arxiv.org/abs/2002.04745) — On Layer Normalization in the Transformer Architecture.
[^tp-nucleus]: [Holtzman et al. (2019)](https://arxiv.org/abs/1904.09751) — The Curious Case of Neural Text Degeneration.
[^tp-gqa]: [Ainslie et al. (2023)](https://arxiv.org/abs/2305.13245) — GQA: Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints.
[^tp-vllm]: [Kwon et al. (2023)](https://arxiv.org/abs/2309.06180) — Efficient Memory Management for Large Language Model Serving with PagedAttention.
[^tp-rag]: [Lewis et al. (2020)](https://arxiv.org/abs/2005.11401) — Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks.
[^tp-lost]: [Liu et al. (2023)](https://arxiv.org/abs/2307.03172) — Lost in the Middle: How Language Models Use Long Contexts.
[^tp-dong]: [Dong, Cordonnier & Loukas (2021)](https://arxiv.org/abs/2103.03404) — Attention is Not All You Need: Pure Attention Loses Rank Doubly Exponentially with Depth.
[^tp-gpt4]: [Arkoudas (2023), GPT-4 Can't Reason](https://arxiv.org/pdf/2308.03762v2) — Originally saved link; abstract rechecked 27 September 2026.
