from helper import BinarySearchTreeNode


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
        queue = [root]
        while len(queue) > 0:
            print(queue[0].info, end=" ")
            node = queue.pop(0)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    def top_view(self, root):
        level = [(root, 0)]
        viewable = {}

        while level:
            node, score = level.pop(0)
            if score not in viewable:
                viewable[score] = node.info
            if node.left:
                level.append((node.left, score - 1))
            if node.right:
                level.append((node.right, score + 1))

        for data in sorted(viewable):
            print(viewable[data], end=" ")

    def insert(self, val):
        new_node = BinarySearchTreeNode(val)
        if not self.root:
            self.root = new_node
            return self.root
        curr = self.root
        while curr:
            if curr.info > val:
                if curr.left:
                    curr = curr.left
                else:
                    curr.left = new_node
                    break
            else:
                if curr.right:
                    curr = curr.right
                else:
                    curr.right = new_node
                    break
        # [for recursion]
        # if not self.root:
        #     self.root = BinarySearchTreeNode(val)
        # else:
        #     self.insertion(self.root, val)

        return self.root

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
            # print(node)
            if max(v1, v2) < node.info:
                node = node.left
            elif min(v1, v2) > node.info:
                node = node.right
            else:
                break

        return node
