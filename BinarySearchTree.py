import random
import sys


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
        elif value > node.value:
            if node.right_child is None:
                node.right_child = Node(value)
            else:
                self._insert(value, node.right_child)

    def print_in_order(self):
        if self.root is not None:
            self._print_in_order(self.root)

    def _print_in_order(self, node):
        if node is not None:
            self._print_in_order(node.left_child)
            print(node.value)
            self._print_in_order(node.right_child)

    def print_pre_order(self):
        if self.root is not None:
            self._print_pre_order(self.root)

    def _print_pre_order(self, node):
        if node is not None:
            print(node.value)
            self._print_pre_order(node.left_child)
            self._print_pre_order(node.right_child)

    def get_height(self):
        if self.root is not None:
            return self._get_height(self.root)
        else:
            return 0

    def _get_height(self, node):
        if node is None:
            return -1
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

    def is_bst(self, node, minimum=-sys.maxsize, maximum=sys.maxsize):
        if node is None:
            return True
        if minimum < node.value < maximum and self.is_bst(node.left_child, minimum, node.value) and\
                self.is_bst(node.right_child, node.value, maximum):
            return True

    def bfs(self):
        node_queue = []
        root = self.root
        if root is not None:
            node_queue.insert(0, root)
            print(root.value)
            while len(node_queue) != 0:
                node = node_queue.pop()
                left_node = node.left_child
                right_node = node.right_child
                if left_node is not None:
                    node_queue.insert(0, left_node)
                    print(left_node.value)
                if right_node is not None:
                    node_queue.insert(0, right_node)
                    print(right_node.value)


array = [i for i in range(0, 1000)]
random.shuffle(array)

bst = BST()

for i in array:
    bst.insert(i)

bst.bfs()
