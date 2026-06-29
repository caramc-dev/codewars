"""
Tree Constructor

Have the function TreeConstructor(strArr) take the array of strings stored in strArr, which will contain pairs of
integers in the following format: (i1,i2), where i1 represents a child node in a tree and the second integer i2
signifies that it is the parent of i1. For example: if strArr is ["(1,2)", "(2,4)", "(7,2)"], then this forms the
following tree:

            4
          /
        2
      /   \
    1      7



which you can see forms a proper binary tree.
Your program should, in this case, return the string true because a valid binary tree can be formed.
If a proper binary tree cannot be formed with the integer pairs, then return the string false.

All the integers within the tree will be ( need to be) unique, which means there can only be one node in the tree
with the given integer value.
"""


def TreeConstructor(strArr):
    tree = {}
    children = set()

    for pair in strArr:
        pair = pair.strip("()")  # Strip the string brackets
        child, parent = pair.split(",")  # split on the comma to seperate parent and child

        if parent not in tree:  # Add parents to the dictionary if there isn't any and track 1 child
            tree[parent] = 1
        elif tree[parent] == 2:  # If the parent node has reached 2 children,
            return "false"
        else:
            tree[parent] += 1  # else add a child

        if child not in children:  # If the child has not been added already add
            children.add(child)
        else:  # If there is a child in the set, return false as there can be only unique child nodes
            return "false"

    return "true"


# keep this function call here
print(TreeConstructor(input()))