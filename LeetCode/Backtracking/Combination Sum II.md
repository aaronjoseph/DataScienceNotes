---
tags:
  - leetcode
problem_number: 40
difficulty: "Medium"
pattern: "Backtracking"
languages:
  - Python
---

Find unique combinations summing to a target when each candidate occurrence can be used at most once.[^implementation]

Problem link: [[Job Interviews/Coding Practice Index#^lc40|LeetCode — LC 40]] · Completion: [[Action-Plan Kanban#Coding Backlog|Coding Backlog]].

## How to Solve

1. Sort candidates and maintain a path, starting index, and remaining target.
2. Loop through candidate choices, skipping values already tried at the same depth.
3. Recurse from the next index after choosing an occurrence, then undo it; record a path at remaining target zero.

## Why It Works

Increasing indices prevent reuse, and same-depth duplicate skipping removes equivalent value combinations without excluding valid repeated occurrences.

## Worked Example

**Illustrative input:** `candidates = [1, 1, 2]`, `target = 2`.

**Trace:** One path uses both 1 occurrences; another uses the single 2.

**Result:** Return `[[1, 1], [2]]`.

## Python

Adapted reference implementation for the LeetCode Python 3 judge.

```python
from __future__ import annotations
from typing import List

class Solution:

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def backtrack(cur, pos, target):
            if target == 0:
                res.append(cur.copy())
                return
            if target <= 0:
                return
            prev = -1
            for i in range(pos, len(candidates)):
                if candidates[i] == prev:
                    continue
                cur.append(candidates[i])
                backtrack(cur, i + 1, target - candidates[i])
                cur.pop()
                prev = candidates[i]
        backtrack([], 0, target)
        return res
```

## Complexity

$O(n2^n)$ conservative worst-case time including output copies; $O(n)$ auxiliary space. Bounds describe the implementation above and exclude required output unless stated otherwise.

## Common Pitfalls

Skip duplicates only at the same recursion depth. Moving to the next index distinguishes this from unlimited-use Combination Sum.

## Related Notes

- [[Job Interviews/Coding Practice Index#^lc40|Coding Practice Index — Combination Sum II]] — Central problem URL and solution navigation.
- [[Action-Plan Kanban#Coding Backlog|Coding Backlog]] — Mark practice completion on the board.

## References & Useful Links

[^implementation]: [NeetCode contributors — Python reference for LC 40](https://github.com/neetcode-gh/leetcode/blob/d5ebb3ea8bd4b52d605bc7aa179e22af684d31bb/python/0040-combination-sum-ii.py) — Source implementation reviewed on 18 October 2026; the walkthrough and illustrative example are written for this vault. Code is adapted where needed for the stated approach.

> [!info]- Reference implementation licence
> ![[Job Interviews/Coding Practice Index#Implementation Licence]]
