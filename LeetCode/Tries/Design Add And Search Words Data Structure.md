---
tags:
  - leetcode
problem_number: 211
difficulty: "Medium"
pattern: "Tries"
languages:
  - Python
---

## Template

### Python

Adapted reference implementation for the LeetCode Python 3 judge.

```python
from __future__ import annotations

class TrieNode:

    def __init__(self):
        self.children = {}
        self.word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.word = True

    def search(self, word: str) -> bool:

        def dfs(j, root):
            cur = root
            for i in range(j, len(word)):
                c = word[i]
                if c == '.':
                    for child in cur.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]
            return cur.word
        return dfs(0, self.root)
```

## Complexity

Insertion takes $O(L)$ time. Search visits at most the relevant trie nodes; a loose bound is $O(L\,26^d)$ for `d` dots. Trie storage is $O(S)$. Bounds describe the implementation above and exclude required output unless stated otherwise.

## Overview

Store words and search patterns where a dot matches any single letter.[^implementation]

Problem link: [[Job Interviews/Coding Practice Index#^lc211|LeetCode — LC 211]] · Completion: [[Action-Plan Kanban#Coding Backlog|Coding Backlog]].

## How to Solve

1. Insert ordinary words into a trie and mark their ends.
2. For a literal search character, follow only that child.
3. For a dot, recursively try each child; accept only if the full pattern ends at a completed word.

## Why It Works

Literal steps preserve exact matches, and wildcard branching enumerates exactly the permitted one-character alternatives.

## Worked Example

**Illustrative input:** Insert `"bad"` and `"dad"`; search `".ad"`.

**Trace:** The dot explores first-letter children, and the remaining suffix matches ad.

**Result:** Return `True`.

## Common Pitfalls

A dot matches one character, not an arbitrary-length substring. Reaching a nonterminal prefix does not complete a match.

## Related Notes

- [[Job Interviews/Coding Practice Index#^lc211|Coding Practice Index — Design Add And Search Words Data Structure]] — Central problem URL and solution navigation.
- [[Action-Plan Kanban#Coding Backlog|Coding Backlog]] — Mark practice completion on the board.

## References & Useful Links

[^implementation]: [NeetCode contributors — Python reference for LC 211](https://github.com/neetcode-gh/leetcode/blob/d5ebb3ea8bd4b52d605bc7aa179e22af684d31bb/python/0211-design-add-and-search-words-data-structure.py) — Source implementation reviewed on 18 October 2026; the walkthrough and illustrative example are written for this vault. Code is adapted where needed for the stated approach.

> [!info]- Reference implementation licence
> ![[Job Interviews/Coding Practice Index#Implementation Licence]]
