"""
Given the roots of two binary trees p and q, write a function to check if they
are the same or not.

Two binary trees are considered the same if they are structurally identical,
and the nodes have the same value.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p, q):

        if not p and not q:
            return True

        if not p or not q or p.val != q.val:  # if one of the nodes is empty and the other has a value,
            return False                      # or they do not equal each other. This immediately returns False and short-circuits the 'and' in the recursive statement

        # if p.val != q.val:    # originally had as 2 lines
        #     return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right) # recursively run through.
        # if the recursion hits the base case (nodes are empty) and all have been true this is bubbled back up and outputs true



