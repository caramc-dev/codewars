from binary_trees_DFS import in_order, TreeNode

# Binary tree


#       Tree Structure
#           5
#       1       8
#    -1   3   7   9


A = TreeNode(5)
B = TreeNode(1)
C = TreeNode(8)
D = TreeNode(-1)
E = TreeNode(3)
F = TreeNode(7)
G = TreeNode(9)

A.left = B
A.right = C
B.left = D
B.right = E
C.left = F
C.right = G

# in_order(A)


"""
BST - Search - Time: O(log n), SPace: O(log n)

Takes the current node and the value looking for
if not node:
    triggers if you get to the bottom of the tree and you have not found your target, return False
if the value of the node is == to the target then return True

In the first conditional for 'not node' will not trigger as we always start with a valid node
The second conditional may trigger on the first pass if the root is equal to the target

If not, the current value of the node is compared against the target value and uses that to choose which path it goes in.
It continues down the tree, always discarding the side it cannot be

It targets the nodes recursively until there are either no nodes left or it hits it target.
By removing half the tree to search in each recursive iteration, the halves the amount to be searched

This is why BST search operations are O(log n)
Space is also O(log n) as each recursive call adds a frame to the stack but as we are discarding by half each time
space follows the same logic as time
"""


def search_bst(node, target):
    if not node:
        return False

    if node.val == target:
        return True

    if target < node.val:
        return search_bst(node.left, target)
    else:
        return search_bst(node.right, target)


print(search_bst(A, 4))
