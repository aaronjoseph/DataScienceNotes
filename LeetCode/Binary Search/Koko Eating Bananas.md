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

## Template

### Template: First True

```text
lo, hi = 1, max(piles)
while lo < hi:
    mid = (lo + hi) // 2
    if feasible(mid): hi = mid       # mid may be the answer; keep it
    else:            lo = mid + 1    # mid is too slow; discard it
return lo
```

**Complexity:** $O(n \log M)$ time, where $n$ is the number of piles and $M$ is the largest pile size; $O(1)$ extra space.

## Complexity

Each feasibility check visits $n$ piles and uses a constant-size integer accumulator. Binary search makes $O(\log M)$ checks for largest pile size $M$, giving $O(n\log M)$ total time and $O(1)$ auxiliary space in the Python and Rust implementations.

> [!info]- Why is the time complexity O(n log M)?
> There are two pieces of work: **checking one speed** and **deciding how many speeds to check**.
>
> **Example inputs:** `piles = [3, 6, 7, 11]`, `h = 8`. Here, $n = 4$ piles and $M = 11$, the largest pile size.
>
> **1. Checking one speed takes O(n).** For a candidate speed, calculate the required hours for every pile and add them:
>
> ```python
> def hours(k):
>     return sum((p + k - 1) // k for p in piles)
> ```
>
> At $k = 4$, the four piles require `[1, 2, 2, 3]` hours. The check visits all $n$ piles, doing constant work per pile under the problem's bounded-integer assumptions.
>
> **2. Binary search checks O(log M) speeds.** The candidate speeds range from 1 through $M$. Each iteration removes approximately half the remaining candidates. For this example, the candidate counts shrink as follows:
>
> ```text
> 11 → 6 → 3 → 2 → 1
> ```
>
> Repeated halving gives a logarithmic number of checks. Roughly one million candidate speeds require only about 20 checks:
>
> $$
> 2^{20} = 1{,}048{,}576
> $$
>
> **3. Multiply the costs.** Every speed check scans all the piles:
>
> $$
> \text{total checking work}
> = \text{number of speed checks} \times \text{work per check}
> $$
>
> $$
> O(\log M) \times O(n) = O(n\log M)
> $$
>
> In this example, binary search tries speeds **6, 3, 5, and 4**. Each attempt visits four piles:
>
> $$
> 4 \times 4 = 16\text{ pile calculations}
> $$
>
> Finding `max(piles)` initially also takes $O(n)$. Including that scan, a bound covering even $M = 1$ is:
>
> $$
> O\bigl(n(1+\log M)\bigr)
> $$
>
> For $M \ge 2$, this simplifies to the usual $O(n\log M)$. **Binary search halves the range of speeds; it still scans every pile to check each speed.**

## Overview

Koko Eating Bananas is a **binary search** problem, not a binary tree problem. The technique is *binary search on the answer*: search over possible speeds instead of over an array index.

## Problem

- There are `piles` of bananas and `h` hours.
- Koko chooses one speed `k` (bananas per hour) for the whole time.
- Each hour she eats up to `k` bananas from **one** pile; if the pile has fewer, she finishes it and waits for the next hour.
- Return the **minimum** `k` that lets her finish within `h` hours.

## How to Solve

1. Start with speeds from 1 through the largest pile. The problem guarantees at least one hour per pile, so the upper bound is feasible.
2. For a candidate speed, compute each pile's required hours using integer ceiling division and add them.
3. If the total fits within the allowed hours, retain that speed and search for a smaller feasible one; otherwise discard it and all slower speeds.
4. Stop when the lower and upper bounds meet. That speed is the minimum feasible answer.

## Key Concepts

### Hours at a Given Speed

Let $p_i$ be the positive size of pile $i$, $n$ the number of piles, and $k > 0$ the integer eating speed. Each pile occupies a whole number of hours, so the total is:

$$
\text{hours}(k) = \sum_{i=1}^{n} \left\lceil \frac{p_i}{k} \right\rceil
$$

Compute the ceiling with integers to avoid floating-point error:

$$
\left\lceil \frac{p}{k} \right\rceil = \left\lfloor \frac{p + k - 1}{k} \right\rfloor
$$

#### Why the Integer Ceiling Works

Integer division rounds **down**. Adding $k - 1$ first pushes any value with a remainder past the next multiple of $k$, but never pushes an exact multiple past it. Write $p$ as a quotient $q$ and remainder $r$:

$$
p = qk + r, \qquad 0 \le r < k
$$

Then:

$$
p + k - 1 = qk + (r + k - 1)
$$

- **Case $r = 0$:** the added remainder stays below one full divisor, so the floor is $q$, which equals the ceiling.
- **Case $1 \le r \le k - 1$:** the added remainder crosses one full divisor but stays below two, so the floor increases by exactly one, matching the ceiling.

**Check with k = 4:**

$$
p = 8: \quad \left\lfloor \frac{11}{4} \right\rfloor = 2
$$

$$
p = 9: \quad \left\lfloor \frac{12}{4} \right\rfloor = 3
$$

$$
p = 11: \quad \left\lfloor \frac{14}{4} \right\rfloor = 3
$$

These results match the exact division for 8 and the upward rounding required for 9 and 11.

**Why not `math.ceil(p / k)`?** A 64-bit float represents integers exactly only up to $2^{53}$, so for very large values the division can be slightly off and the ceiling wrong by one. Koko's limits ($p \le 10^9$) are safe for this floating-point calculation, but integer division avoids floating-point rounding. In fixed-width arithmetic, widen before adding the numerator terms, or use an overflow-safe ceiling-division primitive. Equivalent idioms, both assuming $p \ge 0$ and $k > 0$:

```python
-(-p // k)
```

```rust
let hours = (p as u64).div_ceil(k as u64);
```

### Monotonicity

A faster speed never needs more hours, so feasibility looks like this as $k$ increases:

```text
k:        1  2  3  4  5  6 ...
feasible: F  F  F  T  T  T ...
```

Any false-then-true pattern like this can be searched with binary search for the **first true**.

### Search Range

- **Lower bound:** $k = 1$.
- **Upper bound:** use the largest pile size. At that speed each pile takes exactly one hour, and the problem guarantees `h >= len(piles)`.

## Why It Works

A faster speed never increases any pile's required hours. Therefore, an infeasible midpoint rules out every slower speed, while a feasible midpoint lets the search keep that candidate and discard every larger candidate. The interval always contains the smallest feasible speed and strictly shrinks until only that speed remains.

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

### Iteration Trace

The Python solution below, run by hand on the same input. It starts with `lo = 1` and `hi = max(piles) = 11`.

**Iteration 1: range 1–11.**

$$
\text{mid} = \left\lfloor \frac{1 + 11}{2} \right\rfloor = 6
$$

**Hours at that speed:**

$$
\text{hours}(6) = 1 + 1 + 2 + 2 = 6
$$

6 ≤ 8, so speed 6 works; keep it and look lower: `hi = 6`.

**Iteration 2: range 1–6.**

$$
\text{mid} = \left\lfloor \frac{1 + 6}{2} \right\rfloor = 3
$$

**Hours at that speed:**

$$
\text{hours}(3) = 1 + 2 + 3 + 4 = 10
$$

10 > 8, so 3 and everything below it is too slow: `lo = 4`.

**Iteration 3: range 4–6.**

$$
\text{mid} = \left\lfloor \frac{4 + 6}{2} \right\rfloor = 5
$$

**Hours at that speed:**

$$
\text{hours}(5) = 1 + 2 + 2 + 3 = 8
$$

8 ≤ 8, so 5 works, but a smaller speed might too: `hi = 5`.

**Iteration 4: range 4–5.**

$$
\text{mid} = \left\lfloor \frac{4 + 5}{2} \right\rfloor = 4
$$

**Hours at that speed:**

$$
\text{hours}(4) = 1 + 2 + 2 + 3 = 8
$$

8 ≤ 8, so 4 works: `hi = 4`.

**End:** `lo = hi = 4`, so the loop stops and returns 4.

| Iter | lo | hi | mid | hours(mid) | ≤ 8? | Update |
|---|---|---|---|---|---|---|
| 1 | 1 | 11 | 6 | 6 | Yes | hi = 6 |
| 2 | 1 | 6 | 3 | 10 | No | lo = 4 |
| 3 | 4 | 6 | 5 | 8 | Yes | hi = 5 |
| 4 | 4 | 5 | 4 | 8 | Yes | hi = 4 |
| End | 4 | 4 | — | — | — | return 4 |

- The candidate range shrinks 11 → 6 → 3 → 2 → 1, about $\log_2 11 \approx 4$ iterations.
- `hi = mid` keeps a working speed because it may be the answer, as speed 4 was in iteration 4.
- `lo = mid + 1` is safe because a failing speed can never be the answer.
- Speeds 5 and 4 both need 8 hours; the search continues past 5 because it wants the **smallest** working speed.

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

- Floating-point ceiling can fail outside this problem's safe numeric range; integer ceiling division avoids that issue.
- Starting `lo` at 0 divides by zero.
- Using `hi = mid - 1` when `mid` is feasible can skip the answer.

## Related Problems

- TODO: Capacity To Ship Packages Within D Days (1011).
- TODO: Split Array Largest Sum (410).
- TODO: Minimum Number of Days to Make m Bouquets (1482).

## Related Notes

- [[Job Interviews/Coding Practice Index#^lc875|Coding Practice Index — LC 875]] — Problem entry in the complete NeetCode 150 collection.
- [[Action-Plan Kanban#Coding Backlog|Action-Plan Kanban — Coding Backlog]] — Track practice completion.
- [[LeetCode/Binary Search/Binary Search|Binary Search]] — Reusable search templates and monotonicity.
- [[Big O]] — complexity notation used above.

## References & Useful Links

- [[Job Interviews/Coding Practice Index#^lc875|LeetCode 875 — Koko Eating Bananas]] — Central problem URL and constraints.
- [NeetCode contributors — Koko Eating Bananas Python reference](https://github.com/neetcode-gh/leetcode/blob/d5ebb3ea8bd4b52d605bc7aa179e22af684d31bb/python/0875-koko-eating-bananas.py) — Binary-search approach reviewed on 18 October 2026; the implementations in this note retain integer ceiling division.
