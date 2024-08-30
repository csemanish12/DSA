class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def get_clock_wise_boundary_traversal(self, root: TreeNode):
        ans = []
        if root is None:
            return ans

        if not self.__is_leaf_node(root):
            ans.append(root.val)

        self.__add_right_boundary(root, ans)
        self.__add_leaf_nodes(root, ans)
        self.__add_left_boundary(root, ans)

        return ans

    def __is_leaf_node(self, node):
        return node.left is None and node.right is None

    def __add_left_boundary(self, node, ans):
        curr = node.left
        temp_stack = []

        while curr:
            if not self.__is_leaf_node(curr):
                temp_stack.append(curr.val)

            if curr.left:
                curr = curr.left
            else:
                curr = curr.right
        while temp_stack:
            ans.append(temp_stack.pop())

    def __add_leaf_nodes(self, node, ans):
        if self.__is_leaf_node(node):
            ans.append(node.val)
            return

        if node.right:
            self.__add_leaf_nodes(node.right, ans)

        if node.left:
            self.__add_leaf_nodes(node.left, ans)

    def __add_right_boundary(self, node, ans):
        curr = node.right
        while curr:
            if not self.__is_leaf_node(curr):
                ans.append(curr.val)

            if curr.right:
                curr = curr.right
            else:
                curr = curr.left


root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(3)
root.left.left.right = TreeNode(4)
root.left.left.right.left = TreeNode(5)
root.left.left.right.right = TreeNode(6)
root.right = TreeNode(7)
root.right.right = TreeNode(8)
root.right.right.left = TreeNode(9)
root.right.right.left.left = TreeNode(10)
root.right.right.left.right = TreeNode(11)

expected = [1, 7, 8, 9, 11, 10, 6, 5, 4, 3, 2]

print("output:", Solution().get_clock_wise_boundary_traversal(root))