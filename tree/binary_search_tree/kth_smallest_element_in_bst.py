"""
Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.



Example 1:


Input: root = [3,1,4,null,2], k = 1
Output: 1
Example 2:


Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3


Constraints:

The number of nodes in the tree is n.
1 <= k <= n <= 104
0 <= Node.val <= 104


Follow up: If the BST is modified often (i.e., we can do insert and delete operations) and you need to find the kth smallest frequently, how would you optimize?
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = [0]
        kth = [float('inf')]
        self.get_kth_element(root, k, count, kth)

        return kth[0]

    def get_kth_element(self, root, k, count, kth):
        if root is None or count[0] >= k:
            return

        self.get_kth_element(root.left, k, count, kth)
        count[0] += 1

        if count[0] == k:
            kth[0] = root.val
            return

        self.get_kth_element(root.right, k, count, kth)


root = TreeNode(3)
root.left = TreeNode(1)
root.left.right = TreeNode(2)
root.right = TreeNode(4)

print("output:", Solution().kthSmallest(root, 3))
