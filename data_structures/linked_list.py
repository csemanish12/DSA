class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def create_linked_list(numbers) -> Node:
    head = Node(numbers[0])
    mover = head
    for i in range(1, len(numbers)):
        new_node = Node(numbers[i])
        mover.next = new_node
        mover = new_node

    return head


def print_linked_list(head_node):
    current = head_node
    while current.next:
        print(current.data)
        current = current.next
    print(current.data)


numbers = [2, 1, 3, 4, 5]
head_node = create_linked_list(numbers)
print_linked_list(head_node)
