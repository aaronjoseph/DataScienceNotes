---
tags:
  - leetcode
problem_number: 621
difficulty: "Medium"
pattern: "Heap / Priority Queue"
languages:
  - Python
---

## Template

### Python

Adapted reference implementation for the LeetCode Python 3 judge.

```python
from __future__ import annotations
from typing import List
from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        if not counts:
            return 0
        highest = max(counts.values())
        tied = sum(count == highest for count in counts.values())
        forced_length = (highest - 1) * (n + 1) + tied
        return max(len(tasks), forced_length)
```

## Complexity

$O(n+u)$ time and $O(u)$ space for `u` task types, bounded by the fixed uppercase alphabet. Bounds describe the implementation above and exclude required output unless stated otherwise.

## Overview

Schedule tasks with a cooldown between equal task types, minimizing total elapsed slots.[^implementation]

Problem link: [[Job Interviews/Coding Practice Index#^lc621|LeetCode — LC 621]] · Completion: [[Action-Plan Kanban#Coding Backlog|Coding Backlog]].

## How to Solve

1. Count task types, find the maximum frequency, and count how many types reach it.
2. Build the lower bound formed by separated occurrences of the most frequent types.
3. Return the larger of that bound and the number of tasks; the extra tasks can fill otherwise idle slots.

## Why It Works

Repeated maximum-frequency tasks force separated blocks, while enough other tasks fill every gap without increasing the total.

## Worked Example

**Illustrative input:** Tasks `[A, A, A, B, B, B]`, cooldown 2.

**Trace:** A schedule is A B idle A B idle A B.

**Result:** Return `8`.

## Common Pitfalls

Cooldown 2 requires two intervening slots between identical types. Include all task types tied for maximum frequency.

## Related Notes

- [[Job Interviews/Coding Practice Index#^lc621|Coding Practice Index — Task Scheduler]] — Central problem URL and solution navigation.
- [[Action-Plan Kanban#Coding Backlog|Coding Backlog]] — Mark practice completion on the board.

## References & Useful Links

[^implementation]: [NeetCode contributors — Python reference for LC 621](https://github.com/neetcode-gh/leetcode/blob/d5ebb3ea8bd4b52d605bc7aa179e22af684d31bb/python/0621-task-scheduler.py) — Source implementation reviewed on 18 October 2026; the walkthrough and illustrative example are written for this vault. Code is adapted where needed for the stated approach.

> [!info]- Reference implementation licence
> ![[Job Interviews/Coding Practice Index#Implementation Licence]]
