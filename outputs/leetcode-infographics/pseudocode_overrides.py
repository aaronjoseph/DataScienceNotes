"""Compact logical forms for implementations with substantial class scaffolding."""
OVERRIDES = {
146: '''initialize capacity, keyToNode map, and empty recency list

function get(key):
    if key is not in keyToNode: return -1
    move keyToNode[key] to the most-recent end
    return its value

function put(key, value):
    if key already exists: detach its old node
    create and map the replacement node
    append it to the most-recent end
    if number of cached keys exceeds capacity:
        detach the least-recent real node
        remove that node's key from the map

detach and append update only neighboring list pointers''',
208: '''initialize root as an empty trie node

function insert(word):
    node = root
    for each character in word:
        create its child if missing
        node = that child
    mark node as a complete word

function follow(text):
    start at root; follow each character's child
    return null if a required child is missing
    return the final node

search(word): follow(word) exists and is a complete word
startsWith(prefix): follow(prefix) exists''',
211: '''initialize an empty trie
addWord(word): insert its characters; mark the final node

function search(pattern):
    return match(root, 0)

function match(node, index):
    if index equals pattern length:
        return node marks a complete word
    if pattern[index] is not '.':
        child = the matching character child
        return child exists and match(child, index + 1)
    for each existing child:
        if match(child, index + 1): return true
    return false''',
212: '''build a trie of words, with live-word prefix counts
results = empty set

function explore(row, col, trieNode, prefix, usedCells):
    reject out-of-bounds or already-used cells
    follow the board character's trie edge
    reject missing or exhausted prefixes
    mark this cell used; extend prefix
    if the trie node marks a word:
        add prefix to results once
        clear its terminal marker
        decrease that word's live prefix counts
    explore each of the four adjacent cells
    unmark this cell when returning

for each board cell:
    explore from the trie root and an empty path
return results as a list''',
355: '''store timestamped tweet lists and followed-user sets

postTweet(user, tweet): append with a new timestamp
follow(user, other): add other to user's followed set
unfollow(user, other): discard other from that set

function getNewsFeed(user):
    sources = user's followed users plus user
    heap = latest tweet from each nonempty source
    heapify by newest timestamp first
    feed = empty list
    while heap is not empty and feed has fewer than 10:
        pop the newest tweet and append its ID
        if its source has an older tweet:
            push that previous tweet from the source
    return feed''',
}
