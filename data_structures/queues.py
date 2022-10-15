from doubly_linked_lists import DoublyLinkedList
from stacks import MyStack

# [Using Doubly Linked Lists/Nodes]


class MyQueue:
    def __init__(self):
        self.items = DoublyLinkedList()

    def is_empty(self):
        return self.items.length() == 0

    def front(self):
        if self.is_empty():
            return None
        return self.items.head.data

    def rear(self):
        if self.is_empty():
            return None
        return self.items.tail.data

    def size(self):
        return self.items.length()

    def enqueue(self, value):
        return self.items.insert_tail(value)

    def dequeue(self):
        return self.items.remove_head()

    def reverse_k(self, queue, k):
        # Handling invalid input
        if queue.is_empty() is True or k > queue.size() or k < 0:
            return None
        stack = MyStack()
        for i in range(k):
            stack.push(queue.dequeue())
        while stack.is_empty() is False:
            queue.enqueue(stack.pop())
        size = queue.size()
        for i in range(size - k):
            queue.enqueue(queue.dequeue())

        return queue

    def print_list(self):
        return self.items.__str__()


# [Using Stacks]
class NewQueue:
    def __init__(self):
        self.main_stack = MyStack()
        self.temp_stack = MyStack()

    # Inserts Element in the Queue

    def enqueue(self, value):
        self.main_stack.push(value)
        return self.main_stack.peek()

    # Removes Element From Queue

    def dequeue(self):
        if self.main_stack.is_empty() and self.temp_stack.is_empty():
            return None

        while not self.main_stack.is_empty():
            value = self.main_stack.pop()
            self.temp_stack.push(value)
        return self.temp_stack.pop()


queue_obj = MyQueue()
print("queue.enqueue(2);")
queue_obj.enqueue(2)
print("queue.enqueue(4);")
queue_obj.enqueue(4)
print("queue.enqueue(6);")
queue_obj.enqueue(6)
print("queue.enqueue(8);")
queue_obj.enqueue(8)
print("queue.enqueue(10);")
queue_obj.enqueue(10)

queue_obj.print_list()

print("is_empty(): " + str(queue_obj.is_empty()))
print("front(): " + str(queue_obj.front()))
print("rear(): " + str(queue_obj.rear()))
print("size(): " + str(queue_obj.size()))
