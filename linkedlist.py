import random


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = Node()

    def append(self, data):
        new_node = Node(data)
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = new_node

    def length(self):
        cur = self.head
        count = 0
        while cur.next is not None:
            cur = cur.next
            count += 1
        return count

    def display(self):
        cur = self.head
        elements = []
        while cur.next is not None:
            cur = cur.next
            elements.append(cur.data)
        print(elements)

    def get(self, index):
        if index >= self.length():
            print("Index out of range")
            return None
        cur = self.head
        count = 0
        while True:
            cur = cur.next
            if index == count:
                return cur.data
            count += 1

    def erase(self, index):
        if index >= self.length():
            print("Index out of range")
            return None

        current = self.head
        cur_idx = 0
        while True:
            last_node = current
            current = current.next
            if cur_idx == index:
                last_node.next = current.next
                return
            cur_idx += 1


array = [i for i in range(0, 10)]
random.shuffle(array)

my_list = LinkedList()

for i in array:
    my_list.append(i)

my_list.display()
my_list.erase(5)
my_list.display()
