"""
==============================================================================
PRACTICE QUESTION: Graphs - Breadth-First Search (BFS)
==============================================================================

Given a graph represented as an adjacency list:

    graph = {
        "A": ["B", "C"],
        "B": ["D"],
        "C": ["E"],
        "D": [],
        "E": []
    }

      A
     / \\
    B   C
    |   |
    D   E

Write bfs(graph, start) that prints/returns the nodes in the order they
are VISITED via breadth-first search, starting from `start`.

------------------------------------------------------------------------------
EXAMPLES
------------------------------------------------------------------------------

bfs(graph, "A")     -> A B C D E

------------------------------------------------------------------------------
WHY A DEQUE + A VISITED SET (this is a recurring exam pattern)
------------------------------------------------------------------------------
BFS explores level by level - everything 1 step away, THEN everything 2
steps away, etc. That "process in the order added" behaviour is exactly a
QUEUE (FIFO), which is why deque.popleft() shows up here just like it did
in the customer support queue question.

The `visited` set exists to stop you re-processing a node you've already
queued/visited - without it, on a graph with a cycle, BFS would loop
forever. Mark a node visited the moment you ADD it to the queue (not when
you pop it) - otherwise the same node can be added to the queue multiple
times before it's ever processed.

    from collections import deque

    def bfs(graph, start):
        visited = set([start])
        queue = deque([start])
        order = []
        while queue:
            node = queue.popleft()
            order.append(node)
            for neighbour in graph[node]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append(neighbour)
        return order

Trace for graph above, start "A":
    queue=[A], visited={A}
    pop A -> order=[A] -> neighbours B,C unvisited -> queue=[B,C], visited={A,B,C}
    pop B -> order=[A,B] -> neighbour D unvisited -> queue=[C,D], visited={A,B,C,D}
    pop C -> order=[A,B,C] -> neighbour E unvisited -> queue=[D,E], visited={A,B,C,D,E}
    pop D -> order=[A,B,C,D] -> no neighbours
    pop E -> order=[A,B,C,D,E] -> no neighbours
    queue empty -> done

------------------------------------------------------------------------------
EXTENSION - shortest path between two nodes
------------------------------------------------------------------------------
This is the part flagged from your last MCQ as a gap, so spend real time
on it: BFS finds the SHORTEST path in an unweighted graph because it
explores in order of distance from the start - the first time you reach
the target node, you are guaranteed to have done so via the fewest
possible edges.

shortest_path(graph, start, target) should return the path as a list of
nodes, or None if unreachable.

Key idea: instead of (or alongside) a visited set, track HOW each node was
reached (its "parent" in the BFS tree). Once you reach the target, walk
the parent pointers backwards from target to start, then reverse the
result.

    def shortest_path(graph, start, target):
        if start == target:
            return [start]
        visited = {start}
        queue = deque([start])
        parent = {start: None}
        while queue:
            node = queue.popleft()
            for neighbour in graph[node]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    parent[neighbour] = node
                    if neighbour == target:
                        # reconstruct path by walking parents backwards
                        path = [target]
                        while path[-1] != start:
                            path.append(parent[path[-1]])
                        return path[::-1]
                    queue.append(neighbour)
        return None   # target unreachable

shortest_path(graph, "A", "E")  -> ["A", "C", "E"]
shortest_path(graph, "A", "D")  -> ["A", "B", "D"]
shortest_path(graph, "D", "A")  -> None   (no edges go back towards A)
"""

from collections import deque


def bfs(graph, start):
    pass


def shortest_path(graph, start, target):
    pass


# ==============================================================================
# TEST CASES - run this file to check your solution
# ==============================================================================

graph = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": ["E"],
    "D": [],
    "E": []
}

print(bfs(graph, "A"))
# Expected: ['A', 'B', 'C', 'D', 'E']

print(shortest_path(graph, "A", "E"))   # Expected: ['A', 'C', 'E']
print(shortest_path(graph, "A", "D"))   # Expected: ['A', 'B', 'D']
print(shortest_path(graph, "A", "A"))   # Expected: ['A']
print(shortest_path(graph, "D", "A"))   # Expected: None