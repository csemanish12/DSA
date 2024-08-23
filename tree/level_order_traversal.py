"""
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).



Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []


Constraints:

The number of nodes in the tree is in the range [0, 2000].
-1000 <= Node.val <= 1000
"""
from collections import deque
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        q = deque()

        if root is None:
            return ans

        q.append(root)

        while q:
            size = len(q)
            sublist = []
            for _ in range(size):
                node = q.popleft()
                sublist.append(node.val)

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

            ans.append(sublist)

        return ans


root = TreeNode(3)
child1 = TreeNode(9)
child2 = TreeNode(20)
child3 = TreeNode(15)
child4 = TreeNode(17)

root.left = child1
root.right = child2

child2.left = child3
child2.right = child4

output = Solution().levelOrder(root)
print("output is:", output)