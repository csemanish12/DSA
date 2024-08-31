class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def delete_node(self, root, target):
        if root is None:
            return
        if root.val == target:
            return self.helper(root)

        dummy = root
        while root is not None:
            if root.val > target:
                if root.left is not None and root.left.val == target:
                    root.left = self.helper(root.left)
                    break
                else:
                    root = root.left
            else:
                if root.right is not None and root.right.val == target:
                    root.right = self.helper(root.right)
                    break
                else:
                    root = root.right

        return dummy

    def helper(self, root):
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        else:
            right_child = root.right
            last_right = self.find_last_right(root.left)
            last_right.right = right_child
            return root.left

    def find_last_right(self, root):
        if root.right is None:
            return root
        return self.find_last_right(root.right)


def print_inorder(root: TreeNode):
    if root is None:
        return
    print_inorder(root.left)
    print(root.val)
    print_inorder(root.right)


root = TreeNode(8)
root.left = TreeNode(5)
root.left.left = TreeNode(2)
root.left.left.left = TreeNode(1)
root.left.left.right = TreeNode(3)
root.left.left.right.right = TreeNode(4)
root.left.right = TreeNode(7)
root.left.right.left = TreeNode(6)
root.left.right.right = TreeNode(8)
root.right = TreeNode(12)

node = Solution().delete_node(root, 5)
print_inorder(node)