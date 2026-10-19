---
tags:
  - leetcode
problem_number: 763
difficulty: "Medium"
pattern: "Greedy"
languages:
  - Python
---

## Algorithm at a glance

![[Attachements/LeetCode/LC0763 - Partition Labels.png|700]]

## Overview

Split a string into as many contiguous parts as possible so each character appears in only one part.[^implementation]

Problem link: [[Job Interviews/Coding Practice Index#^lc763|LeetCode — LC 763]] · Completion: [[Action-Plan Kanban#Coding Backlog|Coding Backlog]].

## How to Solve

1. Record the last occurrence of each character.
2. Scan left to right, extending the current part's required endpoint to include each encountered character's last occurrence.
3. When the current index reaches that endpoint, close the part and begin the next.

## Why It Works

Before the endpoint, some seen character still occurs later; at the endpoint, no character in the part escapes it, so the earliest safe cut is optimal.

## Worked Example

**Illustrative input:** `s = "abac"`.

**Trace:** The a at index zero extends the first part through index two; c then forms its own part.

**Result:** Return `[3, 1]`.

## Common Pitfalls

Use last occurrences across the entire string. The objective is the greatest number of parts, not shortest total length.

## Related Notes

- [[Job Interviews/Coding Practice Index#^lc763|Coding Practice Index — Partition Labels]] — Central problem URL and solution navigation.
- [[Action-Plan Kanban#Coding Backlog|Coding Backlog]] — Mark practice completion on the board.

## Template

### Python

Adapted reference implementation for the LeetCode Python 3 judge.

```python
from __future__ import annotations
from typing import List

class Solution:

    def partitionLabels(self, S: str) -> List[int]:
        count = {}
        res = []
        i, length = (0, len(S))
        for j in range(length):
            c = S[j]
            count[c] = j
        curLen = 0
        goal = 0
        while i < length:
            c = S[i]
            goal = max(goal, count[c])
            curLen += 1
            if goal == i:
                res.append(curLen)
                curLen = 0
            i += 1
        return res
```

## Complexity

$O(n)$ expected time and $O(u)$ auxiliary space, excluding output. Bounds describe the implementation above and exclude required output unless stated otherwise.

## References & Useful Links

[^implementation]: [NeetCode contributors — Python reference for LC 763](https://github.com/neetcode-gh/leetcode/blob/d5ebb3ea8bd4b52d605bc7aa179e22af684d31bb/python/0763-partition-labels.py) — Source implementation reviewed on 18 October 2026; the walkthrough and illustrative example are written for this vault. Code is adapted where needed for the stated approach.

> [!info]- Reference implementation licence
> ![[Job Interviews/Coding Practice Index#Implementation Licence]]
