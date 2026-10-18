---
tags:
  - leetcode
problem_number: 239
difficulty: "Hard"
pattern: "Sliding Window"
languages:
  - Python
---

Return the maximum in every length-k window. Keep a deque of indices whose values decrease from front to back.[^implementation]

Problem link: [[Job Interviews/Coding Practice Index#^lc239|LeetCode — LC 239]] · Completion: [[Action-Plan Kanban#Coding Backlog|Coding Backlog]].

## How to Solve

1. Remove trailing deque indices with values smaller than the incoming value, then append its index.
2. Remove the front index when it falls left of the window.
3. Once a full window exists, output the value at the front.

## Why It Works

A newer, larger value outlives every smaller value it removes, so none of those removed candidates can become a future maximum.

## Worked Example

**Illustrative input:** `nums = [1, 3, 2, 5]`, `k = 2`.

**Trace:** Window maxima are 3, 3, then 5.

**Result:** Return `[3, 3, 5]`.

## Python

Adapted reference implementation for the LeetCode Python 3 judge.

```python
from __future__ import annotations
from typing import List
import collections

class Solution:

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        q = collections.deque()
        l = r = 0
        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)
            if l > q[0]:
                q.popleft()
            if r + 1 >= k:
                output.append(nums[q[0]])
                l += 1
            r += 1
        return output
```

## Complexity

$O(n)$ time and $O(k)$ auxiliary space, excluding output. Bounds describe the implementation above and exclude required output unless stated otherwise.

## Common Pitfalls

Store indices so expiration is detectable. Each index enters and leaves the deque at most once.

## Related Notes

- [[Job Interviews/Coding Practice Index#^lc239|Coding Practice Index — Sliding Window Maximum]] — Central problem URL and solution navigation.
- [[Action-Plan Kanban#Coding Backlog|Coding Backlog]] — Mark practice completion on the board.

## References & Useful Links

[^implementation]: [NeetCode contributors — Python reference for LC 239](https://github.com/neetcode-gh/leetcode/blob/d5ebb3ea8bd4b52d605bc7aa179e22af684d31bb/python/0239-sliding-window-maximum.py) — Source implementation reviewed on 18 October 2026; the walkthrough and illustrative example are written for this vault. Code is adapted where needed for the stated approach.

> [!info]- Reference implementation licence
> ![[Job Interviews/Coding Practice Index#Implementation Licence]]
