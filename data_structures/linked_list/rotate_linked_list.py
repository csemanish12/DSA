"""
Given the head of a linked list, rotate the list to the right by k places.


Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]
Example 2:


Input: head = [0,1,2], k = 4
Output: [2,0,1]


Constraints:

The number of nodes in the list is in the range [0, 500].
-100 <= Node.val <= 100
0 <= k <= 2 * 109
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    Observation:
    1. find length of linked list
    2. when k is multiple of n, rotation will lead to original linked list
    3. when k is greater than n, actual rotation will be k % n
    Approach:
    1. find length of linked list and point last node to head
    2. find the node which needs to point to null after rotation(n-k) and point the node to null
    3. point head to (n-k+1)th node
    """

    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 0 or head is None:
            return head

        n = 1
        temp = head
        while temp.next is not None:
            n += 1
            print("n is",n)
            temp = temp.next

        # point last node to head
        temp.next = head

        # find actual k
        k = k % n

        # find the node which needs to point to n
        k = n - k

        temp = head
        count = 1
        while count < k:
            temp = temp.next
            count += 1

        head = temp.next
        temp.next = None

        return head
