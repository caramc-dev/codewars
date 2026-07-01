# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root):
        if not root:                                                           # Base case; if root is None, return 0
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))    # return 1 plus the max of the right or left node, called recursively


# Example tree:
#       3
#      / \
#     9  20
#        / \
#       15   7


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)


solution = Solution()
print(solution.maxDepth(root))