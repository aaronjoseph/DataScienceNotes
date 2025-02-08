[[Encoding]]

### Main Concepts

**Word Encoding** refers to the process of converting words into numerical representations so they can be used in machine learning models. This process doesn't necessarily capture the meaning or relationships between words but focuses on transforming text into numbers. Common techniques include:
- **Bag of Words (BoW)**: Counts word occurrences in a document without considering the order or context.
- **TF-IDF (Term Frequency-Inverse Document Frequency)**: Weighs word importance based on its frequency in a document and across multiple documents, giving more value to rarer words.
---
- **Embedding representation** refers to the vector representations of words, where each word is assigned a continuous vector of real numbers.
- These vectors are dense, meaning each word’s vector contains real-valued components that reflect semantic relationships between words.
- Embeddings capture relationships such as:
    - Similar words have similar vectors (e.g., "king" and "queen").
    - Analogies can be computed with embeddings (e.g., "king - man + woman = queen").

**Why embeddings?**

- They are compact and capture semantic meaning in fewer dimensions than sparse representations (like one-hot encoding).

### Key Differences

- **Encoding** is a broader term encompassing any method that transforms words into numbers.
- **Embeddings** are a subset of encoding techniques that emphasise capturing the meaning and relationships between words, making them more powerful for tasks that involve understanding context.

> In summary, word embeddings are a specific type of encoding designed to preserve meaning, while simpler encoding methods like TF-IDF and BoW focus solely on numeric representation without context.