from collections import deque, defaultdict


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def bottom_view(self, root):
        q = deque()
        line_map = defaultdict(int)

        q.append((root, 0))
        while q:
            node, level = q.popleft()
            line_map[level] = node.val

            if node.left:
                q.append((node.left, level - 1))

            if node.right:
                q.append((node.right, level + 1))
        result = []
        for line, node_val in sorted(line_map.items()):
            result.append(node_val)

        return result


# Creating a sample binary tree
root = Node(1)
root.left = Node(2)
root.left.left = Node(4)
root.left.right = Node(10)
root.left.left.right = Node(5)
root.left.left.right.right = Node(6)
root.right = Node(3)
root.right.right = Node(10)
root.right.left = Node(9)

print("output:", Solution().bottom_view(root))
