"""
Given the head of a singly linked list, reverse the list, and return the reversed list.



Example 1:


Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
Example 2:


Input: head = [1,2]
Output: [2,1]
Example 3:

Input: head = []
Output: []


Constraints:

The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000


Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?
"""
from typing import Optional

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    First iteration:
    - point head->next to new_head
    - point new_head to head
    - point head to head.next
    At the end of first iteration, current_node is not pointed by any node. new_head is pointing to current_node.
    Only in the second iteration, when head->next = new_head, we point the current node to prev element
    Next Iteration:
    - point current_node->next to new_head. This will complete the incomplete link of first iteration.
    - same as above
    """
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        new_head = None
        while head is not None:
            next_node = head.next
            head.next = new_head
            new_head = head
            head = next_node

        return new_head

