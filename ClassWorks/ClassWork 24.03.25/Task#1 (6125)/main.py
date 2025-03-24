class Queue:
    def __init__(self, maxsize=100):
        self._items = [None for _ in range(maxsize)]
        self._maxsize = maxsize
        self._front = 0  # Початок
        self._back = 0  # Кінець
        self._size = 0  # Поточний розмір

    def push(self, item: int):
        if self._size < self._maxsize:
            self._items[self._back] = item
            self._back = (self._back + 1) % self._maxsize  # Перехід по колу
            self._size += 1
            return "ok"

    def pop(self):
        if self._size > 0:
            item = self._items[self._front]  # Беремо елемент із початку
            self._front = (self._front + 1) % self._maxsize  # front
            self._size -= 1
            return item

    def front(self):
        if self._size > 0:
            return self._items[self._front]  # Повертаємо перший елемент

    def size(self):
        return self._size  # Повертаємо поточну кількість елементів

    def clear(self):
        self._front = 0
        self._back = 0
        self._size = 0
        return "ok"

    def exit(self):
        return "bye"


if __name__ == "__main__":
    queue = Queue()
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
