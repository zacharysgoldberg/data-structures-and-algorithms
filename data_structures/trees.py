from heapq import heappush, heappop, _siftup, _siftdown
from helpers import BSTNode
from collections import deque
import pickle
import sys
from heapq import *


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
            print(root.data, end=" ")
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

        return (root1 and root2) and (root1.data == root2.data) \
            and self.are_identical(root1.left, root2.left) and \
            self.are_identical(root1.right, root2.right)

        # if root1 is None and root2 is None:
        #     return True

        # if root1 is not None and root2 is not None:
        #     return root1.data == root2.data and \
        #         self.are_identical(root1.left, root2.left) and \
        #         self.are_identical(root1.right, root2.right)

        # return False

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
                    curr_level.insert(0, node.data)
                else:
                    curr_level.append(node.data)
                if node.left:
                    nodes.append(node.left)
                if node.right:
                    nodes.append(node.right)
            result.append(curr_level)
            zig_zag = not zig_zag

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

    def find_minimum_depth(self, root):
        if root is None:
            return 0
        stack = [root]
        min_depth = 0
        while stack:
            min_depth += 1
            for _ in range(len(stack)):
                node = stack.pop(0)
            if node.left is None and node.right is None:
                return min_depth
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

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
            zero_sum = self.helper(root)
            if zero_sum == 0:
                root = None
        return
# Convert binary tree to n ary

    def convert_n_ary_to_binary(self, node):
        return self.convert_to_binary(node, 'left')

    def convert_to_binary(self, root, direction):
        node = BSTNode(root.data)
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

    # [for recursion]
    def insertion(self, curr, val):
        if not curr:
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

    def tree_sum(self, root):
        if root is None:
            return 0
        left_sum = self.tree_sum(root.left)
        right_sum = self.tree_sum(root.right)
        return root.data + left_sum + right_sum

    def tree_max(self, root):
        if root is None:
            return float('-inf')
        left_max = self.tree_max(root.left)
        right_max = self.tree_max(root.right)
        return max(root.data, left_max, right_max)

    def tree_height(self, root):
        if root is None:
            return -1
        left_height = self.tree_height(root.left)
        right_height = self.tree_height(root.right)
        return 1 + max(left_height, right_height)

    def exists_in_tree(self, root, val):
        if root is None:
            return False
        left = self.exists_in_tree(root.left, val)
        right = self.exists_in_tree(root.right, val)
        return root.data == val or (left or right)

    def reverse_tree(self, root):
        if root is None:
            return
        self.reverse_level_order(root.left)
        self.reverse_level_order(root.right)
        root.left, root.right = root.right, root.left

    # space complexity O(h)
    def is_bst(self, root, min=float('-inf'), max=float('inf')):
        if root is None:
            return True
        elif not min < root.data < max:
            return False
        else:
            return self.is_bst(root.left, min, root.data) and \
                self.is_bst(root.right, root.data, max)

    # All Paths with a sum of s
    def finding_paths(self, root, s, curr_path, all_paths, curr_sum):
        if root is None:
            return

        curr_path.append(root.data)
        curr_sum += root.data
        if curr_sum == s and root.left is None and root.right is None:
            all_paths.append(list(curr_path))
        # print(curr_path, curr_sum)
        self.finding_paths(root.left, s,
                           curr_path, all_paths, curr_sum)
        self.finding_paths(root.right, s,
                           curr_path, all_paths, curr_sum)
        del curr_path[-1]
        return all_paths

    def find_paths(self, root, s):
        all_paths = []
        return self.finding_paths(root, s, [], all_paths, 0)

# ==============================================================================

    # Sum of Path numbers
    def find_sum(self, root, curr_sum):
        if root is None:
            return 0
        curr_sum = 10 * curr_sum + root.val
        print(curr_sum)
        if root.left is None and root.right is None:
            return curr_sum
        return self.find_sum(root.left, curr_sum) + self.find_sum(root.right, curr_sum)

    def find_sum_of_path_numbers(self, root):
        return self.find_sum(root, 0)
# =======================================================================================

    # Path With a Given Sequence
    # 0(n) space complexity
    def find_path_rec(self, root, sequence, curr_path, all_paths):
        if root is None:
            return False

        curr_path.append(root.data)
        if root.left is None and root.right is None:
            all_paths.append(list(curr_path))

        self.find_path_rec(root.left, sequence, curr_path, all_paths)
        self.find_path_rec(root.right, sequence, curr_path, all_paths)
        del curr_path[-1]
        if sequence in all_paths:
            return True

        return False

    def find_path(self, root, sequence):
        return self.find_path_rec(root, sequence, [], [])

    # O(1) space complexity

    def find_seq_path(self, root, sequence):
        if not root:
            return len(sequence) == 0

        return self.find_seq_path_recursive(root, sequence, 0)

    def find_seq_path_recursive(self, root, sequence, index):
        if root is None:
            return False

        if index >= len(sequence) or root.data != sequence[index]:
            return False
        # if the current node is a leaf, add it as the end of the sequence, we have found a path!
        if root.left is None and root.right is None and index == len(sequence) - 1:
            return True
        # recursively call to traverse the left and right sub-tree
        # return true if any of the two recursive call return true
        return self.find_seq_path_recursive(root.left, sequence, index + 1) or \
            self.find_seq_path_recursive(
                root.right, sequence, index + 1)

# ========================================================================

    # O(n) space complexity
    def count_paths_rec(self, root, S, curr_path):
        if root is None:
            return 0

        curr_path.append(root.val)
        path_sum, total_count = 0, 0
        for i in range(len(curr_path) - 1, -1, -1):
            path_sum += curr_path[i]
            if path_sum == S:
                total_count += 1

        total_count += self.count_paths_rec(root.left, S, curr_path)
        total_count += self.count_paths_rec(root.right, S, curr_path)
        del curr_path[-1]
        return total_count

    def count_paths(self, root, S):
        return self.count_paths_rec(root, S, [])

# ================================================================================


# Find the Median of a Number Stream (Heap Queues)


class MedianStream:
    def __init__(self):
        self.max_heap = []
        self.min_heap = []

    def insert_num(self, num):
        if not self.max_heap or num <= -self.max_heap[0]:
            # use negative value for max heap because heappop removes and returns the lowest heap value in a list
            heappush(self.max_heap, -num)
        else:
            heappush(self.min_heap, num)

        if len(self.max_heap) > len(self.min_heap) + 1:
            heappush(self.min_heap, -heappop(self.max_heap))
        elif len(self.max_heap) < len(self.min_heap):
            heappush(self.max_heap, -heappop(self.min_heap))

    def find_median(self):
        if len(self.max_heap) == len(self.min_heap):
            med = (-self.max_heap[0] + self.min_heap[0]) / 2
            return med
        return float(-self.max_heap[0])


class SlidingWindowMedian:
    def __init__(self):
        self.max_heaps = []
        self.min_heaps = []

    def find_sliding_window_median(self, nums, k):
        result = []
        for i in range(len(nums)):
            if not self.max_heaps or nums[i] <= -self.max_heaps[0]:
                heappush(self.max_heaps, -nums[i])
            else:
                heappush(self.min_heaps, nums[i])
            self.rebalance_heaps()
            # if we have at least 'k' elements in the sliding window
            if i - k + 1 >= 0:
                # if k is even
                if k % 2 == 0:
                    med = (-self.max_heaps[0] + self.min_heaps[0]) / 2
                    result.append(med)
                # if k is odd
                else:
                    med = float(-self.max_heaps[0])
                    result.append(med)
                # remove the element going out of the sliding window
                heap = nums[i - k + 1]
                if heap <= -self.max_heaps[0]:
                    self.remove_heap(self.max_heaps, -heap)
                else:
                    self.remove_heap(self.min_heaps, heap)
                self.rebalance_heaps()
        return result

        """
        either both the heaps will have equal number of elements 
        or max-heap will have one more element than the min-heap
        """

    def rebalance_heaps(self):
        if len(self.max_heaps) > len(self.min_heaps) + 1:
            heappush(self.min_heaps, -heappop(self.max_heaps))
        elif len(self.max_heaps) < len(self.min_heaps):
            heappush(self.max_heaps, -heappop(self.min_heaps))

    def remove_heap(self, heap_list, heap):
        index = heap_list.index(heap)
        # delete element from list
        del heap_list[index]
        # adjust only one element which will O(logN)
        if index < len(heap_list):
            _siftup(heap_list, index)
            _siftdown(heap_list, 0, index)

    # Maximize Capital
    def find_maximum_capital(self, capital, profits, number_of_projects, initial_capital):
        for i in range(len(profits)):
            heappush(self.min_heaps, (capital[i], i))

        for _ in range(number_of_projects):
            while self.min_heaps and self.min_heaps[0][0] <= initial_capital:
                capital, i = heappop(self.min_heaps)
                heappush(self.max_heaps, -profits[i])

            initial_capital += -heappop(self.max_heaps)

        return initial_capital


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
    left = []
    while root:
        node = root.data
        if root.left:
            root = root.left
        elif root.right:
            root = root.right
        else:
            break
        left.append(str(node.data))
    return "".join(left)


if __name__ == "__main__":
    tree1 = BSTNode(100)
    tree1.left = BSTNode(50)
    tree1.left.left = BSTNode(25)
    tree1.left.right = BSTNode(75)
    tree1.right = BSTNode(200)
    tree1.right.left = BSTNode(150)
    tree1.right.right = BSTNode(350)
    prev = None

    # tree2 = BSTNode(100)
    # tree2.left = BSTNode(50)
    # tree2.left.left = BSTNode(25)
    # tree2.left.right = BSTNode(70)
    # tree2.right = BSTNode(200)
    # tree2.right.left = BSTNode(150)
    # tree2.right.right = BSTNode(350)

    print(BinarySearchTree().bst(tree1))
