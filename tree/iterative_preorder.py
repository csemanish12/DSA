class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorder_iterative_traversal(self, root):
        ans = []
        if root is None:
            return ans

        stack = [root]
        while stack:
            node = stack.pop()
            ans.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return ans


root = TreeNode(1)
child1 = TreeNode(2)
child2 = TreeNode(3)
root.right = child1
child1.left = child2

output = Solution().preorder_iterative_traversal(root)
print("output is:", output)
