from helpers import BinarySearchTreeNode


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def pre_order(self, root):
        if root:
            print(root.data, end=" ")
            self.pre_order(root.left)
            self.pre_order(root.right)

    def post_order(self, root):
        if root:
            self.post_order(root.left)
            self.post_order(root.right)
            print(root.info, end=" ")

    def in_order(self, root):
        if root:
            self.in_order(root.left)
            print(root.info, end=" ")
            self.in_order(root.right)

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
            print(nodes[0].info, end=" ")
            node = nodes.pop(0)

            if node.left:
                nodes.append(node.left)
            if node.right:
                nodes.append(node.right)

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
