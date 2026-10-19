---
tags:
  - leetcode
problem_number: 253
difficulty: "Medium"
pattern: "Intervals"
languages:
  - Python
---

## Algorithm at a glance

![[Attachements/LeetCode/LC0253 - Meeting Rooms II.png|700]]

## Overview

Find the minimum number of meeting rooms by measuring maximum simultaneous meetings.[^implementation]

Problem link: [[Job Interviews/Coding Practice Index#^lc253|LeetCode — LC 253]] · Completion: [[Action-Plan Kanban#Coding Backlog|Coding Backlog]].

## How to Solve

1. Sort starts and ends into separate arrays.
2. Compare the next start and end; a start earlier than the end requires another active room.
3. Otherwise process an ending first and free a room; track the maximum active count.

## Why It Works

The minimum room requirement equals peak concurrency, which the chronological sweep measures exactly.

## Worked Example

**Illustrative input:** `intervals = [[0, 10], [5, 7], [7, 9]]`.

**Trace:** Two meetings overlap, while the room ending at 7 can immediately host the meeting starting at 7.

**Result:** Return `2`.

## Common Pitfalls

Process ends before equal-time starts so reusable rooms are not overcounted. The contract uses positive-duration meetings.

## Related Notes

- [[Job Interviews/Coding Practice Index#^lc253|Coding Practice Index — Meeting Rooms II]] — Central problem URL and solution navigation.
- [[Action-Plan Kanban#Coding Backlog|Coding Backlog]] — Mark practice completion on the board.

## Template

### Python

Adapted reference implementation for the LeetCode Python 3 judge.

```python
from __future__ import annotations

class Solution:

    def minMeetingRooms(self, intervals):
        start = sorted([i[0] for i in intervals])
        end = sorted([i[1] for i in intervals])
        res, count = (0, 0)
        s, e = (0, 0)
        while s < len(intervals):
            if start[s] < end[e]:
                s += 1
                count += 1
            else:
                e += 1
                count -= 1
            res = max(res, count)
        return res
```

## Complexity

$O(n\log n)$ time and $O(n)$ extra space. Bounds describe the implementation above and exclude required output unless stated otherwise.

## References & Useful Links

[^implementation]: [NeetCode contributors — Python reference for LC 253](https://github.com/neetcode-gh/leetcode/blob/d5ebb3ea8bd4b52d605bc7aa179e22af684d31bb/python/0253-meeting-rooms.py) — Source implementation reviewed on 18 October 2026; the walkthrough and illustrative example are written for this vault. Code is adapted where needed for the stated approach.

> [!info]- Reference implementation licence
> ![[Job Interviews/Coding Practice Index#Implementation Licence]]
