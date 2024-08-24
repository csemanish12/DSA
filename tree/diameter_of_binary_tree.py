"""
Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.



Example 1:


Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
Example 2:

Input: root = [1,2]
Output: 1


Constraints:

The number of nodes in the tree is in the range [1, 104].
-100 <= Node.val <= 100
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    using height calculation approach
    TC = O(N)
    SP = O(N)
    """
    MAX_DIAMENTER = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.findMax(root)
        return self.MAX_DIAMENTER

    def findMax(self, node):
        if node is None:
            return 0

        left_height = self.findMax(node.left)
        right_height = self.findMax(node.right)

        self.MAX_DIAMENTER = max(self.MAX_DIAMENTER, left_height + right_height)

        return 1 + max(left_height, right_height)
