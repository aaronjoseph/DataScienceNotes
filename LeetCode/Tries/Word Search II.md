---
tags:
  - leetcode
problem_number: 212
difficulty: "Hard"
pattern: "Tries"
languages:
  - Python
---

## Algorithm at a glance

![[Attachements/LeetCode/LC0212 - Word Search II.png|700]]

## Overview

Find dictionary words that can be traced through adjacent board cells without reusing a cell in one path.[^implementation]

Problem link: [[Job Interviews/Coding Practice Index#^lc212|LeetCode — LC 212]] · Completion: [[Action-Plan Kanban#Coding Backlog|Coding Backlog]].

## How to Solve

1. Build a trie for all words so common prefixes share work.
2. Start depth-first search at every cell, following only matching trie edges and marking the current cell as used.
3. On a terminal node, record the word once and prune exhausted prefixes; undo path visitation when returning.

## Why It Works

Every possible board path is explored unless its prefix matches no remaining word, in which case extending it cannot help.

## Worked Example

**Illustrative input:** `board = [["a", "b"], ["c", "d"]]`, words `["ab", "ac", "aa"]`.

**Trace:** Paths along the top row and left column find ab and ac; aa would require an unavailable next a.

**Result:** Return `ab` and `ac`.

## Common Pitfalls

Restore visited cells after each branch. Deduplicate words and distinguish path-local visitation from global visitation.

## Related Notes

- [[Job Interviews/Coding Practice Index#^lc212|Coding Practice Index — Word Search II]] — Central problem URL and solution navigation.
- [[Action-Plan Kanban#Coding Backlog|Coding Backlog]] — Mark practice completion on the board.

## Template

### Python

Adapted reference implementation for the LeetCode Python 3 judge.

```python
from __future__ import annotations
from typing import List

class TrieNode:

    def __init__(self):
        self.children = {}
        self.isWord = False
        self.refs = 0

    def addWord(self, word):
        cur = self
        cur.refs += 1
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
            cur.refs += 1
        cur.isWord = True

    def removeWord(self, word):
        cur = self
        cur.refs -= 1
        for c in word:
            if c in cur.children:
                cur = cur.children[c]
                cur.refs -= 1

class Solution:

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for w in words:
            root.addWord(w)
        ROWS, COLS = (len(board), len(board[0]))
        res, visit = (set(), set())

        def dfs(r, c, node, word):
            if r not in range(ROWS) or c not in range(COLS) or board[r][c] not in node.children or (node.children[board[r][c]].refs < 1) or ((r, c) in visit):
                return
            visit.add((r, c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.isWord:
                node.isWord = False
                res.add(word)
                root.removeWord(word)
            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)
            visit.remove((r, c))
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, '')
        return list(res)
```

## Complexity

A conservative bound is $O(S+RC\,L\,4^L)$ time with Python path-string copies; $O(S+L^2)$ auxiliary space excluding results, where `L` is maximum word length. Bounds describe the implementation above and exclude required output unless stated otherwise.

## References & Useful Links

[^implementation]: [NeetCode contributors — Python reference for LC 212](https://github.com/neetcode-gh/leetcode/blob/d5ebb3ea8bd4b52d605bc7aa179e22af684d31bb/python/0212-word-search-ii.py) — Source implementation reviewed on 18 October 2026; the walkthrough and illustrative example are written for this vault. Code is adapted where needed for the stated approach.

> [!info]- Reference implementation licence
> ![[Job Interviews/Coding Practice Index#Implementation Licence]]
