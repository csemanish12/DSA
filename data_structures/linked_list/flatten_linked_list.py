class Node:
    def __init__(self, data, next=None, bottom=None):
        self.data = data
        self.next = next
        self.bottom = bottom


def flatten(root):
    if root is None or root.next is None:
        return root
    root.next = flatten(root.next)
    root = merge(root, root.next)

    return root


def merge(l1, l2):
    temp = result = Node(0)
    while l1 is not None and l2 is not None:
        if l1.data < l2.data:
            temp.bottom = l1
            temp = temp.bottom
            l1 = l1.bottom
        else:
            temp.bottom = l2
            temp = temp.bottom
            l2 = l2.bottom

    if l1 is not None:
        temp.bottom = l1
    else:
        temp.bottom = l2

    return result.bottom


def printList(node):
    while (node is not None):
        print(node.data, end=" ")
        node = node.bottom

    print()


if __name__ == "__main__":
    t = int(input())
    while (t > 0):
        head = None
        N = int(input())
        arr = []

        arr = [int(x) for x in input().strip().split()]
        temp = None
        tempB = None
        pre = None
        preB = None

        flag = 1
        flag1 = 1
        listo = [int(x) for x in input().strip().split()]
        it = 0
        for i in range(N):
            m = arr[i]
            m -= 1
            a1 = listo[it]
            it += 1
            temp = Node(a1)
            if flag == 1:
                head = temp
                pre = temp
                flag = 0
                flag1 = 1
            else:
                pre.next = temp
                pre = temp
                flag1 = 1

            for j in range(m):
                a = listo[it]
                it += 1
                tempB = Node(a)
                if flag1 == 1:
                    temp.bottom = tempB
                    preB = tempB
                    flag1 = 0
                else:
                    preB.bottom = tempB
                    preB = tempB
        root = flatten(head)
        printList(root)

        t -= 1

# } Driver Code Ends