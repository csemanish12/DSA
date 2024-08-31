from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthLargest(self, root: Optional[TreeNode], k: int) -> int:
        count = [0]
        kth = [float('-inf')]
        self.get_kth_element(root, k, count, kth)

        return kth[0]

    def get_kth_element(self, root, k, count, kth):
        if root is None or count[0] >= k:
            return

        self.get_kth_element(root.right, k, count, kth)
        count[0] += 1

        if count[0] == k:
            kth[0] = root.val
            return

        self.get_kth_element(root.left, k, count, kth)


root = TreeNode(3)
root.left = TreeNode(1)
root.left.right = TreeNode(2)
root.right = TreeNode(4)

print("output:", Solution().kthLargest(root, 1))