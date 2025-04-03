class DequeNode:
    def __init__(self, value, prev_node=None, next_node=None):
        self.value = value
        self.prev = prev_node
        self.next = next_node


class RecursiveDeque:
    def __init__(self):
        self.front_node = None
        self.rear_node = None
        self.count = 0

    def push_front(self, n):
        new_node = DequeNode(n, None, self.front_node)
        if self.front_node:
            self.front_node.prev = new_node
        self.front_node = new_node
        if not self.rear_node:
            self.rear_node = new_node
        self.count += 1
        print("ok")

    def push_back(self, n):
        new_node = DequeNode(n, self.rear_node, None)
        if self.rear_node:
            self.rear_node.next = new_node
        self.rear_node = new_node
        if not self.front_node:
            self.front_node = new_node
        self.count += 1
        print("ok")

    def pop_front(self):
        if not self.front_node:
            print("error")
            return
        value = self.front_node.value
        self.front_node = self.front_node.next
        if self.front_node:
            self.front_node.prev = None
        else:
            self.rear_node = None
        self.count -= 1
        print(value)

    def pop_back(self):
        if not self.rear_node:
            print("error")
            return
        value = self.rear_node.value
        self.rear_node = self.rear_node.prev
        if self.rear_node:
            self.rear_node.next = None
        else:
            self.front_node = None
        self.count -= 1
        print(value)

    def front(self):
        if not self.front_node:
            print("error")
            return
        print(self.front_node.value)

    def back(self):
        if not self.rear_node:
            print("error")
            return
        print(self.rear_node.value)

    def size(self):
        print(self.count)

    def clear(self):
        self.front_node = None
        self.rear_node = None
        self.count = 0
        print("ok")

    def exit(self):
        print("bye")
        exit()


def process_commands():
    deque = RecursiveDeque()
    while True:
        command = input().strip().split()
        if command[0] == "push_front":
            deque.push_front(int(command[1]))
        elif command[0] == "push_back":
            deque.push_back(int(command[1]))
        elif command[0] == "pop_front":
            deque.pop_front()
        elif command[0] == "pop_back":
            deque.pop_back()
        elif command[0] == "front":
            deque.front()
        elif command[0] == "back":
            deque.back()
        elif command[0] == "size":
            deque.size()
        elif command[0] == "clear":
            deque.clear()
        elif command[0] == "exit":
            deque.exit()


if __name__ == "__main__":
    process_commands()
