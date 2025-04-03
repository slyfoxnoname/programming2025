class QueueNode:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node


class RecursiveQueue:
    def __init__(self):
        self.front_node = None
        self.rear_node = None
        self.count = 0

    def push(self, n):
        new_node = QueueNode(n)
        if self.rear_node:
            self.rear_node.next = new_node
        self.rear_node = new_node
        if not self.front_node:
            self.front_node = new_node
        self.count += 1
        print("ok")

    def pop(self):
        if not self.front_node:
            print("error")
            return
        value = self.front_node.value
        self.front_node = self.front_node.next
        if not self.front_node:
            self.rear_node = None
        self.count -= 1
        print(value)

    def front(self):
        if not self.front_node:
            print("error")
            return
        print(self.front_node.value)

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
    queue = RecursiveQueue()
    while True:
        command = input().strip().split()
        if command[0] == "push":
            queue.push(int(command[1]))
        elif command[0] == "pop":
            queue.pop()
        elif command[0] == "front":
            queue.front()
        elif command[0] == "size":
            queue.size()
        elif command[0] == "clear":
            queue.clear()
        elif command[0] == "exit":
            queue.exit()


if __name__ == "__main__":
    process_commands()
