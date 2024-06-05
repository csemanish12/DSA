"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.



Example 1:


Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]


Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    Node contains only single digit value. if the sum is >= 10, divide it to val and carry.
    sum // 10 -> val
    sum % 10 -> carry
    """

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        new_head = prev_node = None
        carry_over = 0
        while l1 is not None and l2 is not None:
            sum = l1.val + l2.val + carry_over
            val, carry_over = sum % 10, sum // 10
            new_node = ListNode(val)

            if new_head is None:
                new_head = prev_node = new_node
            else:
                prev_node.next = new_node
                prev_node = new_node

            l1 = l1.next
            l2 = l2.next

        while l1 is not None:
            sum = l1.val + carry_over
            val, carry_over = sum % 10, sum // 10
            new_node = ListNode(val)
            prev_node.next = new_node
            prev_node = new_node
            l1 = l1.next

        while l2 is not None:
            sum = l2.val + carry_over
            val, carry_over = sum % 10, sum // 10
            new_node = ListNode(val)
            prev_node.next = new_node
            prev_node = new_node
            l2 = l2.next

        if carry_over > 0:
            new_node = ListNode(carry_over)
            prev_node.next = new_node

        return new_head