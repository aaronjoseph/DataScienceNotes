---
tags:
  - leetcode
problem_number: 435
difficulty: "Medium"
pattern: "Intervals"
languages:
  - Python
---

Remove the fewest intervals so the remaining intervals do not overlap.[^implementation]

Problem link: [[Job Interviews/Coding Practice Index#^lc435|LeetCode — LC 435]] · Completion: [[Action-Plan Kanban#Coding Backlog|Coding Backlog]].

## How to Solve

1. Sort intervals by start and track the end of the last retained interval.
2. When an interval does not overlap, retain it and advance that end.
3. When overlap occurs, count one removal and retain whichever interval ends earlier.

## Why It Works

Among conflicting intervals, keeping the earlier finish leaves at least as much room for every future interval.

## Worked Example

**Illustrative input:** `intervals = [[1, 3], [2, 4], [3, 5]]`.

**Trace:** Discard [2,4] in favor of the earlier finish [1,3]; [3,5] can remain.

**Result:** Return `1`.

## Python

Adapted reference implementation for the LeetCode Python 3 judge.

```python
from __future__ import annotations
from typing import List

class Solution:

    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = 0
        prevEnd = intervals[0][1]
        for start, end in intervals[1:]:
            if start >= prevEnd:
                prevEnd = end
            else:
                res += 1
                prevEnd = min(end, prevEnd)
        return res
```

## Complexity

$O(n\log n)$ time and $O(n)$ auxiliary space in Python, including sorting and the loop's slice. Bounds describe the implementation above and exclude required output unless stated otherwise.

## Common Pitfalls

Touching endpoints are allowed here. Compare retained finish times rather than always deleting the current interval.

## Related Notes

- [[Job Interviews/Coding Practice Index#^lc435|Coding Practice Index — Non Overlapping Intervals]] — Central problem URL and solution navigation.
- [[Action-Plan Kanban#Coding Backlog|Coding Backlog]] — Mark practice completion on the board.

## References & Useful Links

[^implementation]: [NeetCode contributors — Python reference for LC 435](https://github.com/neetcode-gh/leetcode/blob/d5ebb3ea8bd4b52d605bc7aa179e22af684d31bb/python/0435-non-overlapping-intervals.py) — Source implementation reviewed on 18 October 2026; the walkthrough and illustrative example are written for this vault. Code is adapted where needed for the stated approach.

> [!info]- Reference implementation licence
> ![[Job Interviews/Coding Practice Index#Implementation Licence]]
