---
tags:
  - "leetcode"
  - "binary-search"
problem_number: 875
difficulty: "Medium"
pattern: "Binary search on the answer"
languages:
  - "Python"
  - "Rust"
problem_url: "https://leetcode.com/problems/koko-eating-bananas/"
time_complexity: "O(n log M)"
space_complexity: "O(1)"
---

Koko Eating Bananas is a **binary search** problem, not a binary tree problem. The technique is *binary search on the answer*: search over possible speeds instead of over an array index.

## Problem

- There are `piles` of bananas and `h` hours.
- Koko chooses one speed `k` (bananas per hour) for the whole time.
- Each hour she eats up to `k` bananas from **one** pile; if the pile has fewer, she finishes it and waits for the next hour.
- Return the **minimum** `k` that lets her finish within `h` hours.

## Key Concepts

### Hours at a Given Speed

A pile of $p$ bananas takes $\lceil p / k \rceil$ hours at speed $k$, so the total is:

$$
\text{hours}(k) = \sum_{i} \left\lceil \frac{p_i}{k} \right\rceil
$$

Compute the ceiling with integers to avoid floating-point error:

$$
\left\lceil \frac{p}{k} \right\rceil = \left\lfloor \frac{p + k - 1}{k} \right\rfloor
$$

### Monotonicity

A faster speed never needs more hours, so feasibility looks like this as $k$ increases:

```text
k:        1  2  3  4  5  6 ...
feasible: F  F  F  T  T  T ...
```

Any false-then-true pattern like this can be searched with binary search for the **first true**.

### Search Range

- **Lower bound:** $k = 1$.
- **Upper bound:** $k = \max(p_i)$. At that speed each pile takes exactly one hour, and the problem guarantees `h >= len(piles)`.

### Template: First True

```text
lo, hi = 1, max(piles)
while lo < hi:
    mid = (lo + hi) // 2
    if feasible(mid): hi = mid       # mid may be the answer; keep it
    else:            lo = mid + 1    # mid is too slow; discard it
return lo
```

**Complexity:** $O(n \log M)$ time with $n$ piles and $M = \max(p_i)$; $O(1)$ extra space.

## Worked Example

**Inputs:** `piles = [3, 6, 7, 11]`, `h = 8`.

**Step 1: try k = 4.**

$$
\left\lceil \tfrac{3}{4} \right\rceil + \left\lceil \tfrac{6}{4} \right\rceil + \left\lceil \tfrac{7}{4} \right\rceil + \left\lceil \tfrac{11}{4} \right\rceil = 1 + 2 + 2 + 3 = 8
$$

**Step 2: try k = 3.**

$$
1 + 2 + 3 + 4 = 10
$$

At k = 4 she needs 8 hours, which fits; at k = 3 she needs 10, which does not. The answer is **4**.

## Python

```python
from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def hours(k: int) -> int:
            return sum((p + k - 1) // k for p in piles)

        lo, hi = 1, max(piles)
        while lo < hi:
            mid = (lo + hi) // 2
            if hours(mid) <= h:
                hi = mid
            else:
                lo = mid + 1
        return lo
```

## Rust

```rust
impl Solution {
    pub fn min_eating_speed(piles: Vec<i32>, h: i32) -> i32 {
        // i64: total hours can exceed i32 when k is small.
        let hours = |k: i64| -> i64 {
            piles.iter().map(|&p| (p as i64 + k - 1) / k).sum()
        };

        let (mut lo, mut hi) = (1i64, *piles.iter().max().unwrap() as i64);
        while lo < hi {
            let mid = lo + (hi - lo) / 2;
            if hours(mid) <= h as i64 {
                hi = mid;
            } else {
                lo = mid + 1;
            }
        }
        lo as i32
    }
}
```

- **Overflow:** up to $10^4$ piles of up to $10^9$ bananas, so at k = 1 the hour total overflows `i32`.
- **Midpoint:** `lo + (hi - lo) / 2` avoids overflow in `lo + hi`.

## Common Pitfalls

- Float division for the ceiling can round wrongly.
- Starting `lo` at 0 divides by zero.
- Using `hi = mid - 1` when `mid` is feasible can skip the answer.

## Related Problems

- TODO: Capacity To Ship Packages Within D Days (1011).
- TODO: Split Array Largest Sum (410).
- TODO: Minimum Number of Days to Make m Bouquets (1482).

## Related Notes

- [[Big O]] — complexity notation used above.

## References & Useful Links

- [LeetCode 875: Koko Eating Bananas](https://leetcode.com/problems/koko-eating-bananas/) — Problem statement and constraints.
