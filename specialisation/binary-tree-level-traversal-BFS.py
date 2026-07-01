"""
N-ary Tree Level Order Traversal

Given an n-ary tree, return the level order traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal,
each group of children is separated by the null value (See examples).

Example:

           1
        /  |  \
      3    2    4
    /  \
  5     6

Input: root = [1,null,3,2,4,null,5,6]
Output: [[1],[3,2,4],[5,6]]

"""


from collections import deque


class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution:

    @staticmethod
    def levelOrder(self, root):

        if not root:
            return []  # base case - empty tree

        q = deque()
        q.append(root)  # starts the bfs from the root
        tree = []  # holds the levels

        while q:  # whilst there are values in the deque, process them
            level = []  # list to group the values for each level
            for _ in range(len(q)):  # loop to go through the nodes on this level
                node = q.popleft()  # takes the leftmost value from th front of the queue
                level.append(node.val)  # adds to the current level list
                for child in node.children:  # takes any children from that current node, and adds to the end fo the deque to be processed in the next batch
                    q.append(child)
            tree.append(
                level)  # After the current level has been processed, and the deque refilled, append the level list to the tree

        return tree

