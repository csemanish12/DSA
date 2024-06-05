"""
Implement stack using list by maintaining top pointer
"""


class StackViaList:
    top = -1
    capacity = 5
    stack = [None for _ in range(capacity)]

    def push(self, element):
        if self.top + 1 == self.capacity:
            print("stack is full.")
            return
        self.top += 1
        self.stack[self.top] = element
        print("pushed element:", element)

    def pop(self):
        if self.top == -1:
            print("stack is empty")
            return
        element = self.stack[self.top]
        print("popped element:", element)
        self.stack[self.top] = None
        self.top -= 1
        return element

    def debug_stack(self):
        print(f"debug-> stack:{self.stack}, top:{self.top}")


my_stack = StackViaList()
my_stack.push(1)
my_stack.push(2)
my_stack.pop()