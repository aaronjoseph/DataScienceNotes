# Big O

#search-eng

## What It Means

$f(n)=O(g(n))$ means an eventual upper bound up to a constant factor: there exist $c>0$ and $n_0$ such that $0\le f(n)\le c g(n)$ for $n\ge n_0$. $\Theta$ gives a tight asymptotic bound; $\Omega$ gives a lower bound.

Big O does not itself mean “worst case”. First identify the quantity being bounded: worst-case runtime, expected runtime, amortised operation cost, or memory. Then state the input size and computational model.

## Examples

| Operation | Typical bound and conditions |
|---|---|
| Array indexing | $O(1)$ under a random-access model |
| Binary search | $O(\log n)$ comparisons on sorted random-access data |
| Insertion sort | $O(n^2)$ worst case; $O(n)$ on already sorted input with the usual implementation |
| Quicksort | Expected $O(n\log n)$ with suitable randomisation; $O(n^2)$ worst case |
| Hash lookup | Expected $O(1)$ under suitable hashing/load assumptions; not a universal worst-case guarantee |

## Search Cost Models

An exact scan of $N$ dense vectors of dimension $d$ performs $O(Nd)$ distance work. Maintaining a size-$k$ heap while scanning scores adds $O(N\log k)$ comparison work for $k\ge2$. An inverted-index query depends on postings visited, query terms, skipping, and scoring; saying all search is $O(\log N)$ hides the algorithm.

Approximation changes the retrieval-quality contract as well as runtime; see [[Approximate Nearest Neighbours]]. Latency also depends on allocation, cache locality, I/O, parallelism, and queueing. Asymptotic bounds alone do not predict a benchmark result.

## Exercise

Double corpus size while holding vector dimension fixed, then double dimension alone. Predict exact distance-computation growth before measuring. Compare with [[Latency vs Throughput]] and [[System Design]].

## References & Useful Links

- [NIST big-O notation](https://xlinux.nist.gov/dads/HTML/bigOnotation.html) — Formal bound definition.

Previously saved resources (retained for further reading; not used to verify this revision):
- [www.bigocheatsheet.com — saved page](https://www.bigocheatsheet.com/)
