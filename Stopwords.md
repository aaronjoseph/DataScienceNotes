# Stopwords

#search-eng

## Overview

Stopwords are terms an analyser chooses to omit, often because they are frequent. There is no universal list. Removing them may reduce index size or processing work, but can also erase information from phrases and names. [^1]

## Search Considerations

For the illustrative query `flights to Delhi`, removing `to` discards direction. For `The Who`, treating every common word as disposable damages a named entity. Test phrase and entity queries before enabling removal.

A frequent term can receive a low [[TF-IDF]] or [[BM25]] weight without being removed entirely. Retaining it can still matter for matching and phrase interpretation.

## Practice

Write five queries whose meaning changes after removing common words. Compare the analysed tokens and retrieved results with removal enabled and disabled.

## Related Notes

- [[Tokenization]] — Token boundaries precede many filtering decisions.
- [[Inverted Index]] — Analysis choices affect what is searchable.

## References & Useful Links

[^1]: [Dropping common terms: stop words](https://nlp.stanford.edu/IR-book/html/htmledition/dropping-common-terms-stop-words-1.html) — Benefits and information loss from stopword removal.
