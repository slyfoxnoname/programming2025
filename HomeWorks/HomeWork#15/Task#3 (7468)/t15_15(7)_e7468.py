class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_tail(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def reorder_list(self):
        if not self.head or not self.head.next:
            return

        # 1. Разделить список на две половины
        slow, fast = self.head, self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Разделяем список
        second_half = slow.next
        slow.next = None
        second_half = self.reverse_list(second_half)

        # 2. Перегруппировать элементы
        first_half = self.head
        while second_half:
            tmp1 = first_half.next
            tmp2 = second_half.next

            first_half.next = second_half
            second_half.next = tmp1

            first_half = tmp1
            second_half = tmp2

    def reverse_list(self, head):
        prev, current = None, head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=' ')
            current = current.next
        print()

if __name__ == "__main__":
    n = int(input())
    values = list(map(int, input().split()))
    linked_list = LinkedList()

    for val in values:
        linked_list.add_to_tail(val)

    linked_list.reorder_list()
    linked_list.print_list()
