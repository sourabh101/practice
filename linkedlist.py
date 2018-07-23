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

    def middle_element(self):
        element_list = []
        current_node = self.head
        while current_node is not None:
            current_node = current_node.next
            if current_node is not None:
                element_list.append(current_node.data)

        return element_list[len(element_list)//2]

    def reverse(self):
        head = self.head
        if head is None or head.next is None:
            return head
        prev_node = head.next
        cur_node = prev_node.next
        next_node = cur_node.next
        prev_node.next = None
        cur_node.next = prev_node
        while next_node is not None:
            prev_node = cur_node
            cur_node = next_node
            next_node = next_node.next
            cur_node.next = prev_node

        head.next = cur_node
        return head

    def rotate(self, num):
        length = self.length()
        if length < 2:
            return
        if num > length:
            num = num % length
        head = self.head
        cur_node = head.next
        count = 0
        while cur_node is not None:
            count += 1
            if count == num:
                temp_node = head.next
                head.next = cur_node.next
                cur_node.next = None
                node = head.next
                while node.next is not None:
                    node = node.next
                node.next = temp_node
            else:
                cur_node = cur_node.next

        return head

    def contains_loop(self):
        fast = self.head
        slow = self.head

        while fast is not None:
            fast = fast.next
            if fast is not None:
                fast = fast.next
            slow = slow.next
            if fast == slow:
                return True
        return False

    def remove_loop(self):
        head = self.head
        fast = head
        slow = head
        match_node = head
        while fast is not None:
            fast = fast.next
            if fast is not None:
                fast = fast.next
            slow = slow.next
            if fast == slow:
                match_node = fast
                break

        if match_node != head:
            new_node = head
            temp_node = match_node

            while new_node is not None:
                new_node = new_node.next
                while temp_node.next != match_node:
                    if temp_node.next == new_node:
                        temp_node.next = None
                        return head
                    temp_node = temp_node.next

                temp_node = match_node


def main():
    array = [i for i in range(1, 11)]
    random.shuffle(array)
    my_list = LinkedList()

    for i in array:
        my_list.append(i)
    my_list.display()


if __name__ == '__main__':
    main()
