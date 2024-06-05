"""
Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.



Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]
Example 2:


Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]


Constraints:

The number of nodes in the list is n.
1 <= k <= n <= 5000
0 <= Node.val <= 1000


Follow-up: Can you solve the problem in O(1) extra memory space?
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    1. Find the count of nodes in linked list
    2. Reverse nodes till length k
    3. Reduce the count by k
    4. Stop when count is smaller than k
    """
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or k == 1:
            return head

        dummy = ListNode(next=head)
        current, previous, next = dummy

        count = 0
        while current.next is not None:
            current = current.next
            count += 1

        while count >= k:
            current = previous.next
            next = current.next
            for i in range(1, k):
                current.next = next.next
                next.next = previous.next
                previous.next = next
                next = current.next

            previous = current
            count -= k

        return dummy.next
