class MyDeque:
    def __init__(self, maxsize = 100):
        self._items = [None for _ in range(maxsize)]  # Використовуємо список для зберігання елементів

    def push_front(self, x):
        self._items.insert(0, x)  # Додаємо елемент на початок
        return "ok"

    def push_back(self, x):
        self._items.append(x)  # Додаємо елемент у кінець
        return "ok"

    def pop_front(self):
        return self._items.pop(0)  # Видаляємо та повертаємо перший елемент

    def pop_back(self):
        return self._items.pop()  # Видаляємо та повертаємо останній елемент

    def front(self):
        return self._items[0]  # Повертаємо перший елемент без видалення

    def back(self):
        return self._items[-1]  # Повертаємо останній елемент без видалення

    def size(self):
        return len(self._items)  # Повертаємо кількість елементів у деку

    def clear(self):
        self._items = []  # Очищаємо список
        return "ok"

    def exit(self):
        return "bye"


if __name__ == "__main__":
    deque = MyDeque()
    while True:
        command = input().strip().split()
        if command[0] == "push_front":
            print(deque.push_front(int(command[1])))
        elif command[0] == "push_back":
            print(deque.push_back(int(command[1])))
        elif command[0] == "pop_front":
            print(deque.pop_front())
        elif command[0] == "pop_back":
            print(deque.pop_back())
        elif command[0] == "front":
            print(deque.front())
        elif command[0] == "back":
            print(deque.back())
        elif command[0] == "size":
            print(deque.size())
        elif command[0] == "clear":
            print(deque.clear())
        elif command[0] == "exit":
            print(deque.exit())
            break
