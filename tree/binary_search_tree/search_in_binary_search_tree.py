"""
You are given the root of a binary search tree (BST) and an integer val.

Find the node in the BST that the node's value equals val and return the subtree rooted with that node. If such a node does not exist, return null.



Example 1:


Input: root = [4,2,7,1,3], val = 2
Output: [2,1,3]
Example 2:


Input: root = [4,2,7,1,3], val = 5
Output: []


Constraints:

The number of nodes in the tree is in the range [1, 5000].
1 <= Node.val <= 107
root is a binary search tree.
1 <= val <= 107
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def search_in_binary_search_tree(self, root, target):
        while root is not None and root.val != target:
            if root.val < target:
                root = root.right
            else:
                root = root.left

        return root


root = TreeNode(8)
root.left = TreeNode(5)
root.left.left = TreeNode(4)
root.left.right = TreeNode(7)
root.left.right.left = TreeNode(6)
root.right = TreeNode(12)
root.right.left = TreeNode(10)
root.right.right = TreeNode(14)
root.right.right.left = TreeNode(13)

found_node = Solution().search_in_binary_search_tree(root, 11)
if found_node:
    print("target found:", found_node.val)
else:
    print("target not found")
