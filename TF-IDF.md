### Term Frequency - Inverse Document Frequency (TF-IDF)

When using a word vectoriser like the [[Bag of Words (BOW)| bag of words]] model, a major issue arises:
- **Common words receive disproportionately high weightage** because they appear frequently across many documents. This requires normalization to ensure that the word importance is appropriately represented.

To address this, we use **TF-IDF**, which is defined as:

$$ \text{TF-IDF} = \text{TF} \times \text{IDF} $$

### Term Frequency (TF)

**Term Frequency (TF)** measures how often a word appears in a sentence (or document) relative to the total number of words in that sentence (or document):

$$ \text{TF} = \frac{\text{Number of Occurrences of the Word in the Document}}{\text{Total Number of Words in the Document}} $$

### Inverse Document Frequency (IDF)

**Inverse Document Frequency (IDF)** measures how unique or rare a word is across all documents in the corpus. It helps to penalize common words:

$$ \text{IDF} = \log\left(\frac{\text{Total Number of Documents}}{\text{Number of Documents Containing the Word}}\right) $$

- If a word appears in many documents, the IDF value decreases, reducing its overall TF-IDF score.
- If a word appears in only a few documents, the IDF value increases, boosting its TF-IDF score.

### Key Aspects of TF-IDF

- **Uncommon words in a document** tend to have a higher TF-IDF score because they are more unique and therefore more significant for that specific document.
- **Common words in a document** tend to have a lower TF-IDF score, often close to zero, because they appear frequently across many documents and are less distinctive.

