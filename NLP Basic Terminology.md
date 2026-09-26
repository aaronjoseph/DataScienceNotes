---
note_type: concept
search_stage: foundations
---

# NLP Basic Terminology

#search-eng

## Core Vocabulary

- **Corpus:** A collection of documents.
- **Token:** One occurrence produced by [[Tokenization]].
- **Vocabulary:** The distinct token types or indexed terms represented by the system.
- **Term frequency (TF):** Occurrences of a term within a document, or a stated transform of that count.
- **Document frequency (DF):** Number of documents containing a term.
- **Inverse document frequency (IDF):** A weight based on document rarity, not DF itself. A basic form is $\log(N/df(t))$ for a term present in a corpus of $N$ documents. [^1]

[[TF-IDF]] multiplies a TF weight by an IDF weight; it does not add them.

## Representation Vocabulary

[[Bag of Words]] uses vocabulary dimensions and ignores ordering. [[N-Grams]] represents adjacent units. [[Embeddings]] uses learned vectors, while [[Cosine Similarity]] is a way to compare vectors rather than a representation itself.

## Count the Right Thing

For a collection $\mathcal D$ with $N$ documents and analysed term $t$, define

**Term frequency:**

$$
\operatorname{tf}(t,d)=\operatorname{count}(t\text{ in }d)
$$

**Document frequency:**

$$
\operatorname{df}(t)=\sum_{d\in\mathcal D}\mathbf1[\operatorname{tf}(t,d)>0]
$$

$$
\operatorname{cf}(t)=\sum_{d\in\mathcal D}\operatorname{tf}(t,d).
$$

Here $\mathbf1[\cdot]$ is 1 when its condition is true and 0 otherwise.

Collection frequency counts occurrences; document frequency counts containing documents.

A repeated term increases CF without necessarily increasing DF.

These definitions assume one fixed field and analysis policy; title statistics and description statistics need not agree.

### Work through the two-document corpus

D1 is `red red boots`; D2 is `red shoes`. There are five token occurrences and three token types: `red`, `boots`, `shoes`.

**1. Count occurrences of `red`.**

- TF in D1: 2.
- Collection frequency (CF): 3.
- Document frequency (DF): 2.
- Collection size: $N=2$.

Its unsmoothed IDF is

$$
\ln\left(\frac{2}{2}\right)=0.
$$

**2. Count occurrences of `boots`.**

TF in D1, CF, and DF are all 1. Its IDF is

$$
\ln\left(\frac{2}{1}\right)=\ln2\approx0.6931.
$$

Adding D3=`red red red` changes red's CF to 6 and DF to 3. Adding a fourth `red` to D3 changes only CF and D3's TF.

## From Vocabulary to Retrieval

A **posting** associates a term with a document; it can also store frequency or positions. A **candidate** is an item selected for later scoring. A **relevance grade** is an assessment of a query–item pair. Keep these terms distinct when interpreting a pipeline: many matching postings do not establish many useful results. See [[Inverted Index]] and [[Candidate Generation]].

## Practice

In documents `red red boots` and `red shoes`, `red` has collection frequency 3 and document frequency 2. Its raw term frequency in the first document is 2. Explain why these counts answer different questions.

## References & Useful Links

[^1]: [Inverse document frequency](https://nlp.stanford.edu/IR-book/html/htmledition/inverse-document-frequency-1.html) — DF, rarity, and IDF weighting.
