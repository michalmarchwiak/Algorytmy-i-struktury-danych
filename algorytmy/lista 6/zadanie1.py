class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, node, key):
        if key <= node.key:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert_recursive(node.left, key)
        else:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert_recursive(node.right, key)

    def display(self):
        self._display_recursive(self.root)
        print()

    def _display_recursive(self, node):
        if node is not None:
            self._display_recursive(node.left)
            print(node.key, end=' ')
            self._display_recursive(node.right)

    def to_list(self):
        if not self.root:
            return []

        height = self._find_height(self.root)
        size = 2**(height + 1) - 1
        tree_list = [None] * size

        self._fill_list(self.root, tree_list, 0)
        return tree_list

    def _find_height(self, node):
        if not node:
            return -1
        return 1 + max(self._find_height(node.left), self._find_height(node.right))

    def _fill_list(self, node, tree_list, index):
        if node is not None:
            tree_list[index] = node.key
            self._fill_list(node.left, tree_list, 2 * index + 1)
            self._fill_list(node.right, tree_list, 2 * index + 2)

bst = BinarySearchTree()
for key in [30, 40, 24, 58, 48, 26, 11, 13]:
    bst.insert(key)

tree_list = bst.to_list()
print(tree_list)