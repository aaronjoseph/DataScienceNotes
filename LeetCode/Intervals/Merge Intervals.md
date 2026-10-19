---
tags:
  - leetcode
problem_number: 56
difficulty: "Medium"
pattern: "Intervals"
languages:
  - Python
---

## Algorithm at a glance

![[Attachements/LeetCode/LC0056 - Merge Intervals.png|700]]

## Overview

Merge all overlapping closed intervals into a sorted nonoverlapping list.[^implementation]

Problem link: [[Job Interviews/Coding Practice Index#^lc56|LeetCode — LC 56]] · Completion: [[Action-Plan Kanban#Coding Backlog|Coding Backlog]].

## How to Solve

1. Sort intervals by their starts.
2. Keep the most recent merged interval in the output.
3. If the next start is no greater than that interval's end, extend its end; otherwise append a new interval.

## Why It Works

After sorting, only the latest merged interval can overlap the next input interval.

## Worked Example

**Illustrative input:** `intervals = [[5, 7], [1, 3], [2, 6]]`.

**Trace:** Sorting places [1,3] first; both later intervals join its growing range.

**Result:** Return `[[1, 7]]`.

## Common Pitfalls

Endpoint contact counts as overlap. This implementation sorts in place and may mutate an interval object reused in the output.

## Related Notes

- [[Job Interviews/Coding Practice Index#^lc56|Coding Practice Index — Merge Intervals]] — Central problem URL and solution navigation.
- [[Action-Plan Kanban#Coding Backlog|Coding Backlog]] — Mark practice completion on the board.

## Template

### Python

Adapted reference implementation for the LeetCode Python 3 judge.

```python
from __future__ import annotations
from typing import List

class Solution:

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda pair: pair[0])
        output = [intervals[0]]
        for start, end in intervals:
            lastEnd = output[-1][1]
            if start <= lastEnd:
                output[-1][1] = max(lastEnd, end)
            else:
                output.append([start, end])
        return output
```

## Complexity

$O(n\log n)$ time and $O(n)$ sorting/output storage. Bounds describe the implementation above and exclude required output unless stated otherwise.

## References & Useful Links

[^implementation]: [NeetCode contributors — Python reference for LC 56](https://github.com/neetcode-gh/leetcode/blob/d5ebb3ea8bd4b52d605bc7aa179e22af684d31bb/python/0056-merge-intervals.py) — Source implementation reviewed on 18 October 2026; the walkthrough and illustrative example are written for this vault. Code is adapted where needed for the stated approach.

> [!info]- Reference implementation licence
> ![[Job Interviews/Coding Practice Index#Implementation Licence]]
