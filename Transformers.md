---
note_type: concept
search_stage: foundations
tags:
  - "search-eng"
  - "ds-foundations"
---

## Overview

A **Transformer** is a neural-network architecture for turning a sequence of tokens into useful, context-dependent representations. Its central operation, **attention**, lets a token gather information from other allowed positions in the sequence. Feed-forward networks then transform that information, while residual connections and normalization help the layers work together.[^aiayn]

Start with `red running shoes`. An initial vector for `shoes` comes from a vocabulary lookup. After attention, its representation can include information from `red` and `running`. The model still has one vector per token; those vectors now describe the tokens **in context**. A task-specific output layer can use them to classify text, score a query–document pair, produce an embedding, or predict another token.

This note follows that example from text to vectors, through one attention calculation, into a complete Transformer. The small vectors, IDs, probabilities, and diagrams are illustrative unless explicitly identified as results from a paper.

![[Attachements/Transformers - Text to Context.svg]]

### How to read this note

1. **Build the picture:** read through [[#From Text to Token Vectors]], [[#Why Transformers Replaced Recurrent Models]], and [[#Positional Information]].
2. **Understand attention:** work through [[#Self-Attention Step by Step]] and [[#Worked Example with Three Tokens]]. Read a matrix row as “where this query position reads from.”
3. **Assemble the model:** continue with [[#Attention Masks and Cross-Attention]], [[#Multi-Head Attention]], and [[#The Rest of a Transformer Block]].
4. **Connect it to a task:** read [[#Three Architecture Families]], [[#Training and Generation]], and [[#Search Connections]].
5. **Revise actively:** run [[#A Small Runnable Attention Example]] and attempt [[#Exercise]].

## Prerequisites

The essential mathematics is modest:

- A **vector** is a list of numbers describing one item. A **matrix** stacks vectors into rows or columns.
- A **dot product** multiplies matching coordinates and adds the results. Attention uses it to score a query–key match. [[Cosine Similarity]] explains the related normalized comparison.
- **Matrix multiplication** performs many such combinations at once.
- [[Softmax Function|Softmax]] converts a row of scores into positive weights that sum to one; masked positions can receive zero weight.

[[Tokenization]] and [[Embeddings]] explain the input representation. [[Layer Normalization]] and [[Dropout - Neural Network|dropout]] provide more detail on supporting components, but their roles are introduced below before they are needed.

## From Text to Token Vectors

### 1. Tokenization decides what the positions are

A model processes **tokens**, which may be words, subwords, characters, or other vocabulary units. For the running example, assume three tokens:

`[red, running, shoes]`

A real tokenizer may split the same text differently and may insert special tokens. Consequently, sequence length counts **tokens, not words**. Use the tokenizer associated with the model; the vocabulary is part of its input contract. See [[Tokenization#Subword Tokenizers for Transformers|subword tokenization]].

### 2. Token IDs select embedding rows

Suppose the three vocabulary IDs are `[17, 42, 91]`. These arbitrary integers identify entries; ID 91 is not semantically “larger” than ID 17.

An **embedding table** contains a learned vector for each vocabulary entry. Looking up the IDs produces three vectors. The table belongs to the model's learned parameters; it is different from the input-specific vectors that change from sentence to sentence.

With three tokens and an illustrative vector width of four, the input representation has shape $3 \times 4$. A batch of $B$ equally padded sequences has shape $B \times n \times d_{\text{model}}$.

The initial lookup vector for a vocabulary entry is reused whenever that entry occurs. Later Transformer layers produce its context-dependent representation. This is why the same token can end up with different vectors in different sentences.

### 3. Preserve one row per position

Attention normally updates every token row; it does not automatically compress a sentence into one vector. A classification head might use a designated token, while an embedding model might pool several rows. The correct choice depends on training. See [[Encoder-Only Model (Transformers)#Pooling: From Token Vectors to One Vector|pooling methods]].

Before these rows enter the first block, the original Transformer adds positional information. That supplies something vocabulary lookup alone does not encode: where a token occurs.

## Why Transformers Replaced Recurrent Models

The original work focused on sequence-to-sequence tasks such as [[Machine Translation]]. Its motivation was to remove a computational bottleneck in [[RNN|recurrent networks]] and [[LSTM|LSTMs]], rather than to establish that recurrence is unsuitable for every task.[^aiayn]

A recurrent model updates a hidden state one position at a time. Position 3 depends on the state produced at position 2, which depends on position 1. This creates:

- **A sequential dependency during training:** positions in one sequence cannot all compute their recurrent states independently.
- **Long routes between distant positions:** information must pass through intermediate states, making long-range dependencies harder to learn.

Earlier translation attention let a recurrent decoder consult different encoder states instead of relying on one fixed-length summary.[^bahdanau] The Transformer went further: self-attention supplies direct interactions between allowed token positions, and the sequence operations can be expressed as large matrix computations.

For `red running shoes`, the update at `shoes` can read `red` directly in one attention layer. It need not receive that information through a chain of recurrent updates.

The paper describes a constant maximum interaction-path length for full self-attention, compared with a path that grows with sequence length for recurrence.[^aiayn] “Constant path length” describes the route between positions; it does **not** mean constant computational cost. Dense attention still compares many token pairs. Standard autoregressive generation also retains a dependency between successive output tokens.

## Notation

The equations below describe **one sequence**, omitting the batch dimension and, initially, the head dimension.

| Symbol | Meaning |
|---|---|
| $n$ | Number of input token positions |
| $d_{\text{model}}$ | Features in each block's token representation |
| $X$ | Matrix of token representations; shape $n \times d_{\text{model}}$ |
| $Q$, $K$, $V$ | Queries, keys, and values for one attention head |
| $d_k$, $d_v$ | Widths of that head's keys/queries and values |
| $W_Q$, $W_K$, $W_V$ | Learned projection matrices |
| $S$, $A$, $M$ | Scaled scores, attention weights, and additive mask |
| $Z$ | Output of one attention head |
| $h$ | Number of heads |
| $W^O$ | Learned projection after combining heads |
| $d_{ff}$ | Hidden width of the feed-forward network |

A **parameter** is learned and then reused across inputs. An **activation**, such as a query vector or attention matrix, is computed for the current input. Keeping these separate helps explain what training changes.

## Positional Information

Unmasked self-attention without positional information cannot distinguish order simply from which vocabulary vectors are present. If the input rows are permuted, the output rows are permuted in the same way: the operation is **permutation-equivariant**.

A causal mask introduces an order-dependent connectivity pattern. The original model additionally supplies explicit positional encodings to both encoder and decoder inputs.[^aiayn]

### Adding position to an embedding

Let $E$ contain the token embedding rows and $PE$ contain position vectors of the same shape. In the original model, the input before dropout is:

$$
X^{(0)} = \sqrt{d_{\text{model}}}\,E + PE
$$

The scaling is part of the original embedding recipe. At a given position, token identity and position contribute to the same vector. Adding rather than concatenating keeps its width at $d_{\text{model}}$.

Position is added at the bottom of the original stack, rather than re-added before every attention layer. Later layers receive representations in which content and position have already interacted.

### Sinusoidal encodings

For zero-based position $pos$ and dimension-pair index $i$, the original fixed encodings are:

$$
PE_{(pos,\,2i)} = \sin\!\left(\frac{pos}{10000^{2i/d_{\text{model}}}}\right)
$$

$$
PE_{(pos,\,2i+1)} = \cos\!\left(\frac{pos}{10000^{2i/d_{\text{model}}}}\right)
$$

Each sine/cosine pair changes at a different rate. The vector therefore marks a position using several frequencies.

**Example inputs:** use $d_{\text{model}}=4$ and inspect position indices 1 and 2.

**Step 1 — position index 1.**

$$
PE_1 \approx [0.8415,\ 0.5403,\ 0.0100,\ 1.0000]
$$

**Step 2 — position index 2.**

$$
PE_2 \approx [0.9093,\ -0.4161,\ 0.0200,\ 0.9998]
$$

The first pair changes quickly; the second changes slowly. The original paper found similar translation results with learned positional embeddings.[^aiayn] [[BERT]] uses learned absolute positions. Other architectures use other position schemes; neither sinusoidal encodings nor attention alone guarantee reliable behavior at arbitrary sequence lengths.

## Self-Attention Step by Step

**Self-attention** means that queries, keys, and values are derived from the same sequence of representations. It does not mean a token reads only itself.

For the query position `shoes`:

- The **query** represents the features used to look for useful context.
- Each **key** represents features against which that query is compared.
- Each **value** contains information that can be passed into the update.

“Looking for” is an analogy. These are learned numerical projections, not explicit questions written in English. An attention query is also different from the user's search query.

![[Attachements/Attention - Flow.svg]]

### 1. Project each token into a query, key, and value

Apply three learned linear projections to $X$:

$$
Q = XW_Q
$$

$$
K = XW_K
$$

$$
V = XW_V
$$

Within one head and layer, the same projection matrices are applied to every position. Different input rows produce different query, key, and value rows. The original architecture gives different heads and layers separate projection parameters.

| Matrix | Shape | Job |
|---|---|---|
| $W_Q$, $W_K$ | $d_{\text{model}} \times d_k$ | Map token features into a matching space |
| $W_V$ | $d_{\text{model}} \times d_v$ | Map token features into a content space |
| $Q$, $K$ | $n \times d_k$ | One query and key per position |
| $V$ | $n \times d_v$ | One value per position |

Using separate keys and values lets the network learn different features for **matching** and **information transfer**. Queries and keys must have compatible widths for their dot product; value width can differ.

### 2. Score every query against every key

Compute all query–key dot products and scale them:

$$
S = \frac{QK^{\top}}{\sqrt{d_k}}
$$

The result has shape $n \times n$. Row $i$ belongs to query position $i$; column $j$ belongs to key position $j$. Thus, $S_{ij}$ is a learned compatibility score for that directed interaction. It is not a human relevance judgment.

The transpose is what lets every query row meet every key row. A dot product here is not necessarily cosine similarity: the vectors are not required to have unit length.

**Why divide by key width's square root?** Under the paper's illustrative assumption of independent, zero-mean, unit-variance query/key components, larger key width makes raw dot products more variable. Large differences between scores can make softmax highly concentrated and its gradients small. The scaling controls that tendency.[^aiayn]

For example, a width of 64 gives a scaling divisor of 8. This is a scale-control argument, not a guarantee that learned scores always have unit variance.

### 3. Mask disallowed positions and normalise

Add a mask before softmax:

$$
A = \operatorname{softmax}_{\text{keys}}(S + M)
$$

The mask contains zero for allowed keys and negative infinity for blocked keys. Examples include padding positions and future positions in a causal decoder.

Softmax is applied **separately across each row**. A score becomes large or small relative to the other allowed scores for that query. It is not normalized across the whole matrix.

For an individual weight, with key index $r$ in the denominator:

$$
a_{ij} = \frac{\exp(S_{ij}+M_{ij})}
{\sum_{r=1}^{n}\exp(S_{ir}+M_{ir})}
$$

Every row needs at least one allowed key for this expression to be defined. For numerical stability, implementations can subtract the row's largest finite score before exponentiating; the normalized weights remain unchanged. [[Softmax Function]] explains why.

An encoder's weights need not be symmetric. Token $i$ can read heavily from token $j$ without the reverse interaction having the same weight.

### 4. Mix the values

For query position $i$, combine the value rows using that query's weights:

$$
z_i = \sum_{j=1}^{n} a_{ij}v_j
$$

For all query positions together:

$$
Z = AV
$$

$Z$ has shape $n \times d_v$. The operation produces one output vector per query position, rather than one output for the entire sentence.

The complete operation is masked scaled dot-product attention:[^aiayn]

$$
\operatorname{Attention}(Q,K,V)
= \operatorname{softmax}_{\text{keys}}\!\left(
\frac{QK^{\top}}{\sqrt{d_k}}+M
\right)V
$$

Before attention dropout and the output projection, each row is a weighted average of **projected value vectors**. The whole block also includes residual additions and nonlinear transformations, so it is more than averaging raw embeddings.

## Worked Example with Three Tokens

This example isolates the mechanics. Its coordinates do not encode real attributes such as color or footwear type, and its weights are not measurements from a trained language model.

### Inputs and assumptions

- Token order: `red`, `running`, `shoes`.
- One head, with $d_k=d_v=2$.
- No positional contribution, biases, dropout, or output projection.
- Initially, all three positions can attend to each other.
- Identity query, key, and value projections:

$$
W_Q = W_K = W_V = I
$$

The input matrix is:

$$
X = \begin{bmatrix}
1&0\\
0&1\\
1&1
\end{bmatrix}
$$

Here the rows of $Q$, $K$, and $V$ equal the rows of $X$ because of the identity projections.

### Step 1 — calculate all raw matches

$$
QK^{\top} = XX^{\top} =
\begin{bmatrix}
1&0&1\\
0&1&1\\
1&1&2
\end{bmatrix}
$$

For instance, the `shoes` query has its largest raw match with the `shoes` key. The setup permits self-attention on the diagonal; “self” does not require excluding a token's own position.

### Step 2 — scale the scores

The divisor is $\sqrt{2}$, approximately $1.4142$:

$$
S \approx
\begin{bmatrix}
0.7071&0&0.7071\\
0&0.7071&0.7071\\
0.7071&0.7071&1.4142
\end{bmatrix}
$$

We will now follow the last row, belonging to `shoes`.

### Step 3 — exponentiate the shoes row

$$
\exp([0.7071,\ 0.7071,\ 1.4142])
\approx [2.0281,\ 2.0281,\ 4.1133]
$$

These are positive scores, but they do not yet sum to one.

### Step 4 — normalize the shoes row

$$
a_{\text{shoes}}
\approx \frac{[2.0281,\ 2.0281,\ 4.1133]}{8.1695}
\approx [0.2483,\ 0.2483,\ 0.5035]
$$

The `shoes` query places about half its weight on its own value and splits the remainder between `red` and `running`. All printed values are rounded.

### Step 5 — combine the values

Using additional digits to keep rounding from affecting the displayed output:

$$
z_{\text{shoes}}
\approx 0.248255[1,0]
+0.248255[0,1]
+0.503490[1,1]
\approx [0.7517,\ 0.7517]
$$

This is an updated feature vector, not a token prediction or class probability. It includes contributions from the context.

### Step 6 — inspect the full attention matrix

Performing the same row-wise normalization for all positions gives:

$$
A \approx
\begin{bmatrix}
0.4011&0.1978&0.4011\\
0.1978&0.4011&0.4011\\
0.2483&0.2483&0.5035
\end{bmatrix}
$$

![[Attachements/Attention - Worked Example.svg]]

Each row sums to one before rounding. Notice the unequal reverse directions: `red` reads from `shoes` with weight about 0.4011, while `shoes` reads from `red` with weight about 0.2483. Even though the raw score matrix in this simplified example is symmetric, row-wise normalization need not preserve symmetry.

### Step 7 — inspect all updated vectors

$$
Z = AV \approx
\begin{bmatrix}
0.8022&0.5989\\
0.5989&0.8022\\
0.7517&0.7517
\end{bmatrix}
$$

All three token rows have been updated in one matrix operation. They still have two features each.

### Causal case — prevent running from seeing shoes

Now use the same inputs in a causal setting. The query at `running`, position 2, can read `red` and itself, but cannot read the later `shoes` position.

**Step 1 — mask the forbidden score.**

$$
S_{\text{running},:}+M_{\text{running},:}
= [0,\ 0.7071,\ -\infty]
$$

**Step 2 — normalize the remaining scores.**

$$
a_{\text{running}}^{\text{causal}}
\approx [0.3302,\ 0.6698,\ 0]
$$

**Step 3 — combine the allowed values.**

$$
z_{\text{running}}^{\text{causal}}
\approx 0.3302[1,0]+0.6698[0,1]
= [0.3302,\ 0.6698]
$$

The unmasked output for `running` was approximately $[0.5989,\ 0.8022]$. Removing the future key changes the distribution over the allowed keys; it does not merely zero out one contribution after the original softmax.

## Attention Masks and Cross-Attention

![[Attachements/Attention - Patterns.svg]]

The diagram shows **allowed connections**, not attention strengths. Three distinctions matter:

- **Bidirectional self-attention:** each real input position can read other real input positions on both sides.
- **Causal self-attention:** position $i$ can read positions up to and including $i$. The model's training targets are shifted so it must predict a token it cannot already read.
- **Cross-attention:** queries come from one sequence of representations; keys and values come from another. In the original encoder–decoder model, decoder states query the final encoder output.[^aiayn]

### Padding and causal masking solve different problems

A padding mask prevents artificial padding tokens from contributing as keys. A causal mask prevents future information from leaking into predictions. A padded causal batch can require both.

Masking padding keys does not automatically remove padded query rows from the output or from a training loss. Pooling and loss calculations need the corresponding valid-position handling.

### Why cross-attention can be rectangular

Suppose there are $m$ decoder query positions and $n$ encoder source positions. Each decoder position compares with each source key, so the attention matrix has shape $m \times n$. Its output still has one row per query.

For example, three decoder positions reading five source positions produce a $3 \times 5$ weight matrix. Source and target lengths do not have to match. See [[Encoder-Decoder Model (Transformers)#Shapes in cross-attention|cross-attention shapes]].

## Multi-Head Attention

One head produces one distribution over keys for each query. **Multi-head attention** lets the model form several such mixtures in different learned projection spaces, then combine them.[^aiayn]

For self-attention, head $i$ projects directly from the shared input $X$:

$$
\operatorname{head}_i =
\operatorname{Attention}(XW_i^Q,\ XW_i^K,\ XW_i^V)
$$

The outputs are concatenated along the feature dimension and projected:

$$
\operatorname{MultiHead}(X) =
\operatorname{Concat}(\operatorname{head}_1,\ldots,\operatorname{head}_h)W^O
$$

![[Attachements/Attention - Multi-Head.svg]]

**Original base-model inputs:** model width 512 and eight heads.

**Step 1 — find each head's width.**

$$
d_k=d_v=\frac{512}{8}=64
$$

**Step 2 — concatenate the outputs.**

$$
8 \times 64 = 512
$$

The final projection mixes information across those 512 features. Eight heads do not mean eight full-width 512-feature attention calculations; the smaller per-head widths keep the main arithmetic comparable to one full-width head.

A head might become sensitive to a particular relationship, but roles such as “syntax head” and “meaning head” are not assigned in advance or guaranteed. The original paper's attention visualizations suggest useful patterns; they do not prove complete explanations of the final prediction.

In its English–German development-set ablation, a single head was 0.9 BLEU worse than the best setting, while too many heads also reduced quality.[^aiayn] This is evidence from that setup, not a rule that increasing head count improves every model.

## The Rest of a Transformer Block

Attention is the part that communicates **across positions**. A complete block also transforms each position's features and provides routes for the previous representation to survive.

| Component | Main role | Original base setting |
|---|---|---|
| Multi-head attention | Mix information across allowed positions | Eight heads |
| Feed-forward network | Nonlinear feature transformation at each position | Inner width 2048 |
| Residual connection | Add a sublayer's input back to its output | Around each sublayer |
| [[Layer Normalization]] | Normalize features within each token row | After residual addition |
| [[Dropout - Neural Network\|Dropout]] | Regularize training | Rate 0.1 |

### Feed-forward networks transform the mixed information

The original position-wise feed-forward network is a small **multi-layer perceptron (MLP)**. It has two linear transformations with a rectified linear unit (**ReLU**) nonlinearity between them:

$$
\operatorname{FFN}(x)
=\max(0,\ xW_1+b_1)W_2+b_2
$$

Here $x$ is one token row. The first transformation expands the feature width from $d_{\text{model}}$ to $d_{ff}$; the second returns it to $d_{\text{model}}$. The nonlinearity makes this more expressive than two consecutive linear maps alone.

“Position-wise” means the same network is applied separately to every row in that layer. It does not mix token positions directly, but it operates on representations that attention has already contextualized.

### Residual connections preserve an update route

A residual connection adds the incoming representation to the sublayer's update. The layer can modify a representation without requiring the sublayer to reconstruct all of it.

The original Transformer normalizes after that addition. Omitting dropout from the notation:

$$
x_{\text{out}}
=\operatorname{LayerNorm}(x+\operatorname{Sublayer}(x))
$$

This arrangement is **Post-LN**. **Pre-LN** instead normalizes the sublayer input before computing its update; see [[Layer Normalization#Where the Normalisation Sits|normalization placement]]. The distinction affects optimization and should be preserved when describing or implementing a specific architecture.[^preln]

### Layer normalization controls feature scale

LayerNorm computes statistics across the features of **one token row**, then applies learned scaling and shifting. It does not average token representations across the sequence or use the other examples in a batch to calculate those statistics.

Normalization helps control the values passed through a deep stack. It does not by itself preserve differences between tokens that have already become identical. The linked [[Layer Normalization]] note provides the formula and a worked calculation.

### Stacking blocks builds on contextual representations

A later attention layer receives representations that already include context from earlier layers. Its matching scores can therefore depend on richer combinations of input information.

Depth supplies repeated opportunities to mix and transform features. It does not guarantee that each layer corresponds to a clean linguistic stage. The complementary roles of attention, residuals, and feed-forward networks are investigated in [[Research_Paper/Attention is not all you need]].

### Where the parameters live

**Inputs:** one original base encoder layer, $d_{\text{model}}=512$ and $d_{ff}=2048$. Ignore biases and normalization parameters.

**Step 1 — count attention projection weights.** There are query, key, value, and output projections:

$$
4 \times 512^2 = 1{,}048{,}576
$$

**Step 2 — count feed-forward weights.**

$$
2 \times 512 \times 2048 = 2{,}097{,}152
$$

The feed-forward network contains about two-thirds of these encoder-layer weights. A decoder layer also has cross-attention projections, and the whole model has embedding and output parameters. This fraction therefore does not describe every layer or the entire model.

## Three Architecture Families

The same building blocks support different information-flow patterns. Architecture specifies the structure; a training objective teaches a particular use of that structure.

| Family | Information flow | Common training objective | Examples or uses |
|---|---|---|---|
| [[Encoder-Only Model (Transformers)\|Encoder-only]] | Bidirectional input self-attention | Masked-token prediction | [[BERT]], [[RoBERTa]], classification and scoring |
| [[Decoder-Only Model (Transformers)\|Decoder-only]] | Causal self-attention | Next-token prediction | GPT-style [[Language Model\|language models]] |
| [[Encoder-Decoder Model (Transformers)\|Encoder–decoder]] | Bidirectional source encoder; causal target decoder with cross-attention | Predict an output sequence given an input | Translation and rewriting |

These are common configurations, not exclusive lists of possible tasks. For example, an encoder can support a relevance classifier, and a decoder's representations can also be adapted for classification.

BERT is an encoder model pretrained to use left and right context.[^bert] A decoder-only language model restricts visibility so predictions depend on the available prefix. An encoder–decoder keeps source and target representations in separate stacks.

### The original encoder–decoder end to end

![[Attachements/Attention - Transformer Architecture.svg]]

Read the original architecture as two connected computations:[^aiayn]

1. **Encoder:** source embeddings plus positions enter six encoder layers. Each layer has self-attention followed by a feed-forward network, with residual addition and normalization around both sublayers.
2. **Decoder:** shifted target embeddings plus positions enter six decoder layers. Each layer has causal self-attention, cross-attention to the final encoder output, and a feed-forward network, again with residual addition and normalization.
3. **Output:** a linear projection turns each final decoder row into vocabulary logits. A vocabulary softmax converts those logits into next-token probabilities.

The six layers share the same structural design but have separate learned parameters. Encoder output supplies keys and values to each decoder cross-attention sublayer; the decoder sublayer's current input supplies its queries.

The **attention softmax** normalizes over key positions. The **output softmax** normalizes over vocabulary entries. They solve different problems, even though both use softmax.

## Training and Generation

### Training supplies known earlier targets

**Teacher forcing** means using the correct earlier target tokens as decoder inputs during training. For an illustrative target `red running shoes <eos>`, shift the input right:

| Position | Decoder input token | Allowed target prefix | Token to predict |
|---|---|---|---|
| 1 | `<s>` | `<s>` | `red` |
| 2 | `red` | `<s> red` | `running` |
| 3 | `running` | `<s> red running` | `shoes` |
| 4 | `shoes` | `<s> red running shoes` | `<eos>` |

`<s>` and `<eos>` denote illustrative start and end tokens; exact special tokens depend on the model.

The input tokens are all available in a training example, but the causal mask prevents a position from reading future target information. All target-position losses can consequently be computed in one forward pass through the decoder. Dependencies between layers still remain.

In an encoder–decoder, the decoder can also read the entire encoded source through cross-attention. See [[Encoder-Decoder Model (Transformers)#Training with Teacher Forcing|teacher forcing in a query-rewrite example]].

### The loss trains vocabulary predictions

For a target of length $T$, let $y_t$ be its token at position $t$, $y_{<t}$ the earlier target tokens, $s$ the source sequence, and $\theta$ the model parameters. An unsmoothed token-average negative log-likelihood is:

$$
\mathcal{L}
=-\frac{1}{T}\sum_{t=1}^{T}
\log p_\theta(y_t\mid y_{<t},s)
$$

This is [[Cross Entropy Loss|cross-entropy]] against the target tokens. Padding positions are excluded from the average. A decoder-only language model uses its available prefix without a separate encoder source.

**Illustrative inputs:** the probabilities assigned to the four correct target tokens are `[0.6, 0.5, 0.8, 0.4]`.

**Step 1 — calculate the average loss using natural logarithms.**

$$
\mathcal{L}
=-\frac{\ln(0.6)+\ln(0.5)+\ln(0.8)+\ln(0.4)}{4}
\approx 0.5859
$$

A low probability for the correct token raises the loss. Backpropagation uses that loss to update embeddings, projections, feed-forward weights, and other trainable parameters. The attention matrices themselves are recomputed activations, not stored learned tables for each sentence.

The original model additionally used label smoothing, so its training target distribution differs from the unsmoothed teaching example above.[^aiayn]

### Generation uses the model's own earlier outputs

At inference, correct future tokens are unavailable. In standard autoregressive generation:

1. Process the source or prompt and available target prefix.
2. Compute vocabulary logits for the next output position.
3. Choose a token using a decoding rule, such as greedy selection, sampling, or beam search.
4. Append the chosen token and continue until an end condition or length limit.

An early prediction changes the context for later predictions. This differs from training on correct prefixes.

A **key–value (KV) cache** stores earlier keys and values in a causal decoder so later steps can reuse them. It saves repeated work; the new query still needs to interact with its allowed history. The cache grows with the retained context and does not make long-context generation free. See [[Decoder-Only Model (Transformers)#Serving and the KV Cache|KV caching]] and [[Decoder-Only Model (Transformers)#Decoding Strategies|decoding strategies]].

## Attention Is All You Need: What the Paper Introduced

**Paper:** *Attention Is All You Need* — Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N. Gomez, Łukasz Kaiser, and Illia Polosukhin, 2017.[^aiayn]

Attention had already been used with recurrent translation models. This paper introduced the Transformer as a complete encoder–decoder architecture that removed recurrent and convolutional sequence-processing layers, using attention for interactions between sequence positions.

Its main contributions combine:

- Scaled dot-product attention implemented with matrix operations.
- Multiple learned attention heads.
- Positional information without recurrent processing.
- Encoder and decoder stacks with feed-forward networks, residuals, and normalization.
- A training and decoding setup that demonstrated strong translation results.

The title's “all” concerns replacing recurrence and convolution as sequence-modeling mechanisms. The architecture still includes substantial computation outside attention.

*Attention is Not All You Need* is a separate 2021 paper about rank collapse in pure attention networks.[^dong] Its claims and experimental boundaries are explained in [[Research_Paper/Attention is not all you need]]. It does not negate the 2017 architecture's results.

### Attention reading path in this vault

- **Core calculation:** [[#Self-Attention Step by Step]] → [[#Worked Example with Three Tokens]] → [[#Multi-Head Attention]].
- **Visibility:** [[#Attention Masks and Cross-Attention]], [[Decoder-Only Model (Transformers)#Causal Masking|causal masking]], and [[Encoder-Decoder Model (Transformers)#Shapes in cross-attention|cross-attention dimensions]].
- **Supporting mechanisms:** [[#The Rest of a Transformer Block]] and [[Layer Normalization#Where the Normalisation Sits|normalization placement]].
- **Pure-attention analysis:** [[Research_Paper/Attention is not all you need#Intuition|token-uniformity intuition]] and [[Research_Paper/Attention is not all you need#Evidence|experimental evidence]].
- **Broader papers:** [[Transformer Papers]].

## How the Original Model Was Trained

The original English–German setup used WMT 2014 data with about 4.5 million sentence pairs and a shared byte-pair vocabulary of about 37,000 tokens.[^aiayn]

| Choice | Original setting |
|---|---|
| Base architecture | Six encoder and six decoder layers; model width 512 |
| Attention | Eight heads; per-head key and value width 64 |
| Feed-forward hidden width | 2048 |
| Optimizer | Adam; $\beta_1=0.9$, $\beta_2=0.98$ |
| Learning-rate schedule | 4,000 warm-up steps, then inverse-square-root decay |
| Regularization | Base dropout 0.1; label smoothing 0.1 |
| Training hardware | Eight NVIDIA P100 GPUs |

The warm-up phase increases the learning rate before the decay phase. Label smoothing reduces confidence in the exact training labels; the paper reports worse perplexity but improved translation BLEU. These choices belong to the original recipe, rather than defining every Transformer.

On English–German `newstest2014`, Table 2 reports:

| Configuration | Training steps | Approximate training time | BLEU |
|---|---|---|---|
| Base | 100,000 | 12 hours | 27.3 |
| Big | 300,000 | 3.5 days | 28.4 |

BLEU, **Bilingual Evaluation Understudy**, compares generated translations with references. The reported results also involve checkpoint averaging and beam search. They measure the complete translation system in that evaluation setup, rather than isolating the benefit of one attention operation.

The big model also differs in capacity; its extra training time is not an experiment that changes only the number of steps. These historical scores should not be treated as universal performance guarantees.

## A Small Runnable Attention Example

This Python example reproduces the numerical forward pass using only the standard library. It assumes nonempty, equal-width rows and uses identity projections, one head, and no positional contribution. It shows attention arithmetic, rather than a complete trainable Transformer.

~~~python
import math


def softmax(scores):
    largest = max(scores)
    exps = [math.exp(score - largest) for score in scores]
    total = sum(exps)
    return [value / total for value in exps]


def self_attention(x, causal=False):
    # Identity projections: Q, K, and V all equal x.
    width = len(x[0])
    weights = []

    for i, query in enumerate(x):
        scores = []
        for j, key in enumerate(x):
            score = sum(q * k for q, k in zip(query, key))
            score /= math.sqrt(width)
            if causal and j > i:
                score = -math.inf
            scores.append(score)
        weights.append(softmax(scores))

    output = [
        [
            sum(weight * value[col] for weight, value in zip(row, x))
            for col in range(width)
        ]
        for row in weights
    ]
    return weights, output


x = [[1.0, 0.0], [0.0, 1.0], [1.0, 1.0]]

weights, output = self_attention(x)
masked_weights, masked_output = self_attention(x, causal=True)

print("shoes weights:", [round(v, 4) for v in weights[2]])
print("shoes output:", [round(v, 4) for v in output[2]])
print("causal running weights:", [round(v, 4) for v in masked_weights[1]])
print("causal running output:", [round(v, 4) for v in masked_output[1]])
~~~

Expected output:

~~~text
shoes weights: [0.2483, 0.2483, 0.5035]
shoes output: [0.7517, 0.7517]
causal running weights: [0.3302, 0.6698, 0.0]
causal running output: [0.3302, 0.6698]
~~~

Try replacing the first token vector or toggling the mask. Observe which rows can change: under causal masking, changing the last input cannot change an earlier position's output in this forward pass.

For an actual framework implementation, pay attention to tensor dimensions, mask conventions, and attention dropout. The pinned PyTorch 2.8 reference documents these details; its boolean mask uses `True` to indicate an allowed position.[^sdpa]

## Cost and Limitations

### Sequence length and width affect different work

Let $n$ be sequence length, $d$ model width, $h$ head count, and $d_{ff}$ the feed-forward hidden width. With total head width comparable to $d$, leading per-layer costs include:

| Operation | Approximate arithmetic |
|---|---|
| Query, key, value, and output projections | $O(nd^2)$ |
| Dense query–key scores and value mixing | $O(n^2d)$ |
| Feed-forward network | $O(ndd_{ff})$ |

The original paper's attention-versus-recurrence table emphasizes the interaction term.[^aiayn] A full Transformer layer also pays for projections and the feed-forward network. Parallelism, batch size, padding, hardware, and kernels affect actual latency; asymptotic complexity alone cannot predict it.

### A small attention-memory calculation

**Inputs:** one sequence, eight heads, and float32 weights at four bytes per element. Count only a fully materialized attention-weight tensor for one layer.

**Step 1 — use 512 tokens.**

$$
8 \times 512^2 \times 4
= 8{,}388{,}608\text{ bytes}
= 8\text{ MiB}
$$

**Step 2 — double the length to 1,024 tokens.**

$$
8 \times 1024^2 \times 4
= 33{,}554{,}432\text{ bytes}
= 32\text{ MiB}
$$

Doubling sequence length quadruples this tensor's size. This is not total model memory: parameters, other activations, batches, gradients, and caches have their own costs.

Memory-efficient exact-attention algorithms such as FlashAttention avoid storing the full attention matrix in accelerator high-bandwidth memory.[^flash] They change memory traffic and storage requirements, rather than removing the dense token interactions from the mathematical operation.

### Common misunderstandings and failure modes

- **“Attention always knows what is important.”** It learns compatibility patterns from the training objective. A large weight is not automatically a human relevance label or a complete explanation of a final prediction.
- **“Each token corresponds to one word.”** Subword splitting and special tokens change the actual sequence. Important text can be truncated before attention sees it.
- **“All positions are always visible.”** Padding masks, causal masks, and other architecture-specific restrictions control information flow.
- **“More heads or layers must be better.”** Capacity, optimization, data, and architecture interact. The original head-count ablation already shows a non-monotonic result.
- **“Positions provide unlimited context.”** Context limits and behavior beyond trained lengths depend on the architecture and training.
- **“Attention alone explains the architecture's success.”** Pure attention has a token-uniformity tendency under the conditions studied by Dong et al.; residual paths can preserve differences, and MLPs can slow contraction.[^dong]
- **“A Transformer output is automatically a good sentence embedding.”** Pooling and the training objective determine whether the resulting vectors support useful similarity comparisons.
- **“KV caching makes every generation step equally cheap.”** It reuses earlier computations, while context-dependent work and cache storage still grow.

## Search Connections

The running phrase `red running shoes` can be a search query. Where it meets product text determines what a Transformer can precompute and what interactions it can learn.

### Retrieval: encode separately

A [[Dense Retrieval|bi-encoder]] encodes the query and product text separately, pools each into a vector, and compares those vectors. Product representations can be computed offline and indexed with [[Approximate Nearest Neighbours]].[^sbert]

Attention contextualizes tokens **within each independently encoded input**. The query's `red` token does not attend directly to a product's `black` token during those separate encoding passes.

### Ranking: encode the pair jointly

A conventional [[Cross-Encoder]] processes a joint sequence such as `[CLS] query [SEP] product text [SEP]` and predicts relevance. The exact special tokens depend on the backbone.

Bidirectional self-attention can compare tokens across the query and product segments. This supports detailed interactions, but the model must process each query–product pair at request time. Such systems commonly rerank a retrieved candidate set.[^sbert]

A **cross-encoder** is a scoring arrangement; it need not contain the decoder's **cross-attention** sublayer. An encoder-only model can use ordinary self-attention over the concatenated pair.

### Understanding, generation, and evaluation

- [[Query Understanding]] can use Transformer representations to classify intent or extract entities; encoder–decoder or decoder models can also rewrite queries.
- [[Retrieval-Augmented Generation]] supplies retrieved passages as context for generation. Retrieval quality and generation quality remain separate concerns.
- A semantic match does not enforce a hard constraint such as an exact SKU or required color. Representation quality, filtering, and [[Search Evaluation|relevance evaluation]] need separate checks.
- [[Latency vs Throughput]] helps assess batching, candidate count, sequence length, and generation costs. A quality gain must be measured alongside its serving cost.

## Exercise

### Attention checks

1. In the numerical example, which axis of $A$ must sum to one, and why?
2. Why do matching features come from keys while the transferred information comes from values?
3. Under a causal mask, can changing `shoes` alter the earlier `running` output in one forward pass?
4. Why is the `shoes` output vector different from the probability of predicting the word `shoes`?

> [!example]- Attention check answers
> Normalize across key columns within each query row. Queries and keys determine weights; values supply the mixed content. A causal earlier position cannot read the changed future token. The head's output contains features; a vocabulary projection and separate softmax are needed to obtain token probabilities.

### Retrieval and ranking calculation

Compare separately encoded query/document vectors with jointly encoding `[query, document]`.

1. Which computation can happen before a query arrives?
2. In which design can a query token attend directly to a document token?
3. A query has 10 tokens and a document 200. Ignoring special tokens, how many scores does one head compute in a bidirectional joint layer? How many connect query positions with document positions in either direction?

> [!example]- Exercise solution
> 1. Separate encoding lets document vectors be computed and indexed offline.
>
> 2. Joint encoding permits direct query–document token attention. With separate encoding, interaction occurs through the final vector comparison.
>
> 3. **Inputs:** 10 query tokens and 200 document tokens, giving 210 positions.
>
>    **Step 1 — total scores.**
>
>    $$
>    210^2 = 44{,}100
>    $$
>
>    **Step 2 — cross-segment scores, counting both directions.**
>
>    $$
>    2 \times 10 \times 200 = 4{,}000
>    $$
>
>    The remaining scores connect positions within the same segment. This counts dense interactions for one head and layer, not total runtime or measured relevance quality. See [[Search Ranking]].

## Existing Reading Collection

![[Transformer Papers]]

## Existing Illustrations

These previously saved illustrations provide additional views alongside the explanatory diagrams above.

![[Transformers-1.png]]

![[Masked_SA&SA.png]]

## Original Paper PDF

[[Research_Paper/Papers/Attention_is_all_you_need.pdf]]

The local copy is arXiv v5, dated 6 December 2017. It supplies the architecture, attention equations, positional encoding, training setup, complexity comparison, and historical English–German results discussed here. The numerical examples and new diagrams explain the mechanics; they are not learned attention measurements or reproduced experimental figures.

## References & Useful Links

[^aiayn]: [Vaswani et al. (2017), Attention Is All You Need](https://arxiv.org/html/1706.03762v7) — Original Transformer architecture, attention, positions, training recipe, complexity table, and ablations. The vault also retains the [PDF source](https://arxiv.org/pdf/1706.03762.pdf), with a local v5 copy linked above.
[^bahdanau]: [Bahdanau, Cho & Bengio (2014), Neural Machine Translation by Jointly Learning to Align and Translate](https://arxiv.org/abs/1409.0473) — Attention over recurrent encoder states to address the fixed-length translation bottleneck.
[^bert]: [Devlin et al. (2019), BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding](https://arxiv.org/abs/1810.04805) — Bidirectional encoder representations and masked-language-model pretraining.
[^sdpa]: [PyTorch 2.8 — scaled dot-product attention](https://docs.pytorch.org/docs/2.8/generated/torch.nn.functional.scaled_dot_product_attention.html) — Tensor shapes, boolean and additive mask conventions, dropout behavior, and implementation options; this is a version-pinned reference.
[^flash]: [Dao et al. (2022), FlashAttention](https://arxiv.org/abs/2205.14135) — Exact attention with reduced memory traffic and without materializing the full attention matrix in high-bandwidth memory; see Figure 1 and Section 3 of the [full paper](https://arxiv.org/html/2205.14135v2).
[^preln]: [Xiong et al. (2020), On Layer Normalization in the Transformer Architecture](https://arxiv.org/abs/2002.04745) — Pre-LN and Post-LN placement, their gradient behavior at initialization, and implications for optimization.
[^dong]: [Dong, Cordonnier & Loukas (2021), Attention is Not All You Need](https://arxiv.org/abs/2103.03404) — Conditional rank-collapse results for pure attention and the roles of skips and MLPs; the linked vault paper note records the local version and review boundaries.
[^sbert]: [Sentence Transformers — Retrieve & Re-Rank](https://sbert.net/examples/sentence_transformer/applications/retrieve_rerank/README.html) — Separately encoded retrieval followed by joint query–document scoring.

Previously saved resources, retained for further reading; not all were used to verify this rewrite:

- [YouTube video 9uw3F6rndnA](https://www.youtube.com/watch?v=9uw3F6rndnA) — Saved video; content has not been rechecked.
- [DataCamp — Building a Transformer with PyTorch](https://www.datacamp.com/tutorial/building-a-transformer-with-py-torch) — Saved implementation tutorial.
- [arXiv 2207.09238](https://arxiv.org/pdf/2207.09238) — Saved paper; title has not been rechecked.
- [Jay Alammar — The Illustrated GPT-2](http://jalammar.github.io/illustrated-gpt2/) — Saved visual walkthrough of a decoder-only model.
- [YouTube video UPtG_38Oq8o](https://www.youtube.com/watch?v=UPtG_38Oq8o) — Saved video; content has not been rechecked.
- [Harvard NLP — The Annotated Transformer](https://nlp.seas.harvard.edu/2018/04/03/attention.html) — Saved annotated implementation of the original paper.
