"""

==============================================================================
PRACTICE QUESTION: Number of Islands
==============================================================================

You are given a 2D grid of '1's (land) and '0's (water).
An ISLAND is a group of adjacent land cells connected horizontally or
vertically (NOT diagonally). Assume the edges of the grid are surrounded
by water.

Write a function that returns the NUMBER of islands in the grid.

This is a graph problem in disguise — think of each land cell as a node,
and each adjacent land cell as an edge connecting them. You need to find
the number of CONNECTED COMPONENTS made of '1's.

You'll need a way to track which cells you've already visited (think about
what happens if you don't — same issue as graph DFS/BFS with cycles).
You can use either BFS or DFS to explore each island — try whichever you
find easier to trace by hand.

------------------------------------------------------------------------------
EXAMPLES
------------------------------------------------------------------------------

grid1 = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]
count_islands(grid1) -> 3

grid2 = [
    ["1", "1", "1"],
    ["0", "1", "0"],
    ["1", "0", "1"]
]
count_islands(grid2) -> 3
# (the big connected blob in the middle/top counts as ONE island,
#  the bottom-left '1' and bottom-right '1' are each their own island —
#  remember, diagonal doesn't count as connected)

"""
from collections import deque


from collections import deque

def count_islands(grid):
    if not grid:        # If the grid is empty, return 0
        return 0

    rows, cols = len(grid), len(grid[0])    # get the grid dimensions
    visited = set()      # tracks every land cell we've already counted, across ALL islands
    island_count = 0     # how many separate islands we've found so far

    def bfs(start_row, start_col):
        # explores one whole island starting from (start_row, start_col),
        # marking every connected land cell as visited so the outer loop
        # never counts this island again
        queue = deque([(start_row, start_col)])   # cells still waiting to be explored
        visited.add((start_row, start_col))       # mark the starting cell visited immediately

        while queue:                              # keep going until no cells left to explore
            r, c = queue.popleft()                 # take the next cell to check (O(1) — deque, not list.pop(0))

            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                # the 4 directions to check: up, down, left, right — no diagonals
                nr, nc = r + dr, c + dc            # coordinates of this neighbour

                if (0 <= nr < rows and 0 <= nc < cols     # neighbour is inside the grid
                        and grid[nr][nc] == "1"           # neighbour is land
                        and (nr, nc) not in visited):      # neighbour hasn't been counted yet
                    visited.add((nr, nc))          # mark it visited so we never re-check it
                    queue.append((nr, nc))          # add it to the queue so its own neighbours get checked too

    for r in range(rows):              # scan every row
        for c in range(cols):          # scan every column in that row
            if grid[r][c] == "1" and (r, c) not in visited:
                # found an unvisited land cell — this is the FIRST cell of a
                # brand new island we haven't counted yet
                island_count += 1       # count this new island
                bfs(r, c)                # explore and mark the whole island as visited,
                                          # so nothing inside it gets counted again

    return island_count


# ==============================================================================
# TEST CASES — run this file to check your solution
# ==============================================================================

grid1 = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]
print(count_islands(grid1))
# Expected: 3

grid2 = [
    ["1", "1", "1"],
    ["0", "1", "0"],
    ["1", "0", "1"]
]
print(count_islands(grid2))
# Expected: 3

# All water
grid3 = [
    ["0", "0"],
    ["0", "0"]
]
print(count_islands(grid3))
# Expected: 0

# All land (one big island)
grid4 = [
    ["1", "1"],
    ["1", "1"]
]
print(count_islands(grid4))
# Expected: 1

# Single cell
grid5 = [["1"]]
print(count_islands(grid5))
# Expected: 1

# Diagonal cells should NOT count as connected
grid6 = [
    ["1", "0"],
    ["0", "1"]
]
print(count_islands(grid6))
# Expected: 2

# Empty grid
print(count_islands([]))
# Expected: 0