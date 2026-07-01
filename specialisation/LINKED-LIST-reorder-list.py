class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reorderList(self, head):
        """
        Don't return anything, modify the list in place

        Split the list in 2, reverse the link then merge them
        """
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast - fast.next.next

        second = slow.next
        prev = slow.next = None

        while second:           # reversing the second portion of the list
            tmp = second.next   # temp var to hold the next node
            second.next = prev  # switch prev with second next
            prev = second
            second = tmp        # move second into the temp variable

        # merge the 2 halves of the list
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next  # storing the next nodes in temp variables as we will be breaking those links
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
