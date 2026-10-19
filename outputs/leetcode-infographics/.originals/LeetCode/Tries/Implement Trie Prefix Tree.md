---
tags:
  - leetcode
problem_number: 208
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
        self.children = [None] * 26
        self.end = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            i = ord(c) - ord('a')
            if curr.children[i] is None:
                curr.children[i] = TrieNode()
            curr = curr.children[i]
        curr.end = True

    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            i = ord(c) - ord('a')
            if curr.children[i] is None:
                return False
            curr = curr.children[i]
        return curr.end

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            i = ord(c) - ord('a')
            if curr.children[i] is None:
                return False
            curr = curr.children[i]
        return True
```

## Complexity

$O(L)$ time per operation for `L` characters; $O(S)$ nodes for `S` total inserted characters, with fixed-size alphabet child arrays. Bounds describe the implementation above and exclude required output unless stated otherwise.

## Overview

Implement word insertion, exact search, and prefix search with a trie, a tree of shared character prefixes.[^implementation]

Problem link: [[Job Interviews/Coding Practice Index#^lc208|LeetCode — LC 208]] · Completion: [[Action-Plan Kanban#Coding Backlog|Coding Backlog]].

## How to Solve

1. Each node stores child links and a flag marking a completed word.
2. Insert by creating missing character nodes and marking the final node.
3. Traverse the same path for searches; exact search needs the terminal flag, while prefix search needs only the path.

## Why It Works

A root-to-node path uniquely identifies a prefix; the terminal marker distinguishes whole words from partial prefixes.

## Worked Example

**Illustrative input:** Insert `"apple"`.

**Trace:** The path app exists, but its node has no completed-word marker.

**Result:** `startsWith("app")` is true and `search("app")` is false.

## Common Pitfalls

This implementation assumes lowercase English letters. A prefix is not automatically a stored word.

## Related Notes

- [[Job Interviews/Coding Practice Index#^lc208|Coding Practice Index — Implement Trie Prefix Tree]] — Central problem URL and solution navigation.
- [[Action-Plan Kanban#Coding Backlog|Coding Backlog]] — Mark practice completion on the board.

## References & Useful Links

[^implementation]: [NeetCode contributors — Python reference for LC 208](https://github.com/neetcode-gh/leetcode/blob/d5ebb3ea8bd4b52d605bc7aa179e22af684d31bb/python/0208-implement-trie-prefix-tree.py) — Source implementation reviewed on 18 October 2026; the walkthrough and illustrative example are written for this vault. Code is adapted where needed for the stated approach.

> [!info]- Reference implementation licence
> ![[Job Interviews/Coding Practice Index#Implementation Licence]]
