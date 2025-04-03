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

    def rotate_right(self, k):
        if not self.head or k == 0:
            return

        # Find the length of the list
        length = 1
        current = self.head
        while current.next:
            current = current.next
            length += 1

        # If k is greater than the length, reduce it
        k %= length
        if k == 0:
            return

        # Find the new tail (length - k - 1)
        current = self.head
        for _ in range(length - k - 1):
            current = current.next

        # Set the new head and tail
        new_head = current.next
        current.next = None
        self.tail.next = self.head
        self.head = new_head
        self.tail = current

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=' ')
            current = current.next
        print()

if __name__ == "__main__":
    n = int(input())  # Read number of elements
    values = list(map(int, input().split()))  # Read the values for the list
    linked_list = LinkedList()

    for val in values:
        linked_list.add_to_tail(val)  # Add each value to the list

    k_values = []
    while True:
        try:
            k = int(input())  # Read k values for rotations
            k_values.append(k)
        except EOFError:
            break

    for k in k_values:
        linked_list.rotate_right(k)  # Rotate the list
        linked_list.print_list()  # Print the rotated list
