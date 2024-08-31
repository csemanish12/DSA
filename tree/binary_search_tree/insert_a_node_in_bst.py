class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def insert_node(self, root, target):
        if root is None:
            return TreeNode(target)

        curr = root
        while True:
            if curr.val <= target:
                if curr.right is not None:
                    curr = curr.right
                else:
                    curr.right = TreeNode(target)
                    break
            else:
                if curr.left is not None:
                    curr = curr.left
                else:
                    curr.left = TreeNode(target)
                    break

        return root

    def print_inorder(self, root):
        if root is None:
            return

        self.print_inorder(root.left)
        print(root.val)
        self.print_inorder(root.right)


root = TreeNode(6)
root.left = TreeNode(3)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right = TreeNode(8)
root.right.left = TreeNode(7)

node = Solution().insert_node(root, 5)
Solution().print_inorder(node)
