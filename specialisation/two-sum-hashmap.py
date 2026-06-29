class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root) -> int:
        if not root:                                                           # Base case; if root is None, return 0
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))    # return 1 plus the max of the right or left node, called recursively