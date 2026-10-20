---
note_type: concept
search_stage: foundations
tags:
  - ds-foundations
  - search-eng
---

## Overview

This is the hands-on companion to [[Transformers]]. A Transformer updates a token's vector by reading information from other tokens, then transforming the resulting features. Here, you will build those operations in Python, assemble a small encoder–decoder, and train it on an illustrative copy task.

Use `red running shoes` throughout: the token `shoes` can read information from `red` and `running`. Initially, the model's vectors are random. Training adjusts the parameters; the architecture alone does not understand language.

**Scope:** the components covered in the parent note, plus the practical details needed to connect them into working code: tokenization, embeddings, positions, attention, masks, heads, feed-forward layers, normalization, residuals, dropout, stacks, output probabilities, loss, optimization, generation, caching, and search applications. This is a foundations worksheet, not a reproduction of the paper's translation benchmark or a complete modern language-model implementation.

## How to Work Through This Worksheet

Run every `python` block **in order in the same notebook or Python session**. Later blocks reuse earlier definitions. The code uses CPU tensors and PyTorch 2.8.0. Each checkpoint asks you to predict or change something before moving on. The examples and exercises are original teaching examples; architecture background is in [[Transformers]], based on Vaswani et al.[^paper]

Create an isolated environment if PyTorch is not already installed:

```bash
python3 -m venv .venv-transformers
source .venv-transformers/bin/activate
python -m pip install 'torch==2.8.0'
```

Prerequisites: Python functions/classes, tensor shapes, matrix multiplication, [[Softmax Function]], and basic gradients. You do not need a pretrained model, a GPU, or a downloaded dataset.

### Shape vocabulary

| Symbol | Meaning | Main example |
|---|---|---|
| `B` | Batch size | 2 sequences |
| `T` | Query/target length | Varies |
| `S` | Key/source length | 4 positions |
| `D` | Model width | 16 features |
| `H` | Number of heads | 4 |
| `Dh` | Features per head | 4 |
| `V` | Vocabulary size | 11 tokens |
| `Dff` | Hidden width of feed-forward network | 32 |

`[B, T, D]` means one vector of `D` features for every position in every sequence. `@` multiplies matrices across their final two dimensions; preceding dimensions are batch dimensions.

```python
import math
import torch
from torch import nn
from torch.nn import functional as F

torch.manual_seed(7)
torch.set_num_threads(1)
torch.set_printoptions(precision=4, sci_mode=False)
D, H, DFF = 16, 4, 32
print("PyTorch:", torch.__version__)
```

## 1. Tokenization and Padding

[[Tokenization]] turns text into discrete symbols and then integer IDs. An ID is a lookup index, not a numeric measure of meaning. This deliberately simple whitespace tokenizer keeps the mechanics visible; real tokenizers often split words into subwords.

`<bos>` starts an output, `<eos>` ends it, `<pad>` equalizes batch lengths, and `<unk>` represents an unknown word. Right-padding lets the examples share a rectangular tensor.

```python
words = ["<pad>", "<bos>", "<eos>", "<unk>", "<mask>", "<sep>",
         "red", "running", "shoes", "blue", "boots"]
vocab = {word: i for i, word in enumerate(words)}
PAD, BOS, EOS, UNK, MASK, SEP = range(6)
V = len(vocab)

def tokenize(text):
    return [vocab.get(word, UNK) for word in text.lower().split()]

def batch_ids(texts):
    rows = [tokenize(text) + [EOS] for text in texts]
    width = max(map(len, rows))
    return torch.tensor([row + [PAD] * (width - len(row)) for row in rows])

src = batch_ids(["red running shoes", "blue boots"])
src_valid = src != PAD
print(src)        # [[6, 7, 8, 2], [9, 10, 2, 0]]
print(src_valid)  # Last position in the second row is False.
assert src.shape == (2, 4)
```

**Checkpoint:** tokenize `green shoes`. Which ID loses the distinction between `green` and every other unknown word? Why does padding need a mask even when its embedding is zero?

## 2. Token Embeddings

An [[Embeddings|embedding]] layer is a learned table with one vector per vocabulary item. The same token initially gets the same vector everywhere. Context is added by the subsequent layers.

```python
embedding = nn.Embedding(V, D, padding_idx=PAD)
x_tokens = embedding(src)
assert x_tokens.shape == (2, 4, D)
assert torch.equal(x_tokens[1, 3], torch.zeros(D))
print("Embedding table:", tuple(embedding.weight.shape))
print("Embedded batch:", tuple(x_tokens.shape))
```

`padding_idx` prevents ordinary embedding gradients from updating that row. It does **not** make later attention ignore padding: position encodings and other operations can make padded hidden vectors nonzero.

**Checkpoint:** compare `embedding(torch.tensor([6, 6]))`. Explain why both rows match before contextual processing.

## 3. Position Encodings

Attention needs information about order. This worksheet adds a fixed sine/cosine vector at each position and scales the token embedding as in the original architecture. The position values are buffers, not learned parameters.[^paper]

Inputs: zero-based position $p$, feature-pair index $i$, and even width $D$.

**Even features:**

$$
PE_{p,2i} = \sin\!\left(\frac{p}{10000^{2i/D}}\right)
$$

**Odd features:**

$$
PE_{p,2i+1} = \cos\!\left(\frac{p}{10000^{2i/D}}\right)
$$

**Combine token and position:**

$$
X_p = \sqrt{D}\,E[\mathrm{token}_p] + PE_p
$$

The sum keeps the feature width unchanged while making different positions distinguishable.

```python
class PositionEncoding(nn.Module):
    def __init__(self, d, max_len=64):
        super().__init__()
        assert d % 2 == 0
        positions = torch.arange(max_len).float().unsqueeze(1)
        frequencies = torch.exp(torch.arange(0, d, 2).float()
                                * (-math.log(10000.0) / d))
        pe = torch.zeros(max_len, d)
        pe[:, 0::2] = torch.sin(positions * frequencies)
        pe[:, 1::2] = torch.cos(positions * frequencies)
        self.register_buffer("pe", pe)

    def forward(self, x, offset=0):
        end = offset + x.size(1)
        if end > self.pe.size(0):
            raise ValueError("Sequence exceeds position buffer")
        return x + self.pe[offset:end].unsqueeze(0)

position = PositionEncoding(D)
x = position(x_tokens * math.sqrt(D))
print(PositionEncoding(4).pe[1:3])
# Approximately [[0.8415, 0.5403, 0.0100, 0.9999],
#                [0.9093, -0.4161, 0.0200, 0.9998]]
assert x.shape == x_tokens.shape
```

**Checkpoint:** inspect positions 0 and 1. Which dimensions change fastest? A fixed encoding does not by itself guarantee that a model generalizes to longer sequences.

## 4. Queries, Keys, and Values

A **query** asks what to read, a **key** provides a matchable description, and a **value** supplies the information to mix. These are learned projections of hidden vectors, not separately tokenized sentences.

```python
q_proj = nn.Linear(D, D, bias=False)
k_proj = nn.Linear(D, D, bias=False)
v_proj = nn.Linear(D, D, bias=False)
q, k, v = q_proj(x), k_proj(x), v_proj(x)
assert q.shape == k.shape == v.shape == (2, 4, D)
print("Projection parameters:", sum(p.numel() for p in q_proj.parameters()))
```

`nn.Linear` stores weights as `[output_features, input_features]`; internally it multiplies by the transposed weight. This is the same mapping as the parent's mathematical projection after accounting for storage convention.

**Checkpoint:** identify what is learned (`weight`) and what is recomputed for each input (`q`, `k`, `v`). Changing only `v` changes the mixed content but leaves the attention weights unchanged.

## 5. Scaled Dot-Product Attention

For one head, let queries have shape `[T, Dh]` and keys/values `[S, Dh]`. Scores and weights have shape `[T, S]`. Softmax runs over **keys**, the last dimension.

**Step 1 — scores:**

$$
S_{\mathrm{scores}} = \frac{QK^{\top}}{\sqrt{D_h}}
$$

**Step 2 — normalize allowed scores:**

$$
A = \operatorname{softmax}_{\mathrm{keys}}(S_{\mathrm{scores}} + M)
$$

**Step 3 — mix values:**

$$
Z = AV
$$

The mask $M$ contributes zero at allowed positions and negative infinity at blocked positions. Scaling helps keep scores from growing too large as the head width grows.[^paper]

```python
def attention(q, k, v, allowed=None):
    scores = q @ k.transpose(-2, -1) / math.sqrt(q.size(-1))
    if allowed is not None:
        # Our convention: True means a key is visible.
        if not allowed.any(dim=-1).all():
            raise ValueError("Every query needs at least one visible key")
        scores = scores.masked_fill(~allowed, float("-inf"))
    weights = torch.softmax(scores, dim=-1)
    return weights @ v, weights

# Reproduce the parent's hand-calculated example with identity projections.
toy = torch.tensor([[1., 0.], [0., 1.], [1., 1.]])
toy_out, toy_weights = attention(toy, toy, toy)
print("shoes weights:", toy_weights[2])
print("shoes output:", toy_out[2])
assert torch.allclose(toy_weights.sum(-1), torch.ones(3))
assert torch.allclose(toy_out[2], torch.tensor([0.7517, 0.7517]), atol=1e-4)
```

Expected: `shoes` assigns approximately `[0.2483, 0.2483, 0.5035]` and outputs `[0.7517, 0.7517]`. These are illustrative vectors, not measured linguistic relationships.

**Checkpoint:** replace the scale with `1` in a copy of the function. Observe how the distribution changes. Explain why a single head's weighted average does not mean the complete block is only an average.

## 6. Padding Masks and Causal Masks

A **padding mask** hides nonexistent key positions. A **causal mask** hides future positions. Combine them for decoder self-attention. Padding query rows may still have outputs; exclude those rows from losses and pooling.

```python
def key_mask(ids):
    return (ids != PAD)[:, None, None, :]  # [B, 1, 1, S]

def causal_mask(length):
    return torch.ones(length, length, dtype=torch.bool).tril()[None, None]

causal_out, causal_weights = attention(
    toy, toy, toy, torch.ones(3, 3, dtype=torch.bool).tril()
)
print("running causal weights:", causal_weights[1])
assert causal_weights[1, 2] == 0
assert torch.allclose(causal_out[1], torch.tensor([0.3302, 0.6698]), atol=1e-4)

allowed_src = key_mask(src)
assert allowed_src.shape == (2, 1, 1, 4)
```

PyTorch APIs do not all use the same Boolean mask convention. The functional scaled-dot-product attention API uses `True` for allowed positions; `nn.MultiheadAttention` Boolean masks use `True` for blocked positions. Check the API before reusing masks.[^sdpa][^mha]

**Checkpoint:** explain why merely shifting targets without a causal mask leaks answers during training. Why would an all-blocked row cause problems for softmax?

## 7. Multi-Head Attention and the Output Projection

Project to `D` features, reshape into `H` smaller heads, attend independently, then concatenate and mix the heads with an output projection. Each head can learn a different pattern; it is not assigned a fixed linguistic role.

```python
class MultiHeadAttention(nn.Module):
    def __init__(self, d=D, heads=H):
        super().__init__()
        assert d % heads == 0
        self.heads, self.dh = heads, d // heads
        self.q = nn.Linear(d, d, bias=False)
        self.k = nn.Linear(d, d, bias=False)
        self.v = nn.Linear(d, d, bias=False)
        self.out = nn.Linear(d, d, bias=False)

    def split(self, x):
        b, length, _ = x.shape
        return x.reshape(b, length, self.heads, self.dh).transpose(1, 2)

    def forward(self, query, context, allowed):
        q = self.split(self.q(query))
        k = self.split(self.k(context))
        v = self.split(self.v(context))
        z, weights = attention(q, k, v, allowed)
        b, _, t, _ = z.shape
        z = z.transpose(1, 2).contiguous().reshape(b, t, -1)
        return self.out(z), weights

mha = MultiHeadAttention()
contextual, head_weights = mha(x, x, key_mask(src))
assert contextual.shape == (2, 4, D)
assert head_weights.shape == (2, H, 4, 4)
assert torch.count_nonzero(head_weights[1, :, :, 3]) == 0

# Compare one head with PyTorch's implementation; dropout is explicitly off.
q_check, k_check, v_check = [torch.randn(1, 2, 3, 4) for _ in range(3)]
z_manual, _ = attention(q_check, k_check, v_check, causal_mask(3))
z_builtin = F.scaled_dot_product_attention(
    q_check, k_check, v_check, attn_mask=causal_mask(3), dropout_p=0.0
)
assert torch.allclose(z_manual, z_builtin, atol=1e-6)
```

**Checkpoint:** trace `[2, 4, 16]` through the split into `[2, 4, 4, 4]`. Here two axes happen to have the same size; name them before doing a transpose. Try `H=3`: why must this implementation reject it?

## 8. Position-Wise Feed-Forward Network

Attention mixes **tokens**. The feed-forward network mixes **features within each token**, using shared weights at every position. ReLU adds nonlinearity; without it, two affine layers collapse to one affine mapping.

```python
def make_ffn(d=D, hidden=DFF):
    return nn.Sequential(nn.Linear(d, hidden), nn.ReLU(), nn.Linear(hidden, d))

ffn = make_ffn()
y_ffn = ffn(x)
assert y_ffn.shape == x.shape
changed = x.detach().clone()
changed[0, 0] += 1
assert torch.allclose(ffn(changed)[0, 1:], y_ffn[0, 1:])
```

The assertion shows that changing one token does not directly affect other tokens through this sublayer. Later attention can propagate the change.

**Checkpoint:** count the two weight matrices separately from their biases. Why expand to `DFF` and then return to `D`?

## 9. Residual Connections, LayerNorm, and Dropout

A residual connection adds the update to the existing representation. [[Layer Normalization]] computes statistics over each token's features. [[Dropout - Neural Network|Dropout]] randomly zeroes features during training and rescales retained values; evaluation disables it.

Inputs: one token vector $x$, feature mean $\mu$, feature variance $\sigma^2$, learned scale $\gamma$, learned offset $\beta$, and positive stability constant $\epsilon$.

**Normalize and apply learned affine parameters:**

$$
\operatorname{LN}(x) = \gamma \odot \frac{x-\mu}{\sqrt{\sigma^2+\epsilon}} + \beta
$$

The statistics cover features, not other tokens or other batch examples. PyTorch uses the population variance for this operation.[^ln]

```python
norm = nn.LayerNorm(D)
residual = x + contextual
normalized = norm(residual)
mu = residual.mean(dim=-1, keepdim=True)
variance = residual.var(dim=-1, keepdim=True, unbiased=False)
manual = (residual - mu) / torch.sqrt(variance + norm.eps)
manual = manual * norm.weight + norm.bias
assert torch.allclose(normalized, manual, atol=1e-5)

drop = nn.Dropout(0.1)
drop.train()
print("Training dropout:", drop(torch.ones(12)))
drop.eval()
assert torch.equal(drop(torch.ones(12)), torch.ones(12))

branch = make_ffn()
post_ln = norm(x + branch(x))
pre_ln = x + branch(norm(x))
assert pre_ln.shape == post_ln.shape == x.shape
```

**Post-LN** normalizes after adding the residual; **Pre-LN** normalizes the sublayer input inside the residual branch. The complete model below uses Post-LN to match the parent's original architecture discussion. They are different computations, not interchangeable names.

**Checkpoint:** why must the update return `D` features? Does LayerNorm guarantee zero mean after a nontrivial learned scale and offset? Explain why `eval()` and disabling gradient recording are separate operations.

## 10. Encoder and Decoder Blocks

The encoder reads the entire nonpadding source. A decoder first reads its allowed target prefix, then uses **cross-attention** to read the encoder's final vectors. Decoder queries and encoder keys need not have the same sequence length.

```python
class EncoderBlock(nn.Module):
    def __init__(self, p=0.1):
        super().__init__()
        self.attn = MultiHeadAttention()
        self.ff = make_ffn()
        self.n1, self.n2 = nn.LayerNorm(D), nn.LayerNorm(D)
        self.drop = nn.Dropout(p)

    def forward(self, x, allowed):
        update, _ = self.attn(x, x, allowed)
        x = self.n1(x + self.drop(update))
        return self.n2(x + self.drop(self.ff(x)))

class DecoderBlock(nn.Module):
    def __init__(self, p=0.1):
        super().__init__()
        self.self_attn = MultiHeadAttention()
        self.cross_attn = MultiHeadAttention()
        self.ff = make_ffn()
        self.n1, self.n2, self.n3 = [nn.LayerNorm(D) for _ in range(3)]
        self.drop = nn.Dropout(p)

    def forward(self, x, memory, target_allowed, source_allowed):
        update, _ = self.self_attn(x, x, target_allowed)
        x = self.n1(x + self.drop(update))
        update, _ = self.cross_attn(x, memory, source_allowed)
        x = self.n2(x + self.drop(update))
        return self.n3(x + self.drop(self.ff(x)))

enc_block, dec_block = EncoderBlock(), DecoderBlock()
enc_block.eval()
dec_block.eval()
memory_demo = enc_block(x, key_mask(src))
target_demo = torch.randn(2, 3, D)
decoded_demo = dec_block(target_demo, memory_demo, causal_mask(3), key_mask(src))
assert decoded_demo.shape == (2, 3, D)
_, cross_weights = dec_block.cross_attn(target_demo, memory_demo, key_mask(src))
assert cross_weights.shape == (2, H, 3, 4)
```

**Checkpoint:** in `[B, H, T, S]` cross-attention weights, which axis is normalized? Why can the decoder read all valid source positions but not all target positions?

## 11. Stacking Blocks and Projecting to Vocabulary Logits

Each layer has its own parameters. `ModuleList` registers them so the optimizer can find them. The last linear layer maps each decoder vector to one score per vocabulary token. These scores are **logits**, not probabilities.

```python
class TinyTransformer(nn.Module):
    def __init__(self, layers=2, p=0.1):
        super().__init__()
        self.embedding = nn.Embedding(V, D, padding_idx=PAD)
        self.position = PositionEncoding(D)
        self.input_drop = nn.Dropout(p)
        self.encoders = nn.ModuleList([EncoderBlock(p) for _ in range(layers)])
        self.decoders = nn.ModuleList([DecoderBlock(p) for _ in range(layers)])
        self.lm_head = nn.Linear(D, V)

    def embed(self, ids):
        return self.input_drop(self.position(self.embedding(ids) * math.sqrt(D)))

    def encode(self, source):
        x = self.embed(source)
        for layer in self.encoders:
            x = layer(x, key_mask(source))
        return x

    def decode(self, target_in, memory, source):
        x = self.embed(target_in)
        allowed = key_mask(target_in) & causal_mask(target_in.size(1))
        for layer in self.decoders:
            x = layer(x, memory, allowed, key_mask(source))
        return self.lm_head(x)

    def forward(self, source, target_in):
        return self.decode(target_in, self.encode(source), source)

model = TinyTransformer()
assert model.encoders[0].attn.q.weight is not model.encoders[1].attn.q.weight
print("Trainable parameters:", sum(p.numel() for p in model.parameters()))
```

This teaching model uses two small layers, shared source/target embeddings, and an untied output projection. It omits some recipe details such as attention-weight dropout. It is not an exact reproduction of the original six-layer model.

**Checkpoint:** replace the list comprehension with repeated references to one block in a separate experiment. Why would that accidentally share parameters?

## 12. Teacher Forcing, Output Softmax, and Loss

For target `red running shoes <eos>`, feed `<bos> red running shoes` to the decoder. At each position, predict the next token. The causal mask allows all target-position losses to be computed in one pass without future-token leakage.

```python
# Copy task: the target text equals the source text.
target = src.clone()
target_in = torch.cat([torch.full((src.size(0), 1), BOS), target[:, :-1]], dim=1)
logits = model(src, target_in)
assert logits.shape == (2, 4, V)
probabilities = logits.softmax(dim=-1)
assert torch.allclose(probabilities.sum(-1), torch.ones(2, 4), atol=1e-6)

criterion = nn.CrossEntropyLoss(ignore_index=PAD)
loss = criterion(logits.reshape(-1, V), target.reshape(-1))
print("Initial loss:", loss.item())

# Show which per-token losses contribute to the mean.
per_token = F.cross_entropy(logits.reshape(-1, V), target.reshape(-1),
                            ignore_index=PAD, reduction="none").reshape_as(target)
assert per_token[1, 3] == 0
assert torch.allclose(loss, per_token.sum() / (target != PAD).sum())

smoothed_loss = F.cross_entropy(logits.reshape(-1, V), target.reshape(-1),
                                ignore_index=PAD, label_smoothing=0.1)
print("Smoothed loss:", smoothed_loss.item())
```

`CrossEntropyLoss` takes raw logits and integer target IDs; do not apply softmax first. With ignored padding targets and no class weights, its mean covers the valid target positions.[^ce]

**Attention softmax** normalizes over source/key positions. **Output softmax** normalizes over vocabulary entries. Label smoothing softens the target distribution; the library's uniform-mixture option is a demonstration, not a claim of exact equivalence to every historical smoothing implementation.

**Checkpoint:** there are seven nonpadding targets in this batch. Explain why dividing by eight would understate the mean loss. `<eos>` is a real target; `<pad>` is not.

## 13. Backpropagation and Optimization

The loss measures prediction error; backpropagation computes parameter gradients; the optimizer changes the parameters. Clearing gradients prevents accumulation from previous steps.

```python
optimizer = torch.optim.Adam(model.parameters(), lr=0.003)
model.train()
training_losses = []
for step in range(250):
    optimizer.zero_grad(set_to_none=True)
    logits = model(src, target_in)
    loss = criterion(logits.reshape(-1, V), target.reshape(-1))
    loss.backward()
    assert model.encoders[0].attn.q.weight.grad is not None
    torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
    optimizer.step()
    training_losses.append(loss.item())
print("First / last training loss:", training_losses[0], training_losses[-1])
```

This intentionally overfits two examples. Falling training loss demonstrates a working learning pipeline, not language understanding, generalization, retrieval quality, or translation performance. A real experiment needs held-out examples and a task-specific metric.

### Original learning-rate schedule as a separate exercise

The original recipe used Adam with warm-up followed by inverse-square-root decay.[^paper] Here `step` is a positive update count and `warmup` is the number of warm-up updates.

```python
def original_learning_rate(step, d_model=512, warmup=4000):
    if step < 1:
        raise ValueError("Use a one-based step")
    return d_model ** -0.5 * min(step ** -0.5, step * warmup ** -1.5)

print([original_learning_rate(s) for s in (1, 1000, 4000, 16000)])
# To try the paper's Adam settings in a NEW experiment:
# optimizer = torch.optim.Adam(model.parameters(), lr=1.0,
#                              betas=(0.9, 0.98), eps=1e-9)
# Before each optimizer.step(), set each param_group['lr'] using the function.
```

The copy-task loop deliberately uses a fixed learning rate for a short exercise. Do not interpret its training duration as a benchmark of the paper's schedule.

**Checkpoint:** train on one color and evaluate on a different one. What does training loss fail to tell you?

## 14. Autoregressive Generation

At inference, only `<bos>` is initially available. Predict one token, append it, and repeat until `<eos>` or a length limit. Encoder output can be computed once.

```python
@torch.no_grad()
def generate_one(model, source, max_new_tokens=10):
    assert source.size(0) == 1
    model.eval()
    memory = model.encode(source)
    generated = torch.tensor([[BOS]])
    for _ in range(max_new_tokens):
        next_logits = model.decode(generated, memory, source)[:, -1, :]
        # These control tokens are not valid outputs for this copy task.
        next_logits[:, [PAD, BOS, UNK, MASK, SEP]] = float("-inf")
        next_id = next_logits.argmax(dim=-1, keepdim=True)
        generated = torch.cat([generated, next_id], dim=1)
        if next_id.item() == EOS:
            break
    return generated[0].tolist()

for row in src:
    ids = generate_one(model, row.unsqueeze(0))
    print([words[i] for i in ids])
```

Greedy decoding picks the highest-scoring token each time. It need not find the most probable whole sequence. Sampling trades determinism for variation; beam search keeps several candidate prefixes. Generation is sequential even though training positions can be processed together.

**Checkpoint:** remove the stop condition in a copy and explain why the length limit still matters. Why can an early wrong prediction affect every later step?

## 15. Checks That Catch Silent Bugs

The following checks test information flow, not just tensor sizes. Evaluation mode removes dropout randomness.

```python
model.eval()
with torch.no_grad():
    # Changing a future decoder input must not change earlier logits.
    baseline = model(src, target_in)
    perturbed = target_in.clone()
    perturbed[:, -1] = vocab["boots"]
    future_changed = model(src, perturbed)
    assert torch.allclose(baseline[:, :-1], future_changed[:, :-1], atol=1e-5)

    # Extra source padding must not affect valid encoder outputs.
    extended = torch.cat([src, torch.full((2, 2), PAD)], dim=1)
    short_memory = model.encode(src)
    long_memory = model.encode(extended)[:, :src.size(1)]
    assert torch.allclose(short_memory[src_valid], long_memory[src_valid], atol=1e-5)

    assert torch.isfinite(baseline).all()
    predicted = baseline.argmax(-1)
    accuracy = (predicted[target != PAD] == target[target != PAD]).float().mean()
    print("Training-token accuracy:", accuracy.item())
```

**Checkpoint:** deliberately remove the causal mask and rerun the first check. Explain why a low loss with a leaking mask would be misleading.

## 16. Encoder-Only and Decoder-Only Variants

The architecture and the training objective are separate choices. An encoder can produce token labels, masked-token predictions, or pooled sequence representations. A decoder-only model uses causal blocks without encoder cross-attention.

### Encoder-only masked-token prediction

```python
masked_ids = src.clone()
masked_ids[0, 1] = MASK
mlm_targets = torch.full_like(src, -100)
mlm_targets[0, 1] = src[0, 1]  # Supervise only this masked position.
mlm_head = nn.Linear(D, V)
masked_states = model.encode(masked_ids)
mlm_logits = mlm_head(masked_states)
mlm_loss = F.cross_entropy(mlm_logits.reshape(-1, V), mlm_targets.reshape(-1),
                           ignore_index=-100)
print("Illustrative masked-token loss:", mlm_loss.item())
```

This illustrates a masked-language-model objective, not a complete [[BERT]] training recipe. The newly created head is untrained. See [[Encoder-Only Model (Transformers)]].

### Decoder-only next-token prediction

```python
class TinyCausalLM(nn.Module):
    def __init__(self):
        super().__init__()
        self.embedding = nn.Embedding(V, D, padding_idx=PAD)
        self.position = PositionEncoding(D)
        # EncoderBlock has the needed attention + FFN structure.
        # Its connectivity becomes causal through the supplied mask.
        self.blocks = nn.ModuleList([EncoderBlock(p=0.0) for _ in range(2)])
        self.output = nn.Linear(D, V)

    def forward(self, ids):
        x = self.position(self.embedding(ids) * math.sqrt(D))
        allowed = key_mask(ids) & causal_mask(ids.size(1))
        for block in self.blocks:
            x = block(x, allowed)
        return self.output(x)

causal_lm = TinyCausalLM()
lm_logits = causal_lm(target_in)
lm_loss = criterion(lm_logits.reshape(-1, V), target.reshape(-1))
assert lm_logits.shape == (2, 4, V)
```

This untrained model has no source encoder and no cross-attention. See [[Decoder-Only Model (Transformers)]] for architecture and serving context.

**Checkpoint:** explain which variant sees words on both sides of a masked token and which must never see its next-token answer.

## 17. KV Caching and Attention Cost

A key–value (KV) cache stores previous projected keys and values during causal generation. For one new token, compute its query/key/value, append its key/value, and attend to the prefix. It avoids repeatedly projecting old positions, but the new query still reads the growing prefix.

This isolated single-head example compares cached and full causal attention. It does **not** add a complete cache to `generate_one`.

```python
stream = torch.randn(1, 5, D)
cache_q = nn.Linear(D, D, bias=False)
cache_k = nn.Linear(D, D, bias=False)
cache_v = nn.Linear(D, D, bias=False)
with torch.no_grad():
    full, _ = attention(cache_q(stream), cache_k(stream), cache_v(stream),
                        torch.ones(5, 5, dtype=torch.bool).tril())
    ks, vs, outputs = [], [], []
    for t in range(stream.size(1)):
        current = stream[:, t:t+1]
        ks.append(cache_k(current))
        vs.append(cache_v(current))
        # Every cached key is from the current or an earlier position.
        z, _ = attention(cache_q(current), torch.cat(ks, dim=1), torch.cat(vs, dim=1))
        outputs.append(z)
    assert torch.allclose(torch.cat(outputs, dim=1), full, atol=1e-6)

for length in (128, 256, 512):
    entries = H * length * length  # One example; attention weights only.
    print(length, "tokens:", entries, "scores;", entries * 4 / 2**20, "MiB float32")
```

A full decoder cache needs separate state for every layer, correct absolute position offsets, and management of padding and finished sequences. Encoder–decoder cross-attention can also reuse projected encoder keys/values. A bidirectional encoder generally cannot append tokens this way without changing earlier outputs.

For sequence length $n$ and model width $D$, dense attention interactions cost $O(n^2D)$, projections add $O(nD^2)$, and the feed-forward network costs $O(nDD_{ff})$. Explicit attention weights use $O(BHn^2)$ storage. Optimized kernels can avoid storing that full matrix.[^sdpa] Our manual implementation materializes it for inspection.

**Checkpoint:** doubling sequence length quadruples the number of scores. Explain why doubling heads at fixed `D` changes explicit weight storage but does not double the combined head-feature width.

## 18. Connect the Components to Search

A **bi-encoder** independently creates query/document vectors. A **cross-encoder** jointly processes the pair so its tokens can interact. The following snippets demonstrate data flow only: the copy-trained encoder has not been trained for relevance.

### Bi-encoder pooling and similarity

```python
def mean_pool(states, ids):
    # In this illustration, exclude padding and all special tokens.
    keep = (ids >= 6).unsqueeze(-1)
    if not keep.any(dim=1).all():
        raise ValueError("Need at least one content token per sequence")
    return (states * keep).sum(1) / keep.sum(1)

query_ids = batch_ids(["red shoes"])
doc_ids = batch_ids(["red running shoes", "blue boots"])
with torch.no_grad():
    query_vec = F.normalize(mean_pool(model.encode(query_ids), query_ids), dim=-1)
    doc_vecs = F.normalize(mean_pool(model.encode(doc_ids), doc_ids), dim=-1)
    similarities = query_vec @ doc_vecs.T
print("Illustrative similarities, not relevance scores:", similarities)
```

Document vectors can be computed before a query arrives. Useful [[Dense Retrieval]] requires suitable training, pooling, and evaluation; an arbitrary Transformer vector is not automatically a good sentence embedding.

### Cross-encoder joint input and scoring head

```python
pair_ids = torch.tensor([[BOS] + tokenize("red shoes") + [SEP]
                         + tokenize("red running shoes") + [EOS]])
relevance_head = nn.Linear(D, 1)
pair_states = model.encode(pair_ids)
raw_score = relevance_head(pair_states[:, 0])
assert raw_score.shape == (1, 1)
print("Untrained joint score:", raw_score.item())
```

The first position can attend to both text segments. The separator marks their boundary; some architectures also use segment embeddings. This score needs relevance supervision and cannot be interpreted as a calibrated probability. See [[Cross-Encoder]] and [[Search Ranking]].

**Checkpoint:** for a 10-token query and 200-token document, ignoring special tokens, calculate the total joint attention scores and the cross-segment scores in both directions. Check your answer in the parent note's [[Transformers#Exercise|exercise]].

## Limitations and Common Pitfalls

- **Random or copy-trained vectors are not semantic evidence.** Inspecting weights shows computation, not a faithful explanation of a prediction.
- **All-masked rows are invalid here.** Keep at least one valid key. These examples assume right-padded sequences and a valid starting token.
- **Masking keys does not remove padded queries.** Also ignore padding in the objective and pooling.
- **Generation and training differ.** Teacher forcing uses correct prefixes; generation uses predictions.
- **Positions have limits.** This implementation has a 64-position buffer. Extending the buffer does not prove longer-context quality.
- **A mask does not eliminate dense computation here.** This code calculates scores before replacing blocked entries.
- **The examples target CPU.** A device-portable version must create masks and new tensors on the same device as its inputs.
- **Two examples cannot establish generalization.** Translation needs held-out sequence evaluation; search needs judged retrieval/ranking evaluation, separate from latency measurements.
- **Beyond this worksheet:** rotary positions, RMSNorm, gated feed-forward layers, grouped-query attention, quantization, and distributed training are further topics, not prerequisites for understanding this implementation.

## Verification Record

All 22 Python blocks were executed in order on CPU with Python 3.12 and PyTorch 2.8.0 on 20 October 2026. The attention arithmetic, built-in attention comparison, causal leakage check, padding invariance check, and cache equivalence assertions passed. The toy model reproduced both training sequences through EOS and reached 100% training-token accuracy; this is memorization of two examples, not a generalization result.

Internal links, heading targets, code fences, math delimiters, and footnote definitions were checked. Obsidian reading-view rendering remains unverified.

## Completion Checklist

- [ ] Explain the path from token IDs to contextual vectors without using the code.
- [ ] Label every attention tensor axis and reproduce the three-token result.
- [ ] Explain padding versus causal masks and pass the leakage checks.
- [ ] Build the multi-head and feed-forward modules from a blank cell.
- [ ] Explain residual paths, normalization placement, and train/eval dropout.
- [ ] Assemble encoder and decoder stacks with distinct layer parameters.
- [ ] Align shifted targets and explain the two different softmax operations.
- [ ] Train the toy model and distinguish memorization from generalization.
- [ ] Generate until EOS and explain what a KV cache saves.
- [ ] Explain the computation that can happen offline in a bi-encoder.

## References & Useful Links

[^paper]: [Vaswani et al. (2017), Attention Is All You Need](https://arxiv.org/html/1706.03762v7) — Original architecture, positional encoding, and optimization recipe; theory and original experimental results are summarized in [[Transformers]].
[^sdpa]: [PyTorch 2.8 — scaled_dot_product_attention](https://docs.pytorch.org/docs/2.8/generated/torch.nn.functional.scaled_dot_product_attention.html) — Functional attention masks, dropout behavior, and optimized implementation options.
[^mha]: [PyTorch 2.8 — MultiheadAttention](https://docs.pytorch.org/docs/2.8/generated/torch.nn.MultiheadAttention.html) — Boolean mask semantics differ from the functional attention API.
[^ln]: [PyTorch 2.8 — LayerNorm](https://docs.pytorch.org/docs/2.8/generated/torch.nn.LayerNorm.html) — Feature-wise normalization, affine parameters, epsilon, and variance convention.
[^ce]: [PyTorch 2.8 — CrossEntropyLoss](https://docs.pytorch.org/docs/2.8/generated/torch.nn.CrossEntropyLoss.html) — Raw logits, integer targets, ignored positions, reduction, and label smoothing.

Documentation checked on 20 October 2026 against the versioned PyTorch 2.8 pages. The snippets intentionally favor inspectable operations over optimized production implementations.
