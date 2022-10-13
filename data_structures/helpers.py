class BinarySearchTreeNode:
    def __init__(self, data):
        self.info = data
        self.left = None
        self.right = None


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class DoubleNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
