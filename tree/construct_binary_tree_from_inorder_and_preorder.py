"""
Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.



Example 1:


Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]
Example 2:

Input: preorder = [-1], inorder = [-1]
Output: [-1]


Constraints:

1 <= preorder.length <= 3000
inorder.length == preorder.length
-3000 <= preorder[i], inorder[i] <= 3000
preorder and inorder consist of unique values.
Each value of inorder also appears in preorder.
preorder is guaranteed to be the preorder traversal of the tree.
inorder is guaranteed to be the inorder traversal of the tree.
"""
from typing import Optional, List


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        inorder_map = {}
        for i in range(len(inorder)):
            inorder_map[inorder[i]] = i

        pre_start = in_start = 0
        pre_end = len(preorder) - 1
        in_end = len(inorder) - 1
        root = self.buildBinaryTree(preorder, pre_start, pre_end, inorder, in_start, in_end, inorder_map)

        return root

    def buildBinaryTree(self, preorder, pre_start, pre_end, inorder, in_start, in_end, inorder_map):
        if pre_start > pre_end or in_start > in_end:
            return None

        root = TreeNode(preorder[pre_start])
        in_root = inorder_map[root.val]
        num_of_left = in_root - in_start

        root.left = self.buildBinaryTree(preorder, pre_start + 1, pre_start + num_of_left, inorder, in_start,
                                         in_root - 1, inorder_map)
        root.right = self.buildBinaryTree(preorder, pre_start + num_of_left + 1, pre_end, inorder, in_root + 1, in_end,
                                          inorder_map)

        return root

    def get_preorder(self, root, ans):
        if root is None:
            return
        ans.append(root.val)
        self.get_preorder(root.left, ans)
        self.get_preorder(root.right, ans)


inorder_nodes = [9, 3, 15, 20, 7]
preorder_nodes = [3, 9, 20, 15, 7]
constructed_root = Solution().buildTree(preorder_nodes, inorder_nodes)
ans = []
Solution().get_preorder(constructed_root, ans)
print("ans:", ans)
