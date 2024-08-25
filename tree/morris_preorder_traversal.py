from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Using Morris
    - by creating threads from right most node to its root.
    """
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        inorder = []
        cur = root
        while cur is not None:
            if cur.left is None:
                inorder.append(cur.val)
                cur = cur.right

            else:
                prev = cur.left
                while prev.right and prev.right != cur:
                    prev = prev.right

                if prev.right is None:
                    prev.right = cur
                    inorder.append(cur.val)
                    cur = cur.left
                else:
                    prev.right = None
                    cur = cur.right
        return inorder


root = TreeNode(1)
child1 = TreeNode(2)
child2 = TreeNode(3)
root.right = child1
child1.left = child2

output = Solution().preorderTraversal(root)
print("output is: ", output)
