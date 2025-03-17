class Node:
    def __init__(self, item):
        self.item = item
        self.next = None  # Указатель на следующий элемент


class Stack:
    def __init__(self):
        self._top = None  # Верхний элемент
        self._size = 0  # Размер стека

    def push(self, item):
        node = Node(item)  # Создаём новый узел
        node.next = self._top  # Новый узел указывает на старый верхний
        self._top = node  # Новый узел становится верхним
        self._size += 1
        return "ok"

    def pop(self):
        if self.empty():  # Если стек пуст
            return "error"
        item = self._top.item  # Запоминаем удаляемый элемент
        self._top = self._top.next  # Смещаем верхний указатель
        self._size -= 1
        return item

    def empty(self):
        return self._top is None

    def back(self):
        if self.empty():
            return "error"
        return self._top.item

    def size(self):
        return self._size

    def clear(self):
        self._top = None  # Удаляем все элементы
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
            break  # Обрабатываем неожиданный конец ввода
