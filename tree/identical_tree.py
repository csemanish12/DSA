from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def is_identical(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None or q is None:
            return p == q

        return (p.val == q.val) and self.is_identical(p.left, q.left) and self.is_identical(p.right, q.right)


root_p = TreeNode(1)
root_q = TreeNode(1)
child1_p = TreeNode(2)
child1_q = TreeNode(2)
child2_p = TreeNode(3)
child2_q = TreeNode(3)

root_p.right = child1_p
root_q.right = child1_q
child1_p.left = child2_p
child1_q.left = child2_q

print("is identical:", Solution().is_identical(root_p, root_q))
