"""
Given the root of a binary tree, return the postorder traversal of its nodes' values.


Example 1:


Input: root = [1,null,2,3]
Output: [3,2,1]
Example 2:

Input: root = []
Output: []
Example 3:

Input: root = [1]
Output: [1]


Constraints:

The number of the nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100


Follow up: Recursive solution is trivial, could you do it iteratively?
"""


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root):
        ans = []
        self.postorder(root, ans)

        return ans

    def postorder(self, root, ans):
        if root is None:
            return

        self.postorder(root.left, ans)
        self.postorder(root.right, ans)
        ans.append(root.val)


root = TreeNode(1)
child1 = TreeNode(2)
child2 = TreeNode(3)
root.right = child1
child1.left = child2

output = Solution().postorderTraversal(root)
print("output is:", output)
