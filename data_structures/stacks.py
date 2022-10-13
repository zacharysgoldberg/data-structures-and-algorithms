class MyStack:
    def __init__(self):
        self.stack_list = []
        # self.stack_size = 0

    def is_empty(self):
        return len(self.stack_list) == 0

    def peek(self):
        if self.is_empty():
            return None
        return self.stack_list[-1]

    def size(self):
        return len(self.stack_list)

    def push(self, value):
        self.stack_list.append(value)

    def pop(self):
        if self.is_empty():
            return None
        return self.stack_list.pop()


class MinStack:
    # Constructor
    def __init__(self):
        self.main_stack = MyStack()
        self.min_stack = MyStack()

    def pop(self):
        if self.main_stack and self.min_stack:
            self.min_stack.pop()
            return self.main_stack.pop()
        return None

    # Pushes value into new stack
    def push(self, value):
        self.main_stack.push(value)

    # Returns minimum value from new stack in constant time
    def min(self):
        if self.main_stack:
            self.min_stack.push(min(self.main_stack.stack_list))
            return self.min_stack.peek()
        return None
