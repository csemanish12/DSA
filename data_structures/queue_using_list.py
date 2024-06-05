"""
Uses circular array concept to implement queue

"""


class QueueViaList:
    capacity = 5
    front = 0
    rear = 0
    count = 0
    queue = [0 for _ in range(capacity)]

    def push(self, element):
        print("trying to push:", element)
        if self.count == self.capacity:
            print("Queue is full")
            return

        empty_index = self.rear % self.capacity
        self.queue[empty_index] = element
        self.rear += 1
        self.count += 1

        self.debug_queue()

    def pop(self):
        if self.count == 0:
            print("Queue is empty")
            return

        front_index = self.front % self.capacity
        element = self.queue[front_index]
        self.queue[front_index] = None
        self.count -= 1
        self.front += 1
        print("popped element is:", element)
        self.debug_queue()
        return element

    def debug_queue(self):
        print("queue:", self.queue, " rear is:", self.rear, " front is:", self.front)


q = QueueViaList()
q.push(1)
q.push(2)
q.push(3)
q.push(4)
q.push(5)
q.push(6)
q.pop()
q.pop()
q.push(7)