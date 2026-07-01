# Binary tree

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)

#       Tree Structure
#           1
#       2       3
#     4   5   10


A = TreeNode(1)
B = TreeNode(2)
C = TreeNode(3)
D = TreeNode(4)
E = TreeNode(5)
F = TreeNode(10)

A.left = B
A.right = C
B.left = D
B.right = E
C.left = F


def pre_order(node):
    """
    Recursive **PRE ORDER TRAVERSAL** (DFS) Time: O(n), Space: O(n)
    Order of operations: current -> left -> right

    1. Visits root node A, this has a value of 1 and prints it.
    2. It then reaches the recursive function calls for left and right: pre_order(node.left (2)) and pre_order(node.right (3))
    3. As pre_order(left (2)) 2 is called first, so is run, leaving pre_order(node.right (3)) **waiting**
    4. Calling pre_order(left (2)) prints the value of the node 2 and the recursive function calls for left and right are reached again: pre_order(node.left (4)) and pre_order(node.right (5))
    5. pre_order(node.left (4)) is called and run, printing 4, recursively calling its right and left nodes which are both None
    6. The left node is run with None so returns, the right node is run with None so is returned
    7. Control returns back to pre_order(left (2)) which still has pre_order(node.right (5)) waiting
    8. pre_order(node.right (5)) is run, but has no nodes so these are run, but returned
    9. Control is then brought back up to pre_order(node.right (1)) which has pre_order(node.right (3)) **waiting**
    10. pre_order(node.right (3)) runs, printing 3, recursively calling pre_order(node.left (10)) and pre_order(node.right (None))
    11. pre_order(node.left (10)) is run, 10 is printed, but there is all None run calls from there so the recursion ends
    """
    if not node:
        return

    print(node)
    pre_order(node.left)
    pre_order(node.right)


# pre_order(A)


def in_order(node):
    """
    Recursive **IN ORDER TRAVERSAL** (DFS) Time: O(n), Space: O(n)
    Order of operations: left -> current -> right

    1. Visits root node A, reaches recursive function in_order(node.left (2)), lines up the print of node(A) and the in_order(node.right (3))
    2. Calls recursive in_order(node.left (2)), calls in_order(node.left (4)) and lines up the print of (node.left (2)) and the call to (node.right (5))
    3. calls in_order(node.left (4)), this hits Nones on left and right so prints 4
    4. Control returns to in_order(node.left (2)) which prints 2
    5. (node.right (5)) is then called and 5 is printed
    6. Control returns to node A and the print statement runs
    7. in_order(node.right (3)) runs, calling in_order(node.left (10)), lining up the print of in_order(node.right (3))
    8. in_order(node.left (10)) calls the left node which is None, back to print the in_order(node.left (10)) result
    9. Control returns to in_order(node.right (3)) and this is printed. The rest of the nodes are None and the recursion ends
    """
    if not node:
        return

    in_order(node.left)
    print(node)
    in_order(node.right)


in_order(A)


def post_order(node):
    """
    Recursive **POST ORDER TRAVERSAL** (DFS) Time: O(n), Space: O(n)
    Order of operations: left -> right -> current

    1. Visits root node A, reaches recursive function post_order(node.left (2)), lining up the post_order(node.right (3)) and print for node A
    2. Calls recursive post_order(node.left (2)), hits post_order(node.left (4)), lining up post_order(node.right (5)) and the print for post_order(node.left (2))
    3. calls post_order(node.left (4)), this hits Nones on left and right so prints 4
    4. Control returns to post_order(node.left (2)) which then calls the lined up post_order(node.right (5))
    5. post_order(node.right (5)) has None for right and left so after they return, 5 is printed
    6. Control is returned to post_order(node.left (2) and 2 is printed,
    7. Control returns to node A and post_order(node.right (3)) is called
    8. post_order(node.right (3)) runs, calling post_order(node.left (10)), lining up the print of post_order(node.right (None)) and the print for post_order(node.left (10))
    9. post_order(node.left (10)) is run has None for right and left so after they return, 10 is printed
    10. Control returns to post_order(node.right (3)) and as Right is None,
    11. Control finally returns to node A and 1 is printed, ending the recursion.
    """
    if not node:
        return

    post_order(node.left)
    post_order(node.right)
    print(node)


# if __name__ == "__main__":
    # post_order(A)
    # in_order(A)

