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

        if self.rear >= self.capacity:
            empty_index = self.rear % self.capacity
            print("empty index is now:", empty_index)
            self.queue[empty_index] = element
        else:
            self.queue[self.rear] = element

        self.rear += 1
        self.count += 1

    def pop(self):
        if self.count == 0:
            print("Queue is empty")
            return

        element = self.queue[self.front]
        self.queue[self.front] = None
        self.count -= 1
        if self.front == self.capacity - 1:
            self.front = 0
        else:
            self.front += 1
        print("popped element is:", element)
        return element

    def debug_queue(self):
        print("queue:", self.queue, " rear is:", self.rear, " front is:", self.front)

