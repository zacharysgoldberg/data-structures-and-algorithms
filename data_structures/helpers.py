class BSTNode:
    def __init__(self, data):
        self.data = data
        self.left, self.right = None, None


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class DoubleNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
