# We are finding a path so DFS is better here as naturally visits root to leaf
# Using pre-order traversal to hit each leaf node left to right
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root, targetSum) -> bool:

        if root is None:  # Base case, if you reach the end of the recursion and havn't found it, return False
            return False

        if root.left is None and root.right is None and (
                targetSum - root.val) == 0:  # Condition to check at the leaf node, if the last subtraction is 0, then the condition is met
            return True
        else:  # Recursive block, keeps going down the node,
            targetSum -= root.val  # subtracting the value of the current roon from the targetSum to keep track of it
            return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right,
                                                                            targetSum)  # Recursive calls, keeping calling and subtracting until the None/ None has been reached

            # The Or means it will follow the left then the right and return True if on any branch the condition is met

# O(n) time and space complexity
