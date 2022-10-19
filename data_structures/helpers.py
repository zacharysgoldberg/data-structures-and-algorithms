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


class TrieNode:
    def __init__(self, char=''):
        self.children = [None] * 26  # This will store pointers to the children
        self.is_end_word = False  # true if the node represents the end of word
        self.char = char  # To store the value of a particular key
