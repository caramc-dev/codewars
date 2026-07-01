"""

==============================================================================
PRACTICE QUESTION: Lowest Common Ancestor of a BST
==============================================================================

Given the root of a Binary Search Tree (BST), and two values p and q that
both exist somewhere in the tree, return the LOWEST COMMON ANCESTOR (LCA)
node of p and q.

The lowest common ancestor is defined as the lowest (deepest) node in the
tree that has both p and q as descendants (a node can be a descendant of
itself).

A TreeNode class is provided for you below — you do not need to change it.

HINT: This is a BST, not just any binary tree — that ordering property
(left < node < right) means you don't need to search the whole tree to
find each value. Think about what comparing p and q against the CURRENT
node's value tells you about which direction to go.

------------------------------------------------------------------------------
EXAMPLES
------------------------------------------------------------------------------

Tree:
              6
           /     \\
          2        8
        /   \\    /   \\
       0     4   7     9
            / \\
           3   5

lowest_common_ancestor(root, 2, 8)  -> 6   (2 and 8 split at the root)
lowest_common_ancestor(root, 2, 4)  -> 2   (4 is a descendant of 2)
lowest_common_ancestor(root, 3, 5)  -> 4   (3 and 5 split at node 4)
lowest_common_ancestor(root, 0, 5)  -> 2   (both are in 2's subtree)

"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def lowest_common_ancestor(root, p, q):
    current = root
    while current:
        if p < current.val and q < current.val:  # if both p & q are smaller that the node value, the LCA must be further left so assign the current to current: left
            current = current.left
        elif p > current.val and q > current.val:  # if both are bigger, then go right, same logic
            current = current.right
        else:
            return current  # the moment they are not the same, one is smaller and one is bigger then this is the LCA
    return None


# ==============================================================================
# TEST CASES — run this file to check your solution
# ==============================================================================

#               6
#            /     \
#           2        8
#         /   \    /   \
#        0     4   7     9
#             / \
#            3   5

root = TreeNode(6)
root.left = TreeNode(2)
root.right = TreeNode(8)
root.left.left = TreeNode(0)
root.left.right = TreeNode(4)
root.right.left = TreeNode(7)
root.right.right = TreeNode(9)
root.left.right.left = TreeNode(3)
root.left.right.right = TreeNode(5)



print(lowest_common_ancestor(root, 2, 8).val)
# Expected: 6

print(lowest_common_ancestor(root, 2, 4).val)
# Expected: 2

print(lowest_common_ancestor(root, 3, 5).val)
# Expected: 4

print(lowest_common_ancestor(root, 0, 5).val)
# Expected: 2

print(lowest_common_ancestor(root, 7, 9).val)
# Expected: 8

print(lowest_common_ancestor(root, 3, 9).val)
# Expected: 6

# A node counts as its own ancestor
print(lowest_common_ancestor(root, 4, 5).val)
# Expected: 4

# Single node tree
single = TreeNode(1)
print(lowest_common_ancestor(single, 1, 1).val)
# Expected: 1