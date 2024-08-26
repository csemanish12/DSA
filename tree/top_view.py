from collections import deque, defaultdict


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def top_view(self, root):
        q = deque()
        line_map = defaultdict(int)

        q.append((root, 0))
        while q:
            node, level = q.popleft()

            if not line_map.get(level):
                line_map[level] = node

            if node.left:
                q.append((node.left, level - 1))

            if node.right:
                q.append((node.right, level + 1))
        result = []
        for line, node in sorted(line_map.items()):
            result.append(node.val)

        return result


# Creating a sample binary tree
root = Node(1)
root.left = Node(2)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.right.right = Node(6)
root.right = Node(3)
root.right.right = Node(7)

print("output:", Solution().top_view(root))
