# Node Class:
class Node:
    def _init_(self, val):
        self.data = val
        self.left = None
        self.right = None


# Function to return a list containing elements of left view of the binary tree.
def LeftView(root):
    level = 0
    result = []
    findLeftView(root, level, result)
    return result


def findLeftView(root, level, result):
    if root is None:
        return
    if level == len(result):
        result.append(root.data)
    findLeftView(root.left, level + 1, result)
    findLeftView(root.right, level + 1, result)


