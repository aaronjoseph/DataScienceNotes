Machine translation (MT) is the process of translating text or speech from one language to another using a computer. It is the task that motivated both attention and the [[Transformers|Transformer]], so it is a good lens for understanding [[Sequence Models|sequence-to-sequence models]].

## Approaches Over Time

| Approach | Core idea | Typical weakness |
|---|---|---|
| Rule-based | Hand-written grammars and bilingual dictionaries | Expensive to build; brittle outside the rules |
| Statistical, phrase-based | Learn phrase translation tables and reordering from parallel text | Many separately tuned components |
| Neural encoder–decoder | One network trained end to end to maximise translation quality[^bahdanau] | Early versions squeezed each sentence into one vector |
| Attention and Transformers | The decoder looks back at every source position | Needs large parallel corpora and compute |

### Why attention was introduced

Early neural systems encoded the source sentence into a fixed-length vector and decoded the translation from it.[^seq2seq] Bahdanau, Cho, and Bengio conjectured that this vector was a bottleneck and let the model soft-search for the source words relevant to each target word. Their alignments agreed well with intuition on English–French translation.[^bahdanau]

### The Transformer on translation

The original Transformer was evaluated on WMT 2014 English–German and English–French. It used a shared source–target subword vocabulary of about 37,000 tokens for English–German, and its big model reached 28.4 BLEU on that task.[^aiayn] A shared vocabulary lets names, numbers, and cognates be copied across languages as the same subword pieces.

## How a Neural Translation Model Works

1. **Tokenize** source and target with a subword vocabulary; see [[Tokenization]].
2. **Encode** the source sentence bidirectionally.
3. **Decode** the target one token at a time, using cross-attention over the source; see [[Encoder-Decoder Model (Transformers)]].
4. **Search** for a good output sequence, for example with beam search, rather than taking only the single most likely token each step.

## Evaluating Translations

BLEU (Papineni et al., 2002) scores a system translation by its n-gram overlap with one or more human reference translations, with a penalty for output that is too short.[^bleu] It is cheap and reproducible, but:

- A correct translation that uses different words from the reference scores lower.
- Scores depend on tokenization and the number of references, so compare only under the same setup.
- A higher BLEU does not guarantee that meaning, negation, or numbers were preserved.

Human evaluation remains the reference for quality, as with [[Search Evaluation|search evaluation]].

## Search Connections

- **Cross-lingual search:** translate the query into the document language, translate documents at index time, or use a multilingual embedding model.
- **Query translation errors are silent:** a mistranslated brand or size changes which documents can match, much like a bad [[Query Understanding#Query Rewriting|query rewrite]].
- **Keep identifiers untranslated:** model numbers, SKUs, and many brand names should pass through unchanged.

## Exercise

A user in Germany searches `wasserdichte Wanderschuhe Größe 42` (waterproof hiking shoes size 42) on a catalogue written in English.

1. Name two points in the pipeline where translation could be applied.
2. Which token should never be translated, and why?
3. How would you check that translation helped?

> [!example]- Exercise solution
> 1. Translate the **query** at request time, which is cheap and uses current models but gives one attempt with little context. Alternatively, translate **documents** at index time, which gives more context but requires reindexing when the model changes.
>
> 2. `42`, the size. It is an attribute value, not a word to translate; it should be parsed into a size filter. The same applies to model numbers.
>
> 3. Build a set of German queries with relevance judgments on English products. Compare recall and [[NDCG]] with and without translation, and inspect failures such as a mistranslated product type.

## References & Useful Links

[^seq2seq]: [Sutskever, Vinyals & Le (2014), Sequence to Sequence Learning with Neural Networks](https://arxiv.org/abs/1409.3215) — Fixed-vector LSTM encoder–decoder for translation.
[^bahdanau]: [Bahdanau, Cho & Bengio (2014), Neural Machine Translation by Jointly Learning to Align and Translate](https://arxiv.org/abs/1409.0473) — End-to-end neural translation, the fixed-length bottleneck, and soft alignment.
[^aiayn]: [Vaswani et al. (2017), Attention Is All You Need](https://arxiv.org/html/1706.03762v7) — Transformer translation data, shared vocabulary, and results.
[^bleu]: [Papineni et al. (2002), BLEU: a Method for Automatic Evaluation of Machine Translation](https://aclanthology.org/P02-1040/) — Bibliographic record and PDF. Only the record page was opened in this revision; the description of BLEU above is a standard summary, not checked against the full text.