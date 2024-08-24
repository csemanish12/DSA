class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Algorithm:
    put the root in stack 1
    iterate until stack1 is empty:
        pop the top
        if top has left, push it to stack 1
        if top has right, push it to stack 1
        push top to stack 2

    iterate over stack 2:
         pop the top
         add in ans list


    TC = 0(n)
    SC = 0 (n)
    """
    def iterative_postorder_traversal(self, node):
        postorder = []
        stack1 = [node]
        stack2 = []

        while stack1:
            top = stack1.pop()
            if top.left:
                stack1.append(top.left)

            if top.right:
                stack1.append(top.right)

            stack2.append(top)
        while stack2:
            postorder.append(stack2.pop().val)

        return postorder


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

output = Solution().iterative_postorder_traversal(root)
print("output is:", output)
