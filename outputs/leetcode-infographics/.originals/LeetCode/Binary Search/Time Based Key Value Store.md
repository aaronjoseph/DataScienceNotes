---
tags:
  - leetcode
problem_number: 981
difficulty: "Medium"
pattern: "Binary Search"
languages:
  - Python
---

## Template

### Python

Adapted reference implementation for the LeetCode Python 3 judge.

```python
from __future__ import annotations

class TimeMap:

    def __init__(self):
        self.keyStore = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keyStore:
            self.keyStore[key] = []
        self.keyStore[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res, values = ('', self.keyStore.get(key, []))
        l, r = (0, len(values) - 1)
        while l <= r:
            m = (l + r) // 2
            if values[m][1] <= timestamp:
                res = values[m][0]
                l = m + 1
            else:
                r = m - 1
        return res
```

## Complexity

Set is amortized $O(1)$; get is $O(\log m)$ for `m` versions of that key; total storage is $O(N)$ assignments. Bounds describe the implementation above and exclude required output unless stated otherwise.

## Overview

Store timestamped values and retrieve the latest value at or before a requested time.[^implementation]

Problem link: [[Job Interviews/Coding Practice Index#^lc981|LeetCode — LC 981]] · Completion: [[Action-Plan Kanban#Coding Backlog|Coding Backlog]].

## How to Solve

1. For each key, append timestamped values; the problem supplies increasing set timestamps.
2. During get, binary search that key's history.
3. Save a candidate whenever its timestamp is no greater than the query and continue right for a newer candidate.

## Why It Works

All entries after a too-large timestamp are also too new; searching right after a valid entry finds the latest admissible one.

## Worked Example

**Illustrative input:** Set key x to a at time 2 and b at time 5.

**Trace:** A query at time 4 admits only the earlier assignment.

**Result:** Return `"a"`.

## Common Pitfalls

Return an empty string if the key or an early enough version is absent. Unordered writes require sorted insertion or another structure.

## Related Notes

- [[Job Interviews/Coding Practice Index#^lc981|Coding Practice Index — Time Based Key Value Store]] — Central problem URL and solution navigation.
- [[Action-Plan Kanban#Coding Backlog|Coding Backlog]] — Mark practice completion on the board.
- [[LeetCode/Binary Search/Binary Search|Binary Search]] — Search templates and boundary invariants.

## References & Useful Links

[^implementation]: [NeetCode contributors — Python reference for LC 981](https://github.com/neetcode-gh/leetcode/blob/d5ebb3ea8bd4b52d605bc7aa179e22af684d31bb/python/0981-time-based-key-value-store.py) — Source implementation reviewed on 18 October 2026; the walkthrough and illustrative example are written for this vault. Code is adapted where needed for the stated approach.

> [!info]- Reference implementation licence
> ![[Job Interviews/Coding Practice Index#Implementation Licence]]
