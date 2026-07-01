"""
==============================================================================
TREES & GRAPHS — IMPLEMENTATION REFERENCE
==============================================================================
The night-before cheat sheet. Every pattern that can come up, annotated
in plain English. Don't memorise the code — understand the shape, and the
code writes itself.

CONTENTS
--------
SECTION 1: The building blocks (TreeNode, graph setup)
SECTION 2: Tree traversals (pre / in / post / level-order)
SECTION 3: Common tree problems (max depth, find max, path sum)
SECTION 4: Graph BFS (visit all, shortest path)
SECTION 5: Graph DFS (visit all, path exists, find route)
SECTION 6: THE DECISION CHEAT SHEET (what to reach for and when)
"""

from collections import deque


# ==============================================================================
# SECTION 1: BUILDING BLOCKS
# ==============================================================================

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left    # points to left child TreeNode, or None
        self.right = right  # points to right child TreeNode, or None

# Building a tree manually (you'll often be given this in the question):
#
#         8
#        / \
#       4   12
#      / \
#     2   6
#
root = TreeNode(8)
root.left = TreeNode(4)
root.right = TreeNode(12)
root.left.left = TreeNode(2)
root.left.right = TreeNode(6)

# Graphs are just a dictionary — each key is a node, value is its neighbours:
graph = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": ["E"],
    "D": [],
    "E": []
}


# ==============================================================================
# SECTION 2: TREE TRAVERSALS
# The only thing that changes between these three is WHERE you process the
# current node relative to the two recursive calls.
# ==============================================================================

# PRE-ORDER: process BEFORE going left or right
# Use when: you need to copy/clone a tree, or output parent before children
# Output on tree above: 8, 4, 2, 6, 12
def pre_order(node):
    if node is None:        # base case: nothing here, stop
        return
    print(node.val)         # process NOW, before going anywhere
    pre_order(node.left)    # then go left
    pre_order(node.right)   # then go right


# IN-ORDER: process BETWEEN left and right
# Use when: you want values in ascending order (BST only guarantees this)
# Output on tree above: 2, 4, 6, 8, 12
def in_order(node):
    if node is None:        # base case: nothing here, stop
        return
    in_order(node.left)     # go all the way left first
    print(node.val)         # process when you surface back up
    in_order(node.right)    # then go right


# POST-ORDER: process AFTER both children
# Use when: you need to process children before their parent (e.g. deleting
# a tree, or calculating sizes that depend on subtree results)
# Output on tree above: 2, 6, 4, 12, 8
def post_order(node):
    if node is None:        # base case: nothing here, stop
        return
    post_order(node.left)   # go left all the way first
    post_order(node.right)  # go right all the way
    print(node.val)         # THEN process — after both children are done


# LEVEL-ORDER (BFS on a tree): left to right, level by level
# Use when: you want nodes in their "breadth" order, not depth
# Output on tree above: 8, 4, 12, 2, 6
# This is the ONE tree traversal that uses a queue, not recursion
def level_order(root):
    if root is None:
        return []

    result = []
    queue = deque([root])           # start with just the root in the queue

    while queue:
        node = queue.popleft()      # take from the FRONT (FIFO)
        result.append(node.val)     # process it

        if node.left:               # add left child to queue if it exists
            queue.append(node.left)
        if node.right:              # add right child to queue if it exists
            queue.append(node.right)
        # children will be processed AFTER everything already in the queue
        # — that's what gives us level-by-level order

    return result


# ==============================================================================
# SECTION 3: COMMON TREE PROBLEMS
# These all follow the same recursive shape: base case = None, then ask
# left subtree, ask right subtree, combine the answers.
# ==============================================================================

# MAX DEPTH / HEIGHT
# "How deep is this tree?" = 1 + whichever subtree is deeper
def max_depth(node):
    if node is None:            # base case: empty slot has no depth
        return 0
    left_depth = max_depth(node.left)
    right_depth = max_depth(node.right)
    return 1 + max(left_depth, right_depth)  # this node adds 1 to the deeper side


# FIND MAXIMUM VALUE
# "What's the biggest value anywhere in this tree?"
# float('-inf') as the base case means an empty slot can never "win" a comparison
def find_max(node):
    if node is None:
        return float('-inf')    # empty slot contributes nothing
    left_max = find_max(node.left)
    right_max = find_max(node.right)
    return max(node.val, left_max, right_max)  # biggest of: me, left side, right side


# PATH SUM (does any root-to-leaf path add up to the target?)
# Subtract the current node's value from the target as you go down.
# When you hit a leaf, check if the remaining target is exactly 0.
def has_path_sum(node, target):
    if node is None:
        return False
    target -= node.val                  # "spend" this node's value
    if node.left is None and node.right is None:  # we're at a leaf
        return target == 0              # did we hit the target exactly?
    return has_path_sum(node.left, target) or has_path_sum(node.right, target)


# BST SEARCH
# Only works on a BST (left < root < right guaranteed).
# You CAN skip a whole side — that's what makes BST search O(log n).
def bst_search(node, target):
    if node is None:            # fell off the tree — not here
        return False
    if node.val == target:      # found it
        return True
    if target < node.val:       # target is smaller — must be left
        return bst_search(node.left, target)
    else:                       # target is bigger — must be right
        return bst_search(node.right, target)


# ==============================================================================
# SECTION 4: GRAPH BFS
# Use when: shortest path, level-by-level, "closest first"
# Shape: queue + visited SET (not list — set gives O(1) membership check)
# ==============================================================================

# BFS — visit all reachable nodes from start
def bfs(graph, start):
    visited = set([start])      # mark start as seen immediately
    queue = deque([start])      # start is the first thing to process
    order = []

    while queue:
        node = queue.popleft()  # take from FRONT — this is what makes it BFS
        order.append(node)

        for neighbour in graph[node]:
            if neighbour not in visited:        # haven't seen this one yet
                visited.add(neighbour)          # mark it NOW (before popping)
                queue.append(neighbour)         # add to BACK of queue

    return order
# Output on graph above from "A": ['A', 'B', 'C', 'D', 'E']


# SHORTEST PATH — BFS with parent tracking
# First time BFS reaches a node = guaranteed shortest path (fewest hops)
def shortest_path(graph, start, target):
    if start == target:
        return [start]

    visited = {start}
    queue = deque([start])
    parent = {start: None}      # tracks HOW we got to each node

    while queue:
        node = queue.popleft()
        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.add(neighbour)
                parent[neighbour] = node        # "we got to neighbour via node"
                if neighbour == target:
                    # reconstruct path by walking parent pointers backwards
                    path = [target]
                    while path[-1] != start:
                        path.append(parent[path[-1]])
                    return path[::-1]           # reverse to get start -> target
                queue.append(neighbour)

    return None     # target was never reached


# ==============================================================================
# SECTION 5: GRAPH DFS
# Use when: path exists yes/no, exploring all paths, cycle detection
# Shape: recursion + visited SET (call stack acts as the stack for you)
# ==============================================================================

# DFS — visit all reachable nodes from start
def dfs(graph, start, visited=None, order=None):
    if visited is None:         # NEVER use visited=set() as a default —
        visited = set()         # mutable defaults persist between calls (the
    if order is None:           # same bug family as mutable __init__ defaults)
        order = []

    visited.add(start)
    order.append(start)

    for neighbour in graph[start]:
        if neighbour not in visited:
            dfs(graph, neighbour, visited, order)   # go DEEP before going wide

    return order
# Output on graph above from "A": ['A', 'B', 'D', 'C', 'E']


# PATH EXISTS — does any path connect start to target?
def has_path(graph, start, target, visited=None):
    if start == target:         # base case: already there
        return True
    if visited is None:
        visited = set()

    visited.add(start)

    for neighbour in graph[start]:
        if neighbour not in visited:
            if has_path(graph, neighbour, target, visited):
                return True     # found it somewhere down this branch

    return False                # exhausted all paths, never found target


# FIND ACTUAL ROUTE (DFS with backtracking)
# Builds the path as it goes, removes dead ends by popping on backtrack
def find_route(graph, start, target):
    visited = set()
    path = []

    def dfs_route(current):
        visited.add(current)
        path.append(current)

        if current == target:   # base case: we've arrived
            return True

        for neighbour in graph[current]:
            if neighbour not in visited:
                if dfs_route(neighbour):
                    return True # found it — propagate True back up the stack

        path.pop()              # this branch was a dead end — backtrack
        return False

    if dfs_route(start):
        return path
    return None


# ==============================================================================
# SECTION 6: THE DECISION CHEAT SHEET
# Read the question, pick from this list — then just fill in the template.
# ==============================================================================
#
# "print level by level / level order"          -> LEVEL-ORDER BFS (queue)
# "ascending order in a BST"                    -> IN-ORDER DFS (recursion)
# "shortest path between two nodes"             -> BFS (queue + parent dict)
# "does a path exist"                           -> DFS (recursion, don't care which path)
# "find max/min value in any tree"              -> POST-ORDER style recursion
#                                                  (ask both sides, combine)
# "height / depth of tree"                      -> RECURSION, base case = None
# "visit all nodes in a graph"                  -> BFS or DFS, both work
# "copy / clone a tree"                         -> PRE-ORDER (parent before children)
#
# BASE CASE CHECKLIST (fill in before writing anything else):
#   Tree recursion?   -> "if node is None: return ___"
#   Graph traversal?  -> "visited" set, add before appending to queue/recursing
#   Shortest path?    -> parent dict, reconstruct by walking backwards then [::-1]
#
# STRUCTURE CHECKLIST:
#   BFS  -> deque + visited SET + popleft()
#   DFS  -> recursion + visited SET + None defaults (never mutable defaults)
#   Tree -> TreeNode class, node.left / node.right, recurse both sides
#   BST  -> same as tree BUT you can skip a side (left < root < right)

