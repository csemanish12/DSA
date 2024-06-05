"""
Given the head of a singly linked list, return true if it is a
palindrome
 or false otherwise.



Example 1:


Input: head = [1,2,2,1]
Output: true
Example 2:


Input: head = [1,2]
Output: false


Constraints:

The number of nodes in the list is in the range [1, 105].
0 <= Node.val <= 9


Follow up: Could you do it in O(n) time and O(1) space?
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    1. find mid of linked list using slow and fast pointer
    2. reverse the second half of the linked list
    3. compare the first half and second half. If equal, palindrome else not
    4. repeat step 2 and 3 if asked to bring linked list back to its original condition
    """
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return True

        slow = fast = head
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next

        # reverse second half linked list
        slow.next = self.reverseLinkedList(slow.next)

        # move slow to right half
        slow = slow.next

        # compare
        while slow is not None:
            if head.val != slow.val:
                return False

            head = head.next
            slow = slow.next

        return True

    def reverseLinkedList(self, head):
        prev = next = None
        while head is not None:
            next = head.next
            head.next = prev
            prev = head
            head = next

        return prev
