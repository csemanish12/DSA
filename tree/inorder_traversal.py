"""
Given the root of a binary tree, return the inorder traversal of its nodes' values.



Example 1:


Input: root = [1,null,2,3]
Output: [1,3,2]
Example 2:

Input: root = []
Output: []
Example 3:

Input: root = [1]
Output: [1]


Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100


Follow up: Recursive solution is trivial, could you do it iteratively?
"""
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        self.inorder(root, ans)
        return ans

    def inorder(self, root, ans):
        if root is None:
            return

        self.inorder(root.left, ans)
        ans.append(root.val)
        self.inorder(root.right, ans)


root = TreeNode(1)
child1 = TreeNode(2)
child2 = TreeNode(3)
root.right = child1
child1.left = child2

output = Solution().inorderTraversal(root)
print("output is: ", output)
