class Node:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class DequeSolution:
    rear = None
    front = None
    size = 0
    capacity = 5

    def insert_front(self, element):
        if self.size == self.capacity:
            print("queue is full")
            return None

        node = Node(element)
        if self.front is None:
            self.front = self.rear = node
        else:
            node.next = self.front
            self.front.prev = node
            self.front = node
        self.size += 1
        print("element inserted at front:", element)

    def insert_rear(self, element):
        if self.size == self.capacity:
            print("queue is full")
            return None

        node = Node(element)
        if self.rear is None:
            self.rear = self.front = node
        else:
            node.prev = self.rear
            self.rear.next = node
            self.rear = node
        self.size += 1
        print("element inserted at rear:", element)

    def remove_rear(self):
        if self.is_empty():
            print("queue is empty. cannot remove from rear")
            return
        print("removing element from rear:", self.rear.data)

        self.rear = self.rear.prev

        if self.rear is None:
            self.front = None
        else:
            self.rear.next = None

        self.size -= 1

    def remove_front(self):
        if self.is_empty():
            print("queue is empty cannot remove from rear")
            return
        print("removing element from front:", self.front.data)

        self.front = self.front.next

        if self.front is None:
            self.rear = None
        else:
            self.front.prev = None

        self.size -= 1

    def get_rear(self):
        if self.is_empty():
            print("queue is empty")
            return

        print("rear is:", self.rear.data)

    def get_front(self):
        if self.is_empty():
            print("queue is empty")
            return

        print("front is:", self.front.data)

    def is_empty(self):
        return self.front is None


s = DequeSolution()
s.get_rear()
s.insert_rear(5)
s.insert_rear(10)
s.get_rear()
s.get_front()
s.remove_rear()
s.insert_front(15)
s.get_front()
s.get_rear()
s.remove_front()
s.remove_front()
s.remove_front()
