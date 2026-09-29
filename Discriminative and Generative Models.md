---
aliases:
  - Discriminative vs Generative Models
  - Generative vs Discriminative Models
tags:
  - "ds-foundations"
---

A classifier can be built in two ways. A **discriminative** model learns to predict the label from the input directly. A **generative** model learns how inputs are distributed within each class, then uses Bayes' rule to turn that into a prediction.

"Descriptive vs probabilistic" is not the standard contrast: both families can output probabilities. Two separate questions matter more:

1. **Which distribution is modelled?** The label given the input, or the input itself.
2. **Is the output a probability at all?** Some discriminative models return only a score or a side of a boundary.

## The Two Approaches

Notation: $x$ is the input (features), $y$ the label, and $K$ the number of classes.

**Discriminative.** Model the conditional distribution of the label directly, or only a decision boundary:

$$
p_\theta(y \mid x)
$$

**Generative.** Model the class prior and the class-conditional distribution of the input, which together define the joint distribution:

$$
p(x, y) = p(x \mid y)\,p(y)
$$

Classification then uses Bayes' rule:

$$
p(y = k \mid x) = \frac{p(x \mid y = k)\,p(y = k)}{\sum_{l=1}^{K} p(x \mid y = l)\,p(y = l)}
$$

A generative model therefore answers more questions: how likely an input is, what a typical input of class $k$ looks like, and what to predict when some features are missing. The price is that it must model the input, which is usually harder than modelling the label.

## Examples

| Model | Family | What it learns | Probability output? |
|---|---|---|---|
| [[Logistic Regression]] | Discriminative | $p(y \mid x)$ through a linear logit | Yes |
| [[Support Vector Machines]] | Discriminative | A maximum-margin boundary | No; needs a calibration step |
| [[Decision Trees]], [[Random Forest]], [[Gradient Boosting Machines (GBM)\|GBMs]] | Discriminative | Partitions of feature space | Scores; check calibration |
| Fine-tuned [[BERT]] classifier | Discriminative | $p(y \mid x)$ through a [[Softmax Function\|softmax]] head | Yes |
| [[Naive Bayes]] | Generative | $p(y)$ and one $p(x_j \mid y)$ per feature | Yes, but often poorly calibrated |
| LDA and QDA classifiers | Generative | A Gaussian $p(x \mid y)$ per class | Yes |
| [[Gaussian Mixture Models]] | Generative, unsupervised | $p(x)$ as a mixture of Gaussians | A density |
| [[GAN]] | Generative | A sampler for $p(x)$ | Samples, no explicit density |
| [[Decoder-Only Model (Transformers)\|GPT-style LLM]] | Generative | $p(x_t \mid x_{<t})$ over tokens | Token probabilities |

Linear discriminant analysis (LDA) is generative despite its name: as a classifier, it fits a Gaussian to each class with a shared covariance matrix and applies Bayes' rule.[^sk-lda] The existing [[Linear Discriminant Analysis]] note covers its other use, supervised dimensionality reduction.

Scikit-learn's documentation describes naive Bayes as "a decent classifier" but "a bad estimator", whose `predict_proba` outputs should not be taken too seriously.[^sk-nb] The worked example below shows one reason.

## Tradeoffs

Ng and Jordan compared logistic regression with naive Bayes. They found that the discriminative model has lower asymptotic error, but the generative model can approach its own, higher, asymptotic error much faster. As training data grows, there can be two regimes: naive Bayes ahead with little data, logistic regression ahead with more.[^ng-jordan] This is a result for that pair of models, not a universal rule.

- **Generative strengths:** can score how typical an input is, marginalise over missing features, and generate samples.
- **Generative weaknesses:** wrong modelling assumptions, such as conditional independence, distort the probabilities even when the ranking is fine.
- **Discriminative strengths:** capacity goes only into separating the classes; usually more accurate with enough data.
- **Discriminative weaknesses:** no notion of an unusual input, so it can be confidently wrong on inputs unlike its training data. Grathwohl et al. show a standard image classifier confidently labelling generated noise as a class.[^jem]

## Worked Example: Double-Counted Evidence

A search team classifies queries as **commercial** ($c$) or **informational** ($i$).

**Inputs.** 100 labelled queries: 40 commercial and 60 informational. Feature $x_1$ is 1 when the query contains "buy". It fires on 24 commercial and 6 informational queries.

**Step 1 — estimate the generative model from the counts.**

- Prior: $p(c) = 40/100 = 0.4$, so $p(i) = 0.6$.
- Likelihood for commercial queries: $p(x_1 = 1 \mid c) = 24/40 = 0.6$.
- Likelihood for informational queries: $p(x_1 = 1 \mid i) = 6/60 = 0.1$.

**Step 2 — naive Bayes posterior with one feature.**

$$
p(c \mid x_1 = 1) = \frac{0.6 \times 0.4}{0.6 \times 0.4 + 0.1 \times 0.6} = \frac{0.24}{0.30} = 0.8
$$

**Step 3 — the discriminative estimate, read directly from the counts.**

$$
p(c \mid x_1 = 1) = \frac{24}{24 + 6} = 0.8
$$

With one binary feature, both approaches agree.

**Step 4 — add a duplicate feature.** A second feature $x_2$, "contains a purchase keyword", uses a keyword list that currently contains only "buy", so it fires on exactly the same queries. Naive Bayes assumes the two features are independent given the class and multiplies the evidence twice:

$$
p(c \mid x_1 = 1, x_2 = 1) = \frac{0.6^2 \times 0.4}{0.6^2 \times 0.4 + 0.1^2 \times 0.6} = \frac{0.144}{0.150} = 0.96
$$

**Interpretation.** Among these queries, the true share of commercial queries is still 24 out of 30, or 0.8. Naive Bayes reports 0.96 because it counted the same evidence twice. A maximum-likelihood logistic regression with an intercept can share weight between the two identical features and still predict 0.8. The order of queries is unchanged, so a ranking metric would not notice; the damage is to [[Probability Calibration|calibration]].

## Hybrids and Language Models

- **Adversarial training:** a [[GAN]] trains a generator against a discriminator that estimates whether a sample is real.
- **Joint Energy-based Models (JEM):** Grathwohl et al. reinterpret an ordinary classifier's logits as an energy-based model of $p(x, y)$ and train both parts. On their image benchmarks this improved calibration and out-of-distribution detection, but training was unstable.[^jem]
- **LLMs:** pretraining is generative, modelling token sequences as in [[Language Model]]. Prompting an LLM for a label turns a generative model into a classifier, but its label-token probabilities are not calibrated by default. Measure calibration before using them as probabilities. [[Structured Outputs]] constrains the format of such answers; it does not make them correct.
- **Typed decision models:** [[System One Models]] such as TypeSafe's Jev expose only a distribution over answers you define in advance, which is a discriminative interface. The vendor has not published the architecture behind it.

## Common Pitfalls

- **"Generative AI" is not a model family for classification.** A generative LLM can be used as a discriminative predictor, and a classic generative classifier such as naive Bayes generates nothing useful.
- **A probability output is not a calibrated probability.** Check with reliability diagrams, as in [[Probability Calibration]].
- **Good ranking can hide bad probabilities.** The worked example keeps the order of queries but inflates their probabilities.

## Exercise

Add a third feature to the worked example that again duplicates $x_1$. Compute the naive Bayes posterior, and explain what a well-specified model should report.

> [!example]- Exercise solution
> **Step 1 — numerator.**
>
> $$
> 0.6^3 \times 0.4 = 0.0864
> $$
>
> **Step 2 — the other class.**
>
> $$
> 0.1^3 \times 0.6 = 0.0006
> $$
>
> **Step 3 — posterior.**
>
> $$
> p(c \mid x_1 = x_2 = x_3 = 1) = \frac{0.0864}{0.0864 + 0.0006} \approx 0.993
> $$
>
> The observed share is still 0.8. Each duplicate pushes naive Bayes further towards certainty, while a model that learns $p(y \mid x)$ directly has no reason to move.

## References & Useful Links

[^ng-jordan]: [Ng and Jordan (2001), On Discriminative vs. Generative Classifiers: A comparison of logistic regression and naive Bayes](https://papers.nips.cc/paper/2001/hash/7b7a53e239400a13bd6be6c91c4f6c4e-Abstract.html) — NeurIPS 14; lower asymptotic error for the discriminative model, faster convergence for the generative one, and two data-size regimes.
[^sk-lda]: [Scikit-learn — Linear and Quadratic Discriminant Analysis](https://scikit-learn.org/stable/modules/lda_qda.html) — LDA and QDA as Gaussian class-conditional models classified with Bayes' rule; relation to Gaussian naive Bayes.
[^sk-nb]: [Scikit-learn — Naive Bayes](https://scikit-learn.org/stable/modules/naive_bayes.html) — The conditional-independence assumption and the warning about `predict_proba`.
[^jem]: [Grathwohl et al. (2019), Your Classifier is Secretly an Energy Based Model and You Should Treat it Like One](https://arxiv.org/abs/1912.03263) — The JEM hybrid; calibration, out-of-distribution, and robustness results on CIFAR and SVHN; training-instability caveats.
