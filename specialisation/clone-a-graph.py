class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbours = neighbors if neighbors else []

# LeetCode's standard example: a 4-node square

# 1--2
# |  |
# 4--3


n1, n2, n3, n4 = Node(1), Node(2), Node(3), Node(4)
n1.neighbours = [n2, n4]
n2.neighbours = [n1, n3]
n3.neighbours = [n2, n4]
n4.neighbours = [n1, n3]

oldToNew = {}
hit_count = [0]


def dfs(node):
    if node in oldToNew:
        hit_count[0] += 1
        print(f'  EARLY RETURN #{hit_count[0]}: node {node.val} already cloned')
        return oldToNew[node]

    print("Progress: ", {k.val: v.val for k, v in oldToNew.items()}, "\n")
    print(f'CLONE: making new clone of node {node.val}')
    clone = Node(node.val)
    oldToNew[node] = clone
    for nei in node.neighbours:
        clone.neighbours.append(dfs(nei))
    return clone

dfs(n1)
print()
print(f'Total nodes actually cloned: {len(oldToNew)}')
print(f'Total times early-return fired: {hit_count[0]}')
