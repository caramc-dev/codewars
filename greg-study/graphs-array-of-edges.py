from collections import defaultdict

# Array of Edges (Directed) [Start, End] - 0 points to 1, 1 to 2 etc
n = 8
A = [[0, 1], [1, 2], [0, 3], [3, 4], [3, 6], [3, 7], [4, 2], [4, 5], [5, 2]]

# Convert Array of Edges -> Adjacency Matrix
M = []
for i in range(n):
    M.append([0] * n)

for u, v in A:
    M[u][v] = 1

# for i in range(n):
#     for j in range(n):
#         print(M[i][j], end=' ')
#     print()

# Convert Array of Edges -> Adjacency List
D = defaultdict(list)

for u, v in A:
    D[u].append(v)

# print(D)
# print(D[3])


def dfs_recursive(node):
    """
    DFS with Recursion - O(V + E) where V is the number of
    nodes and E is the number of edges
    """
    print(node)
    for neighbour_node in D[node]:
        if neighbour_node not in seen:
            seen.add(neighbour_node)
            dfs_recursive(neighbour_node)


# source = 0
# seen = set()
# seen.add(source)
# dfs_recursive(source)

source = 0
seen = set()
seen.add(source)
stack = [source]

while stack:
    node = stack.pop()
    print(node)
    for neighbour_node in D[node]:
        if neighbour_node not in seen:
            seen.add(neighbour_node)
            stack.append(neighbour_node)