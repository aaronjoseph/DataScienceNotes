---
tags:
  - leetcode
problem_number: 252
difficulty: "Easy"
pattern: "Intervals"
languages:
  - Python
---

## Template

### Python

Adapted reference implementation for the LeetCode Python 3 judge.

```python
from __future__ import annotations

class Solution:

    def canAttendMeetings(self, intervals):
        intervals.sort(key=lambda i: i[0])
        for i in range(1, len(intervals)):
            i1 = intervals[i - 1]
            i2 = intervals[i]
            if i1[1] > i2[0]:
                return False
        return True
```

## Complexity

$O(n\log n)$ time and $O(n)$ worst-case auxiliary sorting space in Python. Bounds describe the implementation above and exclude required output unless stated otherwise.

## Overview

Determine whether one person can attend every meeting without an overlap.[^implementation]

Problem link: [[Job Interviews/Coding Practice Index#^lc252|LeetCode — LC 252]] · Completion: [[Action-Plan Kanban#Coding Backlog|Coding Backlog]].

## How to Solve

1. Sort meeting intervals by start time.
2. Compare each meeting's start with the preceding meeting's end.
3. Reject a strict overlap; otherwise accept after all adjacent pairs pass.

## Why It Works

If any intervals overlap in sorted order, an overlap also appears between an adjacent pair.

## Worked Example

**Illustrative input:** `intervals = [[1, 2], [2, 3]]`.

**Trace:** The first meeting ends exactly when the next begins.

**Result:** Return `True`.

## Common Pitfalls

A meeting starting at another's end does not overlap. The implementation sorts the input list in place.

## Related Notes

- [[Job Interviews/Coding Practice Index#^lc252|Coding Practice Index — Meeting Rooms]] — Central problem URL and solution navigation.
- [[Action-Plan Kanban#Coding Backlog|Coding Backlog]] — Mark practice completion on the board.

## References & Useful Links

[^implementation]: [NeetCode contributors — Python reference for LC 252](https://github.com/neetcode-gh/leetcode/blob/d5ebb3ea8bd4b52d605bc7aa179e22af684d31bb/python/0252-meeting-rooms.py) — Source implementation reviewed on 18 October 2026; the walkthrough and illustrative example are written for this vault. Code is adapted where needed for the stated approach.

> [!info]- Reference implementation licence
> ![[Job Interviews/Coding Practice Index#Implementation Licence]]
