---
tags:
  - leetcode
  - linked-list
problem_number: 287
difficulty: "Medium"
pattern: "Linked List"
languages:
  - Python
---

## Template

### Python

Adapted reference implementation for the LeetCode Python 3 judge.[^implementation]

```python
from __future__ import annotations
from typing import List

class Solution:

    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = (0, 0)
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow
```

## Complexity

- **Time:** $O(n)$ worst-case, where `len(nums)` is $n + 1$. Both Floyd phases traverse each node a constant number of times.
- **Auxiliary space:** $O(1)$, using only three integer index pointers (`slow`, `fast`, `slow2`) without modifying `nums`.

## Algorithm at a glance

![[Attachements/LeetCode/LC0287 - Find The Duplicate Number.png|700]]

## Overview

Given an array `nums` of $n + 1$ integers where every value lies in $[1, n]$, find the single repeated integer without modifying `nums` and using $O(1)$ extra space.[^implementation] Viewing `i → nums[i]` as a linked-list `next` pointer turns the array into a functional graph whose cycle entry is the duplicate value, extending [[LeetCode/Linked List/Linked List Cycle|Linked List Cycle]] (LC 141).

Problem link: [[Job Interviews/Coding Practice Index#^lc287|LeetCode — LC 287]] · Completion: [[Action-Plan Kanban#Coding Backlog|Coding Backlog]].

## Key Concepts

### Why the Array Forms a Linked List With a Cycle

- Every index $i \in \{0, \dots, n\}$ has an outgoing edge to `nums[i]`, which is a valid index in $\{1, \dots, n\}$.
- Because no element equals $0$, index $0$ has **in-degree 0** (it can never be part of a cycle), so starting at $0$ always enters a tail leading into a cycle.
- By the pigeonhole principle, at least two distinct indices point to the same value $d$ (the duplicate), so $d$ has in-degree $\ge 2$ — making $d$ the **cycle entry**.

### Why Phase 2 Meets at the Cycle Entry

Let $p$ be the distance from index $0$ to the cycle entry, $c$ the cycle length, and $x$ the distance from the Phase 1 meeting point forward to the cycle entry. When `slow` and `fast` first meet, `fast` has travelled twice as far as `slow`, so:

$$
2(p + c - x) = p + k c + (c - x)
$$

for some positive integer $k$ (full laps). Rearranging gives:

$$
p = (k - 1)c + x
$$

Therefore, advancing `slow2` from $0$ and `slow` from the meeting point at $1$ step each guarantees they meet at the cycle entry after exactly $p$ steps.

## How to Solve

1. **Phase 1 (find intersection inside the cycle):** Start `slow = 0`, `fast = 0`. Repeatedly move `slow = nums[slow]` and `fast = nums[nums[fast]]` until `slow == fast`.
2. **Phase 2 (find cycle entry):** Start `slow2 = 0`. Advance both `slow = nums[slow]` and `slow2 = nums[slow2]` one step at a time until `slow == slow2`.
3. Return `slow` (the duplicate value).

## Why It Works

Phase 1 is guaranteed to terminate because the functional graph from index $0$ is finite and has no dead ends. Phase 2 exploits the distance identity above so the two pointers collide at the unique node reachable from $0$ with two incoming edges — the repeated integer.

## Worked Example

**Inputs:** `nums = [1, 3, 4, 2, 2]`.

Index graph from `0`: `0 → 1 → 3 → 2 → 4 → 2…` (cycle is `2 → 4 → 2`, entry is `2`).

1. **Phase 1 (`slow = 0`, `fast = 0`):**
   - Step 1: `slow = 1`, `fast = nums[1] = 3`.
   - Step 2: `slow = 3`, `fast = nums[2] = 4`.
   - Step 3: `slow = 2`, `fast = nums[2] = 4` (from `4 → 2 → 4`).
   - Step 4: `slow = 4`, `fast = 4`. Meet at `4`!
2. **Phase 2 (`slow = 4`, `slow2 = 0`):**
   - Step 1: `slow = nums[4] = 2`, `slow2 = nums[0] = 1`.
   - Step 2: `slow = nums[2] = 4`, `slow2 = nums[1] = 3`.
   - Step 3: `slow = nums[4] = 2`, `slow2 = nums[3] = 2`. Meet at `2`!

**Outcome:** Returns `2`.

## Common Pitfalls

- **Returning the Phase 1 meeting point:** `slow` and `fast` met at `4` in the example above, not at the duplicate `2`. Phase 2 is required.
- **Starting at `nums[0]` instead of `0` without matching Phase 2:** Both `slow`, `fast`, and `slow2` must start from the same origin (`0`) for the distance identity $p = (k - 1)c + x$ to hold.
- **Assuming this works for arbitrary value ranges:** The reduction depends strictly on values being in $[1, n]$ (no `0` values and no out-of-bounds indices) and on only one value being duplicated (possibly more than twice).

## Related Notes

- [[LeetCode/Linked List/Linked List Cycle|Linked List Cycle]] — Phase 1 (Floyd's cycle detection) on an explicit linked list.
- [[Job Interviews/Coding Practice Index#^lc287|Coding Practice Index — Find The Duplicate Number]] — Central problem URL and solution navigation.
- [[Action-Plan Kanban#Coding Backlog|Coding Backlog]] — Mark practice completion on the board.

## References & Useful Links

[^implementation]: [NeetCode contributors — Python reference for LC 287](https://github.com/neetcode-gh/leetcode/blob/d5ebb3ea8bd4b52d605bc7aa179e22af684d31bb/python/0287-find-the-duplicate-number.py) — Source implementation reviewed on 18 October 2026; the walkthrough and illustrative example are written for this vault. Code is adapted where needed for the stated approach.

> [!info]- Reference implementation licence
> ![[Job Interviews/Coding Practice Index#Implementation Licence]]
