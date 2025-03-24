class QueueNode:
    def __init__(self, value, next_node=None):
        self.value = value  # Значення вузла
        self.next = next_node  # Посилання на наступний вузол

class RecursiveQueue:
    def __init__(self):
        self.front_node = None  # Початок черги
        self.rear_node = None  # Кінець черги
        self._size = 0  # Поточний розмір черги

    def push(self, value):
        new_node = QueueNode(value)
        if self.rear_node:
            self.rear_node.next = new_node  # Додаємо елемент у кінець
        self.rear_node = new_node
        if not self.front_node:
            self.front_node = new_node  # Якщо черга була порожня, оновлюємо front
        self._size += 1
        return "ok"

    def pop(self):
        if self.front_node is None:
            return "error"
        value = self.front_node.value
        self.front_node = self.front_node.next  # Пересуваємо front вперед
        if self.front_node is None:
            self.rear_node = None  # Якщо черга стала порожньою, обнуляємо rear
        self._size -= 1
        return value

    def front(self):
        return self.front_node.value if self.front_node else "error"

    def size(self):
        return self._size

    def clear(self):
        self.front_node = None
        self.rear_node = None
        self._size = 0
        return "ok"

    def exit(self):
        return "bye"


if __name__ == "__main__":
    queue = RecursiveQueue()
    while True:
        command = input().strip().split()
        if command[0] == "push":
            print(queue.push(int(command[1])))
        elif command[0] == "pop":
            print(queue.pop())
        elif command[0] == "front":
            print(queue.front())
        elif command[0] == "size":
            print(queue.size())
        elif command[0] == "clear":
            print(queue.clear())
        elif command[0] == "exit":
            print(queue.exit())
            break
