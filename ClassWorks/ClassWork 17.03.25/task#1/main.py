class Stack:
    def __init__(self, maxsize=100):
        self._items = [0] * maxsize
        self._top = -1
        self._size = 0

    def push(self, item):
        if self._size < len(self._items):
            self._top += 1
            self._items[self._top] = item
            self._size += 1
            return "ok"
        return "error"

    def pop(self):
        if self._size > 0:
            item = self._items[self._top]
            self._top -= 1
            self._size -= 1
            return item
        return "error"

    def size(self):
        return self._size

    def back(self):
        if self._size > 0:
            return self._items[self._top]
        return "error"

    def clear(self):
        self._top = -1
        self._size = 0
        return "ok"

    def execute(self, command):
        parts = command.strip().split()
        method = parts[0]

        if method == "push":
            return self.push(int(parts[1]))
        elif method in {"pop", "size", "back", "clear"}:
            return getattr(self, method)()
        elif method == "exit":
            return "bye"
        return "unknown command"


if __name__ == '__main__':
    stack = Stack()

    while True:
        try:
            command = input().strip()
            result = stack.execute(command)
            print(result)
            if result == "bye":
                break
        except EOFError:
            break  # Для случая, если ввод закончится неожиданно
