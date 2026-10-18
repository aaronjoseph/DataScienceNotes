---
tags:
  - leetcode
problem_number: 125
difficulty: "Easy"
pattern: "Two Pointers"
languages:
  - Python
---

Check whether a string reads the same forward and backward after ignoring non-alphanumeric characters and case.[^implementation]

Problem link: [[Job Interviews/Coding Practice Index#^lc125|LeetCode — LC 125]] · Completion: [[Action-Plan Kanban#Coding Backlog|Coding Backlog]].

## How to Solve

1. Keep pointers at both ends.
2. Advance either pointer past punctuation or spaces.
3. Compare lowercase characters, reject a mismatch, and move both inward.

## Why It Works

Every significant outer pair must match; removing a matching pair leaves the same palindrome question on the interior.

## Worked Example

**Illustrative input:** `s = "A,b,a!"`.

**Trace:** Skip punctuation and compare a with a; b remains in the middle.

**Result:** Return `True`.

## Python

Adapted reference implementation for the LeetCode Python 3 judge.

```python
from __future__ import annotations

class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True
```

## Complexity

$O(n)$ time and $O(1)$ extra space with two pointers. Bounds describe the implementation above and exclude required output unless stated otherwise.

## Common Pitfalls

Python's alphanumeric checks support Unicode; state a normalization policy if extending beyond the problem's ASCII input.

## Related Notes

- [[Job Interviews/Coding Practice Index#^lc125|Coding Practice Index — Valid Palindrome]] — Central problem URL and solution navigation.
- [[Action-Plan Kanban#Coding Backlog|Coding Backlog]] — Mark practice completion on the board.

## References & Useful Links

[^implementation]: [NeetCode contributors — Python reference for LC 125](https://github.com/neetcode-gh/leetcode/blob/d5ebb3ea8bd4b52d605bc7aa179e22af684d31bb/python/0125-valid-palindrome.py) — Source implementation reviewed on 18 October 2026; the walkthrough and illustrative example are written for this vault. Code is adapted where needed for the stated approach.

> [!info]- Reference implementation licence
> ![[Job Interviews/Coding Practice Index#Implementation Licence]]
