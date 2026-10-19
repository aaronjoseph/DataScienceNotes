---
tags:
  - leetcode
problem_number: 57
difficulty: "Medium"
pattern: "Intervals"
languages:
  - Python
---

## Template

### Python

Adapted reference implementation for the LeetCode Python 3 judge.

```python
from __future__ import annotations
from typing import List

class Solution:

    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
        res.append(newInterval)
        return res
```

## Complexity

$O(n)$ time and up to $O(n)$ output storage; list slicing/concatenation in this implementation also uses $O(n)$ transient space. Bounds describe the implementation above and exclude required output unless stated otherwise.

## Overview

Insert an interval into an already sorted, nonoverlapping interval list and merge any overlap.[^implementation]

Problem link: [[Job Interviews/Coding Practice Index#^lc57|LeetCode — LC 57]] · Completion: [[Action-Plan Kanban#Coding Backlog|Coding Backlog]].

## How to Solve

1. Append intervals strictly before the new interval.
2. While intervals overlap the new interval, expand its endpoints to cover both.
3. Append the merged interval and every remaining later interval.

## Why It Works

Sorted order puts every possible overlap in one contiguous run, so no earlier or later interval needs revisiting.

## Worked Example

**Illustrative input:** Intervals `[[1, 2], [5, 7]]`, new interval `[2, 6]`.

**Trace:** The new interval touches the first and overlaps the second.

**Result:** Return `[[1, 7]]`.

## Common Pitfalls

The inputs are already sorted and nonoverlapping. These closed intervals merge when endpoints touch.

## Related Notes

- [[Job Interviews/Coding Practice Index#^lc57|Coding Practice Index — Insert Interval]] — Central problem URL and solution navigation.
- [[Action-Plan Kanban#Coding Backlog|Coding Backlog]] — Mark practice completion on the board.

## References & Useful Links

[^implementation]: [NeetCode contributors — Python reference for LC 57](https://github.com/neetcode-gh/leetcode/blob/d5ebb3ea8bd4b52d605bc7aa179e22af684d31bb/python/0057-insert-interval.py) — Source implementation reviewed on 18 October 2026; the walkthrough and illustrative example are written for this vault. Code is adapted where needed for the stated approach.

> [!info]- Reference implementation licence
> ![[Job Interviews/Coding Practice Index#Implementation Licence]]
