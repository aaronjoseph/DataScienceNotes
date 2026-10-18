---
tags:
  - leetcode
problem_number: 1899
difficulty: "Medium"
pattern: "Greedy"
languages:
  - Python
---

Determine whether repeated coordinatewise-maximum merges of triplets can produce the target.[^implementation]

Problem link: [[Job Interviews/Coding Practice Index#^lc1899|LeetCode — LC 1899]] · Completion: [[Action-Plan Kanban#Coding Backlog|Coding Backlog]].

## How to Solve

1. Discard any triplet exceeding the target in any coordinate.
2. For each remaining triplet, mark coordinates that equal the corresponding target coordinate.
3. Accept if all three coordinates are covered by eligible triplets.

## Why It Works

Eligible triplets can never overshoot the target, and merging a set covering every coordinate reaches the target exactly.

## Worked Example

**Illustrative input:** Triplets `[[2, 1, 3], [1, 4, 2]]`, target `[2, 4, 3]`.

**Trace:** The first supplies coordinates zero and two; the second supplies coordinate one.

**Result:** Return `True`.

## Python

Adapted reference implementation for the LeetCode Python 3 judge.

```python
from __future__ import annotations
from typing import List

class Solution:

    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        good = set()
        for t in triplets:
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue
            for i, v in enumerate(t):
                if v == target[i]:
                    good.add(i)
        return len(good) == 3
```

## Complexity

$O(n)$ time and $O(1)$ extra space. Bounds describe the implementation above and exclude required output unless stated otherwise.

## Common Pitfalls

A coordinate match from an overshooting triplet cannot be used. Merges take coordinatewise maxima rather than sums.

## Related Notes

- [[Job Interviews/Coding Practice Index#^lc1899|Coding Practice Index — Merge Triplets to Form Target Triplet]] — Central problem URL and solution navigation.
- [[Action-Plan Kanban#Coding Backlog|Coding Backlog]] — Mark practice completion on the board.

## References & Useful Links

[^implementation]: [NeetCode contributors — Python reference for LC 1899](https://github.com/neetcode-gh/leetcode/blob/d5ebb3ea8bd4b52d605bc7aa179e22af684d31bb/python/1899-merge-triplets-to-form-target-triplet.py) — Source implementation reviewed on 18 October 2026; the walkthrough and illustrative example are written for this vault. Code is adapted where needed for the stated approach.

> [!info]- Reference implementation licence
> ![[Job Interviews/Coding Practice Index#Implementation Licence]]
