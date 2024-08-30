"""
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).



Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []


Constraints:

The number of nodes in the tree is in the range [0, 2000].
-100 <= Node.val <= 100
"""
from typing import Optional, List
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []

        if root is None:
            return ans

        q = deque()
        q.append(root)
        is_left_to_right = True

        while q:
            size = len(q)
            level_wise = []
            for i in range(size):
                node = q.popleft()
                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

                level_wise.append(node.val)

            if is_left_to_right:
                ans.append(level_wise)
            else:
                ans.append(level_wise[::-1])

            is_left_to_right = not is_left_to_right

        return ans








root = TreeNode(3)
root.left = TreeNode(9)
root.right  = TreeNode(20)
root.right.left  = TreeNode(15)
root.right.right  = TreeNode(7)


print("output:", Solution().zigzagLevelOrder(root))