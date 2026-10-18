---
tags:
  - leetcode
problem_number: 127
difficulty: "Hard"
pattern: "Graphs"
languages:
  - Python
---

Find the length of the shortest sequence from a starting word to an ending word, changing one letter at a time through dictionary words.[^implementation]

Problem link: [[Job Interviews/Coding Practice Index#^lc127|LeetCode — LC 127]] · Completion: [[Action-Plan Kanban#Coding Backlog|Coding Backlog]].

## How to Solve

1. Index words by wildcard patterns such as h*t so one-letter neighbors can be found.
2. Run breadth-first search from the starting word, marking words when enqueued.
3. Expand each pattern bucket at most once and return the level when the ending word is dequeued.

## Why It Works

Each edge changes one character, and BFS levels enumerate paths in increasing numbers of transformations.

## Worked Example

**Illustrative input:** `beginWord = "hit"`, `endWord = "hot"`, dictionary `["hot"]`.

**Trace:** The words share pattern h*t and are one transformation apart.

**Result:** Return `2` because the sequence counts both words.

## Python

Adapted reference implementation for the LeetCode Python 3 judge.

```python
from __future__ import annotations
from typing import List
from collections import defaultdict, deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        patterns = defaultdict(list)
        for word in set(wordList) | {beginWord}:
            for i in range(len(word)):
                patterns[word[:i] + "*" + word[i + 1:]].append(word)
        queue = deque([(beginWord, 1)])
        seen = {beginWord}
        while queue:
            word, length = queue.popleft()
            if word == endWord:
                return length
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i + 1:]
                for neighbor in patterns[pattern]:
                    if neighbor not in seen:
                        seen.add(neighbor)
                        queue.append((neighbor, length + 1))
                patterns[pattern].clear()
        return 0
```

## Complexity

$O(NL^2)$ expected time and $O(NL^2)$ stored pattern-character space in Python for `N` words of length `L`, plus bucket references. Bounds describe the implementation above and exclude required output unless stated otherwise.

## Common Pitfalls

Return zero if the target is absent or unreachable. Clear processed buckets to avoid repeatedly scanning the same neighbor lists.

## Related Notes

- [[Job Interviews/Coding Practice Index#^lc127|Coding Practice Index — Word Ladder]] — Central problem URL and solution navigation.
- [[Action-Plan Kanban#Coding Backlog|Coding Backlog]] — Mark practice completion on the board.

## References & Useful Links

[^implementation]: [NeetCode contributors — Python reference for LC 127](https://github.com/neetcode-gh/leetcode/blob/d5ebb3ea8bd4b52d605bc7aa179e22af684d31bb/python/0127-word-ladder.py) — Source implementation reviewed on 18 October 2026; the walkthrough and illustrative example are written for this vault. Code is adapted where needed for the stated approach.

> [!info]- Reference implementation licence
> ![[Job Interviews/Coding Practice Index#Implementation Licence]]
