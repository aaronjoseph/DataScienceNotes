---
note_type: concept
search_stage: query_understanding
---

# Stopwords

#search-eng

## Overview

Stopwords are terms an analyser chooses to omit, often because they are frequent. There is no universal list. Removing them may reduce index size or processing work, but can also erase information from phrases and names. [^1]

## Search Considerations

For the illustrative query `flights to Delhi`, removing `to` discards direction. For `The Who`, treating every common word as disposable damages a named entity. Test phrase and entity queries before enabling removal.

A frequent term can receive a low [[TF-IDF]] or [[BM25]] weight without being removed entirely. Retaining it can still matter for matching and phrase interpretation.

## Removal Changes the Available Evidence

Low weighting and deletion have different consequences. A retained term can still participate in phrase matching even when its score contribution is small. Deletion removes that evidence from the analysed representation.[^1] A later model cannot use a token that was discarded before it received the input.

Apply stopword decisions per field and task. A lexical title field, a phrase field, and a neural encoder input do not need the same preprocessing. In particular, do not apply a lexical stop list to a pretrained model's input without evaluating the resulting change from its expected input distribution.

### Compare two queries after removal

Consider `laptop with touchscreen` and `laptop without touchscreen`. If a rule removes both `with` and `without`, each becomes `laptop touchscreen`. The representation has lost the distinction between requiring and excluding an attribute.

Keeping the words is necessary for a parser to see that distinction, but it is not sufficient: the parser must understand the negation and map it to the correct filter. Test the full route from text to [[Query Understanding|query plan]].

## Empty and Phrase Queries

Define what happens when analysis leaves zero tokens: reject the query, ask for more detail, or use another deliberate route. A silent match-all fallback can produce an apparently healthy result count while ignoring intent. For phrase queries, inspect positions as well as remaining tokens; an engine can preserve position gaps even after deleting terms, and phrase behaviour depends on its implementation.

For revision, explain why removing common words can reduce postings while still making retrieval worse. Then distinguish an observed storage saving from a measured relevance improvement.

## Practice

Write five queries whose meaning changes after removing common words. Compare the analysed tokens and retrieved results with removal enabled and disabled.

## Related Notes

- [[Tokenization]] — Token boundaries precede many filtering decisions.
- [[Inverted Index]] — Analysis choices affect what is searchable.

## References & Useful Links

[^1]: [Dropping common terms: stop words](https://nlp.stanford.edu/IR-book/html/htmledition/dropping-common-terms-stop-words-1.html) — Benefits and information loss from stopword removal.
