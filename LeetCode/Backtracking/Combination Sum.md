---
tags:
  - leetcode
problem_number: 39
difficulty: "Medium"
pattern: "Backtracking"
languages:
  - Python
---

List combinations of distinct positive candidates that sum to a target, allowing each candidate to be reused.[^implementation]

Problem link: [[Job Interviews/Coding Practice Index#^lc39|LeetCode — LC 39]] · Completion: [[Action-Plan Kanban#Coding Backlog|Coding Backlog]].

## How to Solve

1. At a candidate index, branch between taking it again and skipping to the next index.
2. Keep a mutable path and its running total.
3. Copy the path when the total reaches the target; stop when it exceeds the target or candidates end.

## Why It Works

Nondecreasing candidate indices generate each combination once, and positivity makes overshoot pruning safe.

## Worked Example

**Illustrative input:** `candidates = [2, 3]`, `target = 6`.

**Trace:** Repeatedly taking 2 gives one combination; skipping 2 allows two 3s.

**Result:** Return `[[2, 2, 2], [3, 3]]`.

## Python

Adapted reference implementation for the LeetCode Python 3 judge.

```python
from __future__ import annotations
from typing import List

class Solution:

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            if i >= len(candidates) or total > target:
                return
            cur.append(candidates[i])
            dfs(i, cur, total + candidates[i])
            cur.pop()
            dfs(i + 1, cur, total)
        dfs(0, [], 0)
        return res
```

## Complexity

Exponential time in the search depth, plus output copying. With `c` candidates and `D = target/min(candidates)`, a loose bound is $O(2^{c+D}(c+D))$ time and $O(c+D)$ auxiliary space. Bounds describe the implementation above and exclude required output unless stated otherwise.

## Common Pitfalls

Candidate positivity and uniqueness matter. After taking a candidate, remain at its index so reuse is allowed.

## Related Notes

- [[Job Interviews/Coding Practice Index#^lc39|Coding Practice Index — Combination Sum]] — Central problem URL and solution navigation.
- [[Action-Plan Kanban#Coding Backlog|Coding Backlog]] — Mark practice completion on the board.

## References & Useful Links

[^implementation]: [NeetCode contributors — Python reference for LC 39](https://github.com/neetcode-gh/leetcode/blob/d5ebb3ea8bd4b52d605bc7aa179e22af684d31bb/python/0039-combination-sum.py) — Source implementation reviewed on 18 October 2026; the walkthrough and illustrative example are written for this vault. Code is adapted where needed for the stated approach.

> [!info]- Reference implementation licence
> ![[Job Interviews/Coding Practice Index#Implementation Licence]]
