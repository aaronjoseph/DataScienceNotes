---
tags:
  - leetcode
problem_number: 355
difficulty: "Medium"
pattern: "Heap / Priority Queue"
languages:
  - Python
---

## Algorithm at a glance

![[Attachements/LeetCode/LC0355 - Design Twitter.png|700]]

## Overview

Design posting, following, unfollowing, and the ten most recent visible tweets. Merge the heads of relevant tweet histories.[^implementation]

Problem link: [[Job Interviews/Coding Practice Index#^lc355|LeetCode — LC 355]] · Completion: [[Action-Plan Kanban#Coding Backlog|Coding Backlog]].

## How to Solve

1. Store each user's tweets in time order and followees in a set.
2. For a feed, seed a heap with the latest tweet from each followed user and the requester.
3. Pop the newest candidate, then push the previous tweet from that same history; stop after ten.

## Why It Works

Each history is sorted, so merging their current heads always exposes the newest remaining visible tweet.

## Worked Example

**Illustrative input:** User 1 follows user 2. User 1 posts tweet 10, then user 2 posts tweet 20.

**Trace:** Both histories seed the feed heap; tweet 20 is newer.

**Result:** Return `[20, 10]`.

## Common Pitfalls

Always include the requester's own tweets and avoid duplicate histories. This interview design retains all posted tweets in memory.

## Related Notes

- [[Job Interviews/Coding Practice Index#^lc355|Coding Practice Index — Design Twitter]] — Central problem URL and solution navigation.
- [[Action-Plan Kanban#Coding Backlog|Coding Backlog]] — Mark practice completion on the board.

## Template

### Python

Adapted reference implementation for the LeetCode Python 3 judge.

```python
from __future__ import annotations
from typing import List
import heapq
from collections import defaultdict

class Twitter:

    def __init__(self):
        self.count = 0
        self.tweetMap = defaultdict(list)
        self.followMap = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId])
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []
        self.followMap[userId].add(userId)
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                index = len(self.tweetMap[followeeId]) - 1
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])
        while minHeap and len(res) < 10:
            count, tweetId, followeeId, index = heapq.heappop(minHeap)
            res.append(tweetId)
            if index >= 0:
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
```

## Complexity

Posting and follow changes take expected amortized $O(1)$ time. Feed construction takes $O(F\log(F+1))$ plus at most ten heap pops; heap space is $O(F)$. Total storage includes tweets and follow relationships. Bounds describe the implementation above and exclude required output unless stated otherwise.

## References & Useful Links

[^implementation]: [NeetCode contributors — Python reference for LC 355](https://github.com/neetcode-gh/leetcode/blob/d5ebb3ea8bd4b52d605bc7aa179e22af684d31bb/python/0355-design-twitter.py) — Source implementation reviewed on 18 October 2026; the walkthrough and illustrative example are written for this vault. Code is adapted where needed for the stated approach.

> [!info]- Reference implementation licence
> ![[Job Interviews/Coding Practice Index#Implementation Licence]]
