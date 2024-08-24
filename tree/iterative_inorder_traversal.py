class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Algorithm:
    if node is null:
        push node to stack
        move to left
    else:
        pop from stack  (if stack is empty, break)
        print/collect the data
        move to right

    TC = 0(n)
    SC = 0 (n)
    """
    def iterative_inorder_traversal(self, node):
        inorder = []
        stack = []
        while True:
            if node is not None:
                stack.append(node)
                node = node.left
            else:
                if not stack:
                    break

                node = stack.pop()
                inorder.append(node.val)
                node = node.right

        return inorder


root = TreeNode(1)
child2 = TreeNode(2)
child3 = TreeNode(3)
child4 = TreeNode(4)
child5 = TreeNode(5)
child6 = TreeNode(6)
child7 = TreeNode(7)

root.left = child2
root.right = child3

child2.left = child4
child2.right = child5

child5.left = child6
child5.right = child7

output = Solution().iterative_inorder_traversal(root)
print("output is:", output)
