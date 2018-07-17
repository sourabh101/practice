import random


class Node:
    def __init__(self, value=None):
        self.value = value
        self.left_child = None
        self.right_child = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value, node):
        if value < node.value:
            if node.left_child is None:
                node.left_child = Node(value)
            else:
                self._insert(value, node.left_child)
        else:
            if node.right_child is None:
                node.right_child = Node(value)
            else:
                self._insert(value, node.right_child)

    def print_inorder(self):
        if self.root is not None:
            self._print_inorder(self.root)

    def _print_inorder(self, node):
        if node is not None:
            self._print_inorder(node.left_child)
            print(node.value)
            self._print_inorder(node.right_child)

    def print_preorder(self):
        if self.root is not None:
            self._print_preorder(self.root)

    def _print_preorder(self, node):
        if node is not None:
            print(node.value)
            self._print_preorder(node.left_child)
            self._print_preorder(node.right_child)

    def get_height(self):
        if self.root is not None:
            return self._get_height(self.root)
        else:
            return 0

    def _get_height(self, node):
        if node is None:
            return 0
        else:
            left_height = self._get_height(node.left_child)
            right_height = self._get_height(node.right_child)
            return max(left_height, right_height) + 1

    def search(self, value):
        if self.root is None:
            return False
        else:
            return self._search(self.root, value)

    def _search(self, node, value):
        if node is not None:
            if node.value == value:
                return True
            else:
                if value < node.value:
                    return self._search(node.left_child, value)
                else:
                    return self._search(node.right_child, value)
        else:
            return False


array = [i for i in range(0, 10000)]
random.shuffle(array)

bst = BST()

for i in array:
    bst.insert(i)
