class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Algorithm:
    Take three lists (preorder, inorder, postorder)
    Insert root and number (inital value =1 ) in to the stack
    Iterate stack until empty:
        pop the top
        if number == 1:
            push to preorder
            increase the number
            push the node and number to stack
            if node has left:
                push node.left to stack with initial number 1

        elif number == 2:
            push to ineorder
            increase the number
            push the node and number to stack
            if node has right:
                push node.right to stack with initial number 1

        else:
            push to postorder


    TC = 0(3*n)
    SC = 0 (4*n)
    """
    def combined_traversal(self, node):
        preorder = []
        inorder = []
        postorder = []
        if node is None:
            return preorder, inorder, postorder

        stack = [(node, 1)]
        while stack:
            node, number = stack.pop()

            if number == 1:
                preorder.append(node.val)
                number += 1
                stack.append((node, number))

                if node.left:
                    stack.append((node.left, 1))

            elif number == 2:
                inorder.append(node.val)
                number += 1
                stack.append((node, number))

                if node.right:
                    stack.append((node.right, 1))
            else:
                postorder.append(node.val)

        return preorder, inorder, postorder


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

output = Solution().combined_traversal(root)
print("preorder is:", output[0])
print("inorder is:", output[1])
print("postorder is:", output[2])
