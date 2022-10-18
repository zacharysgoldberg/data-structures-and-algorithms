from helpers import BSTNode
from collections import deque
import pickle
import sys


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
        nodes = [root]
        while nodes:
            print(str(nodes[0].data) + " ", end="")
            node = nodes.pop(0)
            if node.left:
                nodes.append(node.left)
            if node.right:
                nodes.append(node.right)

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

    def level_order_averages(self, root):
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

    def level_order_successor(self, root, key):
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

    def connect_level_order_siblings(self, root):
        nodes = [root]
        while nodes:
            prev = None
            for _ in range(len(nodes)):
                node = nodes.pop(0)
                if prev:
                    prev.next = node
                prev = node
                if node.left:
                    nodes.append(node.left)
                if node.right:
                    nodes.append(node.right)
    """
    Converting a tree into a doubly linked list
    """

    prev = None

    def convert_to_linked_list(self, root):
        if root:
            head = self.convert_to_linked_list(root.left)
            global prev
            if prev:
                root.left = prev
                prev.right = root
            else:
                head = root

            prev = root
            self.convert_to_linked_list(root.right)
            return head
        return None

    # [Print Tree Perimeter]
    def display_tree_perimeter(self, root):
        result = []
        self.left_perimeter(root, result)
        self.leaf_nodes(root.left, result)
        self.leaf_nodes(root.right, result)
        self.right_perimeter(root, result)
        result.pop()
        return " ".join(map(str, result))

    def leaf_nodes(self, root, result):
        if root:
            self.leaf_nodes(root.left, result)
            if root.left is None and root.right is None:
                result.append(root.data)

            self.leaf_nodes(root.right, result)

    def left_perimeter(self, root, result):
        if root:
            if root.left:
                result.append(root.data)
                self.left_perimeter(root.left, result)
            elif root.right:
                result.append(root.data)
                self.left_perimeter(root.right, result)

    def right_perimeter(self, root, result):
        if root:
            if root.right:
                self.right_perimeter(root.right, result)
                result.append(root.data)
            elif root.left:
                self.right_perimeter(root.left, result)
                result.append(root.data)

# ================================================================

    def populate_sibling_pointers(self, root):
        curr = root
        last = root
        while curr:
            if curr.left:
                last.next = curr.left
                last = curr.left
            if curr.right:
                last.next = curr.right
                last = curr.right
            curr = curr.next
        return root
    # [Serialize/Deserialize BST]

    def serialize(self, node, stream):
        if node is None:
            stream.dump(sys.maxsize)    # Marker for null pointers
            return
        stream.dump(node.data)
        self.serialize(node.left, stream)
        self.serialize(node.right, stream)

    def deserialize(self, stream):
        try:
            data = pickle.load(stream)
            if data == sys.maxsize:
                return None

            node = BSTNode(data)
            node.left = self.deserialize(stream)
            node.right = self.deserialize(stream)
            return node
        except pickle.UnpicklingError:
            return None

# =============================================================

    def find_nth_highest_in_bst(self, node, n):
        if node is None:
            return None

        left_count = 0
        if node.left:
            left_count = node.left.count
        k = node.count - left_count

        if k == n:
            return node
        elif k > n:
            return self.find_nth_highest_in_bst(node.right, n)
        else:
            return self.find_nth_highest_in_bst(node.left, n - k)

    def mirror_tree(self, root):
        if root is None:
            return None
        if root.left:
            self.mirror_tree(root.left)

        if root.right:
            self.mirror_tree(root.right)

        temp = root.left
        root.left = root.right
        root.right = temp
        return root

# [ Delete Zero Sum Sub Tree]

    def helper(self, root):
        if root is None:
            return 0
        sum_left = self.helper(root.left)
        sum_right = self.helper(root.right)
        if sum_left == 0:
            root.left = None
        if sum_right == 0:
            root.right = None
        return root.data + sum_left + sum_right

    def delete_zero_sum_subtree(self, root):
        if root:
            zero_sum = self.self.helper(root)
            if zero_sum == 0:
                root = None
        return
# Convert binary tree to n ary

    def convert_n_ary_to_binary(self, node):
        return self.convert_to_binary(node, 'left')

    def convert_to_binary(self, root, direction):
        node = self.BSTNode(root.data)
        last = node

        for child in root.children:
            if direction == 'left':
                last.left = self.convert_to_binary(child, 'right')
                last = last.left
            elif direction == 'right':
                last.right = self.convert_to_binary(child, 'left')
                last = last.right

        return node

    def convert_binary_to_n_ary(self, node):
        return self.convert_to_n_ary(node, 'left')

    def convert_to_n_ary(self, root, direction):
        node = BSTNode(root.data)
        temp = node
        if direction == 'left':
            while temp.left:
                child = self.convert_to_n_ary(node.left, 'right')
                node.children.append(child)
                temp = temp.left
        elif direction == 'right':
            while temp.right:
                child = self.convert_to_n_ary(node.right, 'left')
                node.children.append(child)
                temp = temp.right
        return root

    # =======================================================

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
        new_node = BSTNode(val)
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
        #     self.root = BSTNode(val)
        # else:
        #     self.insertion(self.root, val)

        return root

    # [for recursion]
    def insertion(self, cur, val):
        if not cur:
            curr = BSTNode(val)
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

    def is_bst(self, root):
        global prev
        if root:
            if not self.is_bst(root.left):
                return False
            if prev and root.data <= prev.data:
                return False
            prev = root
            return self.is_bst(root.right)

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


def display_tree_perimeter(root):
  result = ""
  left = []
  while root:
    node = root.data
    if root.left:
      root = root.left
    elif root.right:
      root = root.right
    else:
      break
    left.append(str(node)


  # print(result)
  # print(right)
  return left
