---
tags:
  - "leetcode"
  - "binary-search"
problem_number: 704
difficulty: "Easy"
pattern: "Binary search"
languages:
  - "Python"
  - "Rust"
---

## Template

### Three Templates

#### 1. Exact Match in a Sorted Array

```python
def search(nums: list[int], target: int) -> int:
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1
```

#### 2. First True (Lower Bound): Minimise X

Use it when feasibility goes `F F F T T T`. Koko, ship capacity and bouquet days all use this.

```python
def first_true(lo: int, hi: int, feasible) -> int:
    while lo < hi:
        mid = (lo + hi) // 2
        if feasible(mid):
            hi = mid          # mid may be the answer
        else:
            lo = mid + 1
    return lo
```

#### 3. Last True: Maximise X

Use it when feasibility goes `T T T F F F`. Round `mid` **up**, or the loop never ends when `hi = lo + 1`.

```python
def last_true(lo: int, hi: int, feasible) -> int:
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if feasible(mid):
            lo = mid
        else:
            hi = mid - 1
    return lo
```

#### Rust: First True

```rust
fn first_true(mut lo: i64, mut hi: i64, feasible: impl Fn(i64) -> bool) -> i64 {
    while lo < hi {
        let mid = lo + (hi - lo) / 2; // avoids overflow in lo + hi
        if feasible(mid) {
            hi = mid;
        } else {
            lo = mid + 1;
        }
    }
    lo
}
```

These templates have not been run; they use the same loop as the Koko solution.

## Complexity

For the exact-match sorted-array template (LC 704): $O(\log n)$ time and $O(1)$ extra space, where $n$ is the number of array elements.

## Overview

Binary search solves a problem by repeatedly halving a range of candidates, where a single check tells you which half to discard. It works on a sorted array and, more generally, on any **monotonic** yes/no question. It is easy to confuse with a **binary tree**; the comparison below explains how to tell the two apart.

Problem link: [[Job Interviews/Coding Practice Index#^lc704|LeetCode — LC 704]] · Completion: [[Action-Plan Kanban#Coding Backlog|Coding Backlog]].

## LC 704 — Problem and Solution

Return the index of a target in an ascending sorted array, or -1 if absent.[^lc704]

### How to Solve

1. Set an inclusive range from the first through the last index.
2. Compare the middle value with the target and discard the midpoint plus the impossible half.
3. Return immediately on equality; return -1 after the range becomes empty.

### Why It Works

Sorted order makes every discarded value provably too small or too large.

### Worked Example

**Illustrative input:** `nums = [-3, 0, 4, 9]`, `target = 4`.

**Trace:** The first midpoint is 0, so keep indices 2 through 3; the next midpoint is 4.

**Result:** Return `2`.

### Python and Complexity

Use the exact-match implementation under **Three Templates → 1. Exact Match in a Sorted Array** above. $O(\log n)$ time and $O(1)$ extra space.

Use an inclusive loop with midpoint exclusion. The existing note also contains first-true and last-true templates with different rules.

## Binary Search vs Binary Tree

| | Binary search | Binary tree |
|---|---|---|
| What it is | An algorithm over a range | A data structure of nodes |
| Input looks like | Sorted array, or a numeric range of answers | `root: TreeNode` with `left` and `right` |
| Typical tools | `lo`, `hi`, `mid` | Recursion, DFS, BFS with a queue |
| Typical cost | $O(\log n)$ checks | $O(n)$ nodes visited |

They meet in a **binary search tree (BST)**: for every node, keys in the left subtree are smaller and keys in the right subtree are larger. Searching a BST halves the candidates at each step like binary search, but the cost is $O(h)$ for tree height $h$, which is $O(n)$ if the tree is unbalanced.

[[Koko Eating Bananas]] is a binary search problem: there is no tree in it.

## How to Spot a Binary Search Question

Look for one or more of these signals:

1. **Sorted input.** "Given a sorted array...", or a rotated sorted array. Asking for a position, first or last occurrence, or insertion point is a strong hint.
2. **"Minimum X such that..." or "maximum X such that...".** The problem asks for the smallest speed, capacity, days or distance that satisfies a condition.
3. **A monotonic check.** If `X` works, every larger `X` also works (or every smaller one). Feasibility then looks like `F F F T T T`, and you want the first `T`.
4. **A checker is easy, the answer is not.** You can't compute the answer directly, but given a candidate you can test it in $O(n)$.
5. **Large value ranges.** Values up to $10^9$ with $n$ up to $10^5$ rule out trying every value, but $O(n \log M)$ fits, where $M$ is the value range.
6. **"Kth smallest" or median** over sorted structures, or over a value range where you can count elements at most `mid`.

**Not a fit:** the check is not monotonic, or the data is unsorted and you need an exact element (use a hash map instead).

## How to Spot a Binary Tree Question

For contrast:

- The function receives `root` and a `TreeNode` class is defined.
- It asks about depth, paths, subtrees, ancestors, levels, or the shape of the tree.
- Solutions are usually DFS (recursion on `left` and `right`) or BFS (level by level with a queue).

TODO: create a separate `LeetCode/Binary Tree/` note with traversal templates.

## Worked Example: Is It Monotonic?

**Problem:** the minimum ship capacity to deliver weights `[1, 2, 3]` within 2 days.

**Step 1: capacity 3.** Day 1 carries 1 + 2, day 2 carries 3, so it fits in 2 days: feasible.

**Step 2: capacity 2.** Day 1 carries 1, day 2 carries 2, and 3 cannot be carried at all: infeasible.

**Step 3: any capacity above 3** also works, because a bigger ship never needs more days.

Feasibility is `F T T T...` from capacity 2 upwards, so "first true" applies and the answer is 3. The search range is from the heaviest item (smallest possible capacity) to the total weight (one day).

## Common Pitfalls

- Choosing `lo` and `hi` that do not contain the answer.
- Mixing `while lo <= hi` with `hi = mid`, which can loop forever.
- Rounding `mid` down in the last-true template.
- Overflow in `lo + hi` in Rust, Java or C++.

## Practice Problems

- [[Koko Eating Bananas]] (875) — first true on eating speed.
- [[Job Interviews/Coding Practice Index#^lc704|Binary Search (704)]] — Exact-match solution in this note.
- TODO: Search Insert Position (35) — lower bound.
- TODO: Capacity To Ship Packages Within D Days (1011) — first true.
- [[LeetCode/Binary Search/Search In Rotated Sorted Array|Search In Rotated Sorted Array]] (33) — Sorted-half reasoning.
- TODO: Split Array Largest Sum (410) — first true.

## Related Notes

- [[Big O]] — $O(\log n)$ and $O(n \log M)$ costs.
- [[Job Interviews/Coding Practice Index#^lc704|Coding Practice Index — LC 704]] — Central LeetCode URL.
- [[Action-Plan Kanban#Coding Backlog|Coding Backlog]] — Practice completion.

## References & Useful Links

[^lc704]: [NeetCode contributors — Binary Search Python reference](https://github.com/neetcode-gh/leetcode/blob/d5ebb3ea8bd4b52d605bc7aa179e22af684d31bb/python/0704-binary-search.py) — Exact-match search implementation reviewed on 18 October 2026. The LC 704 walkthrough and example above are written for this vault.
