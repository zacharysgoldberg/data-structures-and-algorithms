from helpers import TrieNode


class Trie:
    def __init__(self):
        self.root = TrieNode()  # Root node

    # Function to get the index of character 't'
    def get_index(self, t):
        return ord(t) - ord('a')

    # Function to insert a key in the Trie
    def insert(self, key):
        if key is None:
            return False  # None key

        key = key.lower()  # Keys are stored in lowercase
        current = self.root

        # Iterate over each letter in the key
        # If the letter exists, go down a level
        # Else simply create a TrieNode and go down a level
        for letter in key:
            index = self.get_index(letter)

            if current.children[index] is None:
                current.children[index] = TrieNode(letter)  # Inserted

            current = current.children[index]

        current.is_end_word = True

    # Function to search a given key in Trie
    def search(self, key):
        if key is None:
            return False

        key = key.lower()
        current = self.root

        for letter in key:
            index = self.get_index(letter)
            if current.children[index] is None:
                return False
            current = current.children[index]

        if current and current.is_end_word:
            return True

        return False

    def delete_helper(self, key, current, length, level):
        deleted_self = False
        if current is None:
            return deleted_self
        # Base Case:
        # We have reached at the node which points
        # to the alphabet at the end of the key
        if level is length:
            # If there are no nodes ahead of this node in
            # this path, then we can delete this node
            if current.children.count(None) == len(current.children):
                current = None
                deleted_self = True
            # If there are nodes ahead of current in this path
            # Then we cannot delete current. We simply unmark this as leaf
            else:
                current.is_end_word = False
                deleted_self = False
        else:
            index = self.get_index(key[level])
            child_node = current.children[index]
            child_deleted = self.delete_helper(
                key, child_node, length, level + 1)
            # print( "Returned from", key[level] , "as",  child_deleted)
            if child_deleted:
                # Setting children pointer to None as child is deleted
                current.children[index] = None
                # If current is a leaf node then
                # current is part of another key
                # So, we cannot delete this node and it's parent path nodes
                if current.is_end_word:
                    deleted_self = False
                # If child_node is deleted and current has more children
                # then current must be part of another key
                # So, we cannot delete current Node
                elif current.children.count(None) != len(current.children):
                    deleted_self = False
                # Else we can delete current
                else:
                    current = None
                    deleted_self = True
            else:
                deleted_self = False

        return deleted_self

    # Function to delete given key from Trie
    def delete(self, key):
        if self.root is None or key is None:
            return
        self.delete_helper(key, self.root, len(key), 0)

# Total Number of Words in a Trie


def total_words(root):
    result = 0
    if root.is_end_word:
        result += 1
    for letter in root.children:
        if letter:
            result += total_words(letter)

    return result
