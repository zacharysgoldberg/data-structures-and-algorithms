from helpers import BinarySearchTreeNode
from collections import deque


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def preorder(self, root):
        if root:
            print(root.data, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.info, end=" ")

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.info, end=" ")
            self.inorder(root.right)

    def inorder_iterative(self, root):
        if root is None:
            return
        stack = []
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
                continue
            node = stack.pop()
            print(node.data, end=" ")
            root = node.right

        """
        Find the value d in BST.
        If d has a right child then the left most child in right child's subtree will be the in-order successor of d
        This would also be the child with the minimum value in that subtree.
        If d has no right child then:
            in-order successor is NULL if d is right most node in the BST i.e. last node in the in-order traversal.
            in-order successor is the node with minimum value higher than d in the parent chain of d.

        NOTE: only update/assign the successor whenever we move towards a left node, i.e. a smaller node while looking for the input node.
        """

    def find_min_in_tree(self, root):
        if root is None:
            return None

        while root.left:
            root = root.left

        return root

    def inorder_successor_bst_parent_pointer(self, node):
        if node is None:
            return None

        if node.right:
            return self.find_min_in_tree(node.right)

        while node.parent:
            if node.parent.left == node:
                return node.parent
            node = node.parent

        return None

    def find_successor(self, root, d):
        successor = None
        while root:
            if (root.data < d):
                root = root.right
            elif (root.data > d):
                successor = root
                root = root.left
            else:
                return self.inorder_successor_bst_parent_pointer(root)

        return successor

    def inorder_successor_no_helper(self, root, d):
        if root is None:
            return None
        successor = None
        while root:
            if root.data > d:
                successor = root
                root = root.left
            elif root.data < d:
                root = root.right
            else:
                if root.right:
                    root = root.right
                    while root.left:
                        root = root.left
                    return root
                break
        return successor

    def are_identical(self, root1, root2):
        if root1 is None and root2 is None:
            return True

        if root1 is not None and root2 is not None:
            return root1.data == root2.data and \
                self.are_identical(root1.left, root2.left) and \
                self.are_identical(root1.right, root2.right)

        return False

    def height(self, root):
        if root:
            l = self.height(root.left)
            r = self.height(root.right)
            if r > l:
                return r + 1
            return l + 1
        return -1

    def level_order(self, root):
        result = ""
        nodes = [root]
        while nodes:
            result += str(nodes[0].data) + " "
            node = nodes.pop(0)
            if node.left:
                nodes.append(node.left)
            if node.right:
                nodes.append(node.right)
        return result

    def reverse_level_order(self, root):
        result = deque()
        nodes = [root]
        while nodes:
            curr_level = []
            for _ in range(len(nodes)):
                node = nodes.pop(0)
                curr_level.append(node.data)
                if node.left:
                    nodes.append(node.left)
                if node.right:
                    nodes.append(node.right)
            result.appendleft(curr_level)

        return result

    def find_level_averages(self, root):
        result = []
        nodes = [root]
        while nodes:
            curr_level = []
            for _ in range(len(nodes)):
                node = nodes.pop(0)
                curr_level.append(node.data)
                if node.left:
                    nodes.append(node.left)
                if node.right:
                    nodes.append(node.right)
            result.append(sum(curr_level) / len(curr_level))

        return result

    def find_level_order_successor(self, root, key):
        if root is None:
            return None
        res = [root]
        while res:
            node = res.pop(0)
            if node.left:
                res.append(node.left)
            if node.right:
                res.append(node.right)
            if node.data == key:
                return res[0]

        return None

    def zig_zag_level_order(self, root):
        result = []
        nodes = [root]
        zig_zag = False
        while nodes:
            curr_level = []
            for _ in range(len(nodes)):
                node = nodes.pop(0)
            if zig_zag is True:
                curr_level.insert(0, node.val)
            else:
                curr_level.append(node.val)
            if node.left:
                nodes.append(node.left)
            if node.right:
                nodes.append(node.right)
            result.append(curr_level)
            zig_zag = not zig_zag   # Reverses truthy or falsey

        return result

    def top_view(self, root):
        level = [(root, 0)]
        viewable = {}
        while level:
            node, data = level.pop(0)
            if data not in viewable:
                viewable[data] = node.info
            if node.left:
                level.append((node.left, data - 1))
            if node.right:
                level.append((node.right, data + 1))

        for data in sorted(viewable):
            print(viewable[data], end=" ")

    def insert(self, val):
        new_node = BinarySearchTreeNode(val)
        if not self.root:
            self.root = new_node
            return self.root
        root = self.root
        while root:
            if root.info > val:
                if root.left:
                    root = root.left
                else:
                    root.left = new_node
                    break
            else:
                if root.right:
                    root = root.right
                else:
                    root.right = new_node
                    break
        # [for recursion]
        # if not self.root:
        #     self.root = BinarySearchTreeNode(val)
        # else:
        #     self.insertion(self.root, val)

        return root

    # [for recursion]
    def insertion(self, cur, val):
        if not cur:
            curr = BinarySearchTreeNode(val)
        elif curr.info > val:
            curr.left = self.insertion(curr.left, val)
        else:
            curr.right = self.insertion(curr.right, val)

        return curr

    # [Lowest common ancestor]
    def lca(self, root, v1, v2):
        node = root
        while node:
            if max(v1, v2) < node.info:
                node = node.left
            elif min(v1, v2) > node.info:
                node = node.right
            else:
                return node

    def decode_huff(self, root, string):
        node = root
        # for s in string:
        #     if s == '0':
        #         node = node.left
        #     elif s == '1':
        #         node = node.right
        #     if node.data != '\0':
        #         print(node.data, end="")
        #         node = root

        decoded = ''
        for i in range(len(string)):
            if string[i] == '0':
                node = node.left
            else:
                node = node.right
            if not node.left or not node.right:
                decoded += node.data
                node = root
        print(decoded)
# ==================================================================================================
    prev = None

    def check_binary_search_tree_(self, root):
        global prev
        if root:
            if not self.check_binary_search_tree_(root.left):
                return False
            if prev and root.data <= prev.data:
                return False
            prev = root
            return self.check_binary_search_tree_(root.right)

        return True


class InorderIterator:
    def __init__(self, root):
        self.stack = []
        self.push(root)

    def push(self, root):
        while root:
            self.stack.append(root)
            root = root.left

    def has_next(self):
        if not self.stack:
            return False
        return True
    # getNext returns null if there are no more elements in tree

    def get_next(self):
        if not self.stack:
            return None
        val = self.stack.pop()
        self.push(val.right)
        return val
