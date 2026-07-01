"""
Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums):
        #  Base case - halt once the list is empty
        if not nums:
            return None

        # Split the array and find mid-point index
        mid = len(nums) // 2
        node = TreeNode(nums[mid])  # Create the new tree node (currently with None placeholder values) to the mid-point value using the midpoint index to slice

        # Split the array into right and left halves (making up each subtree) and use recursion to insert into the tree
        node.left = self.sortedArrayToBST(nums[:mid])  # Slice the array so it is everything before the mid point
        node.right = self.sortedArrayToBST(nums[mid +1:]) # Slice the array so it is everything after the midpoint + 1 to disregard the midpoint as that is the root

        return node
