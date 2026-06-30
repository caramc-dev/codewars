# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root):
        # If the root is None return
        if not root:
            return None

        # Swap the children - hold the left root node in a temp variable, swap left with right then assign right with left
        # Do this before the recursion so it takes effect
        temp = root.left
        root.left = root.right
        root.right = temp

        # recursively invert the tree
        # When there are no more subtrees to invert (right and left hit None's), return the root which has everything swapped
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root