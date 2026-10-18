"""Validate study-note links, examples, and selected edge cases; no LeetCode submission."""
from pathlib import Path
import ast
import copy
import itertools
import json
import random
import re
import yaml

ROOT = Path(__file__).resolve().parents[1]
BASE = json.loads((ROOT / 'outputs/coding-backlog-sources.json').read_text())
INDEX_PATH = ROOT / 'Job Interviews/Coding Practice Index.md'
BOARD_PATH = ROOT / 'Action-Plan Kanban.md'
index, board = INDEX_PATH.read_text(), BOARD_PATH.read_text()
notes, environments = {}, {}

class ListNode:
    def __init__(self, val=0, next=None):
        self.val, self.next = val, next

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right

class JudgeNode:
    def __init__(self, val=0, neighbors=None, next=None, random=None):
        self.val = val
        self.neighbors = [] if neighbors is None else neighbors
        self.next, self.random = next, random

def linked(values):
    head = None
    for value in reversed(values):
        head = ListNode(value, head)
    return head

def values(head):
    output = []
    while head:
        assert len(output) < 100, 'Unexpected list cycle'
        output.append(head.val)
        head = head.next
    return output

for path in (ROOT / 'LeetCode').rglob('*.md'):
    text = path.read_text()
    props = yaml.safe_load(text.split('---', 2)[1])
    number = props['problem_number']
    assert number not in notes
    notes[number] = path
    assert isinstance(props['tags'], list) and 'leetcode' in props['tags']
    assert f'Coding Practice Index#^lc{number}|' in text
    assert 'Action-Plan Kanban#Coding Backlog|' in text
    assert '## References & Useful Links' in text
    blocks = re.findall(r'```python\n(.*?)```', text, re.S)
    env = dict(ListNode=ListNode, TreeNode=TreeNode, Node=JudgeNode)
    for code in blocks:
        ast.parse(code)
        # Koko's small ceiling-division idiom is an expression, not a complete solution.
        if code.strip() == '-(-p // k)':
            continue
        exec(compile(code, str(path), 'exec'), env)
    environments[number] = env

expected_ids = {p['id'] for p in BASE['problems']}
assert set(notes) == expected_ids and len(notes) == 150
assert len(re.findall(r'\^lc\d+\s*$', index, re.M)) == 150
for problem in BASE['problems']:
    number = problem['id']
    line = next(line for line in index.splitlines() if line.endswith(f'^lc{number}'))
    assert problem['url'] in line
    assert str(notes[number].relative_to(ROOT).with_suffix('')) in line

def coding_section(text):
    return text.split('## Coding Backlog', 1)[1].split('\n## ', 1)[0]

states = lambda text: dict(re.findall(r'^- \[([^\]])\] \*\*LC (\d+)\*\*', coding_section(text), re.M))
def state_by_number(text):
    return {number: state for state, number in re.findall(r'^- \[([^\]])\] \*\*LC (\d+)\*\*', coding_section(text), re.M)}
assert state_by_number(board) == state_by_number(BASE['board'])
assert board.split('## Coding Backlog')[0] == BASE['board'].split('## Coding Backlog')[0]
assert board.split('## System Design Backlog')[1].rstrip() == BASE['board'].split('## System Design Backlog')[1].rstrip()
cards = re.split(r'(?=^- \[[^\]]\] \*\*LC \d+\*\*)', coding_section(board), flags=re.M)
for card in cards:
    match = re.match(r'- \[[^\]]\] \*\*LC (\d+)\*\*', card)
    if not match:
        continue
    number = int(match[1])
    assert str(notes[number].relative_to(ROOT).with_suffix('')) in card
    assert f'Coding Practice Index#^lc{number}|' in card

files_by_stem = {}
for path in ROOT.rglob('*.md'):
    if not any(part.startswith('.') or part == 'copilot' for part in path.relative_to(ROOT).parts):
        files_by_stem.setdefault(path.stem, []).append(path)
resolved_links = 0
for path in [*notes.values(), INDEX_PATH]:
    text = path.read_text()
    text = re.sub(r'```.*?```', '', text, flags=re.S)
    text = re.sub(r'`[^`\n]*`', '', text)
    for target in re.findall(r'!?\[\[([^\]|]+)(?:\|[^\]]*)?\]\]', text):
        name, _, fragment = target.partition('#')
        target_path = ROOT / (name if name.endswith('.md') else name + '.md')
        if not name:
            target_path = path
        elif not target_path.exists():
            matches = files_by_stem.get(name, [])
            assert len(matches) == 1, (path, target, matches)
            target_path = matches[0]
        target_text = target_path.read_text()
        if fragment.startswith('^'):
            assert re.search(re.escape(fragment) + r'\s*$', target_text, re.M), (path, target)
        elif fragment:
            assert fragment in re.findall(r'^#{1,6} (.+)$', target_text, re.M), (path, target)
        resolved_links += 1

def run(number, method, args):
    return getattr(environments[number]['Solution'](), method)(*copy.deepcopy(args))

# Representative examples, with order normalization where the problem permits it.
cases = {
217: ('containsDuplicate', [[4, 7, 4]], True),
242: ('isAnagram', ['aab', 'aba'], True),
1: ('twoSum', [[4, 2, 7], 9], [1, 2]),
238: ('productExceptSelf', [[2, 3, 4]], [12, 8, 6]),
128: ('longestConsecutive', [[10, 3, 1, 2, 2]], 3),
125: ('isPalindrome', ['A,b,a!'], True),
11: ('maxArea', [[1, 3, 2, 4]], 6),
167: ('twoSum', [[1, 2, 5, 8], 7], [2, 3]),
42: ('trap', [[3, 0, 2, 3]], 4),
121: ('maxProfit', [[7, 2, 5, 1, 4]], 3),
3: ('lengthOfLongestSubstring', ['abba'], 2),
424: ('characterReplacement', ['AABABBA', 1], 4),
76: ('minWindow', ['ADOBECODEBANC', 'ABC'], 'BANC'),
567: ('checkInclusion', ['ab', 'eidbaooo'], True),
239: ('maxSlidingWindow', [[1, 3, 2, 5], 2], [3, 3, 5]),
20: ('isValid', ['([)]'], False),
150: ('evalRPN', [['7', '2', '-']], 5),
739: ('dailyTemperatures', [[70, 70, 72]], [2, 1, 0]),
853: ('carFleet', [12, [10, 8, 0], [2, 4, 1]], 2),
84: ('largestRectangleArea', [[2, 1, 2]], 3),
153: ('findMin', [[4, 5, 1, 2, 3]], 1),
33: ('search', [[4, 5, 6, 1, 2, 3], 2], 4),
74: ('searchMatrix', [[[1, 3, 5], [7, 9, 11]], 9], True),
875: ('minEatingSpeed', [[3, 6, 7, 11], 8], 4),
4: ('findMedianSortedArrays', [[1, 3], [2]], 2),
287: ('findDuplicate', [[1, 3, 4, 2, 2]], 2),
215: ('findKthLargest', [[3, 1, 5, 5, 2], 2], 5),
1046: ('lastStoneWeight', [[2, 7, 4]], 1),
621: ('leastInterval', [list('AAABBB'), 2], 8),
79: ('exist', [[['A', 'B'], ['C', 'D']], 'ABD'], True),
200: ('numIslands', [[['1', '0'], ['0', '1']]], 2),
207: ('canFinish', [2, [[0, 1], [1, 0]]], False),
323: ('countComponents', [5, [[0, 1], [1, 2], [3, 4]]], 2),
261: ('validTree', [4, [[0, 1], [1, 2]]], False),
695: ('maxAreaOfIsland', [[[1, 1, 0], [0, 1, 1]]], 4),
994: ('orangesRotting', [[[2, 1, 1]]], 2),
1584: ('minCostConnectPoints', [[[0, 0], [2, 0], [2, 2]]], 4),
743: ('networkDelayTime', [[[1, 2, 2], [2, 3, 3], [1, 3, 9]], 3, 1], 5),
778: ('swimInWater', [[[0, 2], [1, 3]]], 3),
787: ('findCheapestPrice', [3, [[0, 1, 1], [1, 2, 1], [0, 2, 5]], 0, 2, 0], 5),
70: ('climbStairs', [4], 5),
198: ('rob', [[2, 7, 9, 3, 1]], 12),
213: ('rob', [[2, 3, 2]], 3),
5: ('longestPalindrome', ['cbbd'], 'bb'),
647: ('countSubstrings', ['aaa'], 6),
91: ('numDecodings', ['226'], 3),
322: ('coinChange', [[1, 3, 4], 6], 2),
152: ('maxProduct', [[-2, 3, -4]], 24),
139: ('wordBreak', ['applepenapple', ['apple', 'pen']], True),
300: ('lengthOfLIS', [[3, 1, 2, 4]], 3),
746: ('minCostClimbingStairs', [[10, 15, 20]], 15),
416: ('canPartition', [[1, 5, 11, 5]], True),
62: ('uniquePaths', [2, 3], 3),
1143: ('longestCommonSubsequence', ['abcde', 'ace'], 3),
309: ('maxProfit', [[1, 2, 3, 0, 2]], 3),
518: ('change', [3, [1, 2]], 2),
494: ('findTargetSumWays', [[0, 1], 1], 2),
97: ('isInterleave', ['ab', 'cd', 'acbd'], True),
329: ('longestIncreasingPath', [[[9, 9, 4], [6, 6, 8], [2, 1, 1]]], 4),
115: ('numDistinct', ['babgbag', 'bag'], 5),
72: ('minDistance', ['cat', 'cut'], 1),
312: ('maxCoins', [[3, 1]], 6),
10: ('isMatch', ['aa', 'a*'], True),
53: ('maxSubArray', [[-2, 3, -1, 4, -5]], 6),
55: ('canJump', [[2, 0, 1]], True),
45: ('jump', [[2, 3, 1, 1, 4]], 2),
134: ('canCompleteCircuit', [[1, 2, 3], [2, 3, 1]], 2),
846: ('isNStraightHand', [[1, 2, 3, 2, 3, 4], 3], True),
1899: ('mergeTriplets', [[[2, 1, 3], [1, 4, 2]], [2, 4, 3]], True),
763: ('partitionLabels', ['abac'], [3, 1]),
678: ('checkValidString', ['(*)'], True),
57: ('insert', [[[1, 2], [5, 7]], [2, 6]], [[1, 7]]),
56: ('merge', [[[5, 7], [1, 3], [2, 6]]], [[1, 7]]),
435: ('eraseOverlapIntervals', [[[1, 3], [2, 4], [3, 5]]], 1),
252: ('canAttendMeetings', [[[1, 2], [2, 3]]], True),
253: ('minMeetingRooms', [[[0, 10], [5, 7], [7, 9]]], 2),
1851: ('minInterval', [[[1, 4], [2, 3]], [3, 5]], [2, -1]),
54: ('spiralOrder', [[[1, 2, 3], [4, 5, 6]]], [1, 2, 3, 6, 5, 4]),
202: ('isHappy', [19], True),
66: ('plusOne', [[9, 9]], [1, 0, 0]),
50: ('myPow', [2, -3], 0.125),
43: ('multiply', ['12', '13'], '156'),
191: ('hammingWeight', [12], 2),
338: ('countBits', [5], [0, 1, 1, 2, 1, 2]),
190: ('reverseBits', [1], 2147483648),
268: ('missingNumber', [[3, 0, 1]], 2),
371: ('getSum', [-2, 3], 1),
136: ('singleNumber', [[4, 1, 4]], 1),
7: ('reverse', [-120], -21),
127: ('ladderLength', ['hit', 'hot', ['hot']], 2),
332: ('findItinerary', [[['JFK', 'KUL'], ['JFK', 'NRT'], ['NRT', 'JFK']]], ['JFK', 'NRT', 'JFK', 'KUL']),
210: ('findOrder', [3, [[1, 0], [2, 1]]], [0, 1, 2]),
684: ('findRedundantConnection', [[[1, 2], [1, 3], [2, 3]]], [2, 3]),
}
tested = set()
for number, (method, args, expected) in cases.items():
    actual = run(number, method, args)
    assert actual == expected, (number, actual, expected)
    tested.add(number)

def check(number, assertion):
    assert assertion, number
    tested.add(number)

canonical = lambda groups: sorted(tuple(sorted(group)) for group in groups)
check(49, canonical(run(49, 'groupAnagrams', [['eat', 'tea', 'bat']])) == [('bat',), ('eat', 'tea')])
check(347, set(run(347, 'topKFrequent', [[1, 1, 1, 2, 2, 3], 2])) == {1, 2})
codec = environments[271]['Solution']()
check(271, codec.decode(codec.encode(['a#', ''])) == ['a#', ''])
sudoku = [['.'] * 9 for _ in range(9)]
sudoku[0][0] = sudoku[0][4] = '5'
check(36, run(36, 'isValidSudoku', [sudoku]) is False)
check(15, canonical(run(15, 'threeSum', [[-2, 0, 0, 2, 2]])) == [(-2, 0, 2)])
check(22, set(run(22, 'generateParenthesis', [2])) == {'(())', '()()'})
check(704, environments[704]['search']([-3, 0, 4, 9], 4) == 2)
check(973, {tuple(p) for p in run(973, 'kClosest', [[[1, 2], [3, 4], [0, 1]], 2])} == {(0, 1), (1, 2)})
check(39, canonical(run(39, 'combinationSum', [[2, 3], 6])) == [(2, 2, 2), (3, 3)])
check(78, canonical(run(78, 'subsets', [[1, 2]])) == [(), (1,), (1, 2), (2,)])
check(46, {tuple(p) for p in run(46, 'permute', [[1, 2]])} == {(1, 2), (2, 1)})
check(90, len(canonical(run(90, 'subsetsWithDup', [[1, 2, 2]]))) == 6)
check(40, canonical(run(40, 'combinationSum2', [[1, 1, 2], 2])) == [(1, 1), (2,)])
check(131, canonical(run(131, 'partition', ['aab'])) == [('a', 'a', 'b'), ('aa', 'b')])
check(17, set(run(17, 'letterCombinations', ['23'])) == {a+b for a in 'abc' for b in 'def'})
check(51, len(run(51, 'solveNQueens', [4])) == 2)
check(212, set(run(212, 'findWords', [[['a', 'b'], ['c', 'd']], ['ab', 'ac', 'aa']])) == {'ab', 'ac'})
check(417, {tuple(p) for p in run(417, 'pacificAtlantic', [[[1, 2], [4, 3]]])} == {(0, 1), (1, 0), (1, 1)})
alien = run(269, 'alienOrder', [['za', 'zb', 'ca', 'cb']])
check(269, set(alien) == set('zabc') and alien.index('a') < alien.index('b') and alien.index('z') < alien.index('c'))

# In-place outputs and judge-provided linked/tree nodes.
for number, method, data, expected in [
    (48, 'rotate', [[1, 2], [3, 4]], [[3, 1], [4, 2]]),
    (73, 'setZeroes', [[1, 2, 3], [4, 0, 6]], [[1, 0, 3], [0, 0, 0]]),
    (130, 'solve', [['X','O','X'], ['X','O','X'], ['X','X','X']], [['X','O','X'], ['X','O','X'], ['X','X','X']]),
    (286, 'walls_and_gates', [[0, 2147483647, 2147483647, -1]], [[0, 1, 2, -1]]),
]:
    getattr(environments[number]['Solution'](), method)(data)
    check(number, data == expected)
check(206, values(run(206, 'reverseList', [linked([1,2,3])])) == [3,2,1])
check(21, values(run(21, 'mergeTwoLists', [linked([1,4]), linked([2,3])])) == [1,2,3,4])
head = linked([1,2,3,4,5]); environments[143]['Solution']().reorderList(head)
check(143, values(head) == [1,5,2,4,3])
check(19, values(run(19, 'removeNthFromEnd', [linked([1,2,3]), 3])) == [2,3])
head = linked([1,2,3]); head.next.next.next = head.next
check(141, environments[141]['Solution']().hasCycle(head))
check(23, values(run(23, 'mergeKLists', [[linked([1,4]), linked([2,5]), linked([3])]])) == [1,2,3,4,5])
head = JudgeNode(1, next=JudgeNode(2)); head.next.random = head
copied = environments[138]['Solution']().copyRandomList(head)
check(138, copied is not head and copied.next.random is copied and copied.next is not head.next)
check(2, values(run(2, 'addTwoNumbers', [linked([9,9]), linked([1])])) == [0,0,1])
check(25, values(run(25, 'reverseKGroup', [linked([1,2,3,4,5]), 2])) == [2,1,4,3,5])
tree = TreeNode(1, TreeNode(2), TreeNode(3))
mirrored = run(226, 'invertTree', [tree]); check(226, mirrored.left.val == 3 and mirrored.right.val == 2)
chain = TreeNode(1, TreeNode(2, TreeNode(3)))
check(104, run(104, 'maxDepth', [chain]) == 3)
check(100, run(100, 'isSameTree', [TreeNode(1, TreeNode(2)), TreeNode(1, right=TreeNode(2))]) is False)
check(572, run(572, 'isSubtree', [TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2))), TreeNode(4, TreeNode(1), TreeNode(2))]))
bst = TreeNode(6, TreeNode(2), TreeNode(8)); ancestor = environments[235]['Solution']().lowestCommonAncestor(bst, bst.left, bst.right)
check(235, ancestor is bst)
tree = TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3))
check(102, run(102, 'levelOrder', [tree]) == [[1], [2,3], [4]])
check(98, run(98, 'isValidBST', [TreeNode(5, right=TreeNode(7, TreeNode(4)))]) is False)
check(230, run(230, 'kthSmallest', [TreeNode(3, TreeNode(1, right=TreeNode(2))), 2]) == 2)
tree = run(105, 'buildTree', [[2,1,3], [1,2,3]]); check(105, (tree.val, tree.left.val, tree.right.val) == (2,1,3))
check(124, run(124, 'maxPathSum', [TreeNode(-10, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))]) == 42)
codec = environments[297]['Codec'](); encoded = codec.serialize(TreeNode(1, right=TreeNode(2)))
check(297, encoded == '1,N,2,N,N' and codec.serialize(codec.deserialize(encoded)) == encoded)
check(543, run(543, 'diameterOfBinaryTree', [TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3))]) == 3)
check(110, run(110, 'isBalanced', [chain]) is False)
check(199, run(199, 'rightSideView', [TreeNode(1, TreeNode(2, right=TreeNode(5)))]) == [1,2,5])
check(1448, run(1448, 'goodNodes', [TreeNode(3, TreeNode(1), TreeNode(4))]) == 2)
node = JudgeNode(1); neighbor = JudgeNode(2); node.neighbors=[neighbor]; neighbor.neighbors=[node]
clone = environments[133]['Solution']().cloneGraph(node)
check(133, clone is not node and clone.neighbors[0].neighbors[0] is clone)

# Stateful design examples.
stack = environments[155]['MinStack'](); [stack.push(v) for v in [3,1,1]]; stack.pop()
check(155, stack.getMin() == 1 and stack.top() == 1)
cache = environments[146]['LRUCache'](2); cache.put(1,1); cache.put(2,2); cache.get(1); cache.put(3,3)
check(146, cache.get(2) == -1 and cache.get(1) == 1)
times = environments[981]['TimeMap'](); times.set('x','a',2); times.set('x','b',5)
check(981, times.get('x',4) == 'a' and times.get('x',1) == '')
trie = environments[208]['Trie'](); trie.insert('apple')
check(208, trie.startsWith('app') and not trie.search('app') and trie.search('apple'))
words = environments[211]['WordDictionary'](); words.addWord('bad'); words.addWord('dad')
check(211, words.search('.ad') and not words.search('..'))
median = environments[295]['MedianFinder'](); median.addNum(1); median.addNum(5)
assert median.findMedian() == 3; median.addNum(2); check(295, median.findMedian() == 2)
stream = environments[703]['KthLargest'](2,[4,1]); check(703, stream.add(3) == 3)
twitter = environments[355]['Twitter'](); twitter.follow(1,2); twitter.postTweet(1,10); twitter.postTweet(2,20)
check(355, twitter.getNewsFeed(1) == [20,10])
squares = environments[2013]['DetectSquares'](); [squares.add(p) for p in [[0,1],[1,0],[1,1]]]
check(2013, squares.count([0,0]) == 1)
assert tested == expected_ids, ('Missing smoke cases', expected_ids - tested)

# Independent small-input differential checks for boundary-sensitive algorithms.
rng = random.Random(875)
edge_cases = 0
for _ in range(100):
    nums = [rng.randrange(-5, 6) for _ in range(rng.randrange(1, 8))]
    expected = max(sum(nums[i:j]) for i in range(len(nums)) for j in range(i+1, len(nums)+1))
    assert run(53, 'maxSubArray', [nums]) == expected
    expected = max(__import__('math').prod(nums[i:j]) for i in range(len(nums)) for j in range(i+1,len(nums)+1))
    assert run(152, 'maxProduct', [nums]) == expected
    bars = [abs(v) for v in nums]
    expected = max(min(bars[i:j]) * (j-i) for i in range(len(bars)) for j in range(i+1,len(bars)+1))
    assert run(84, 'largestRectangleArea', [bars]) == expected
    expected = sum(min(max(bars[:i+1]), max(bars[i:]))-bars[i] for i in range(len(bars)))
    assert run(42, 'trap', [bars]) == expected
    piles = [abs(v)+1 for v in nums]; hours = rng.randrange(len(piles), len(piles)+20)
    expected = next(k for k in range(1,max(piles)+1) if sum((p+k-1)//k for p in piles) <= hours)
    assert run(875, 'minEatingSpeed', [piles,hours]) == expected
    positive = [abs(v)+1 for v in nums]
    expected = any(sum(subset)*2 == sum(positive) for count in range(len(positive)+1) for subset in itertools.combinations(positive,count))
    assert run(416, 'canPartition', [positive]) == expected
    edge_cases += 6
for a in range(-20, 21):
    for b in range(-20, 21):
        assert run(371, 'getSum', [a,b]) == a+b
        edge_cases += 1
for value in [-2147483648,2147483647,1534236469,-1563847412,0,-120,120,1463847412]:
    reversed_value = int(str(abs(value))[::-1]) * (-1 if value < 0 else 1)
    expected = reversed_value if -2147483648 <= reversed_value <= 2147483647 else 0
    assert run(7, 'reverse', [value]) == expected
    edge_cases += 1

print(json.dumps({'solution_notes':len(notes), 'smoke_tested_problems':len(tested), 'differential_and_boundary_cases':edge_cases, 'resolved_note_and_index_links':resolved_links, 'checkbox_states_preserved':True, 'noncoding_board_content_preserved':True}, indent=2))
