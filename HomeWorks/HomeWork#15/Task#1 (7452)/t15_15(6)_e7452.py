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

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=' ')
            current = current.next
        print()

    def print_reverse(self):
        def reverse_helper(node):
            if not node:
                return
            reverse_helper(node.next)
            print(node.data, end=' ')

        reverse_helper(self.head)
        print()


if __name__ == "__main__":
    n = int(input())  # Читаем количество элементов
    values = map(int, input().split())  # Читаем значения элементов
    linked_list = LinkedList()

    for val in values:
        linked_list.add_to_tail(val)  # Добавляем элементы в конец списка

    linked_list.print_list()  # Выводим элементы списка в прямом порядке
    linked_list.print_reverse()  # Выводим элементы списка в обратном порядке
