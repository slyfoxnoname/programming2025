import math

EMPTY = None


def is_prime(n: int):
    """Проверяет, является ли число простым"""
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


class Dict:
    M = 31

    def __init__(self, size=11):
        self._size = size
        self._count = 0
        self._keys: list[str | None] = [EMPTY] * size
        self._values: list[list[str] | None] = [EMPTY] * size

    def _rehash(self):
        """Увеличивает размер таблицы и перехеширует элементы"""
        self._size = self._size * 2 + 1
        while not is_prime(self._size):
            self._size += 2

        old_keys = self._keys
        old_values = self._values
        self.__init__(self._size)  # Создаем новую таблицу

        for i in range(len(old_keys)):
            if old_keys[i] is not EMPTY:
                self.set(old_keys[i], old_values[i])

    def hash(self, s):
        """Хеш-функция на основе полиномиального хеширования"""
        h = 0
        for char in s:
            h = h * self.M + ord(char)
        return h % self._size

    def set(self, key: str, value):
        """Добавляет ключ-значение в хеш-таблицу"""
        if self._count / self._size > 0.7:  # Если заполнено > 70%, увеличиваем размер
            self._rehash()

        i = self.hash(key)
        while self._keys[i] is not EMPTY:
            if self._keys[i] == key:
                self._values[i] = value  # Обновление значения
                return
            i = (i + 1) % self._size  # Линейное пробирование

        self._keys[i] = key
        self._values[i] = value
        self._count += 1

    def get(self, key: str):
        """Возвращает значение по ключу или None, если ключ отсутствует"""
        i = self.hash(key)
        while self._keys[i] is not EMPTY:
            if self._keys[i] == key:
                return self._values[i]
            i = (i + 1) % self._size  # Линейное пробирование
        return None

    def keys(self):
        """Возвращает список всех ключей"""
        return [key for key in self._keys if key is not EMPTY]

    def __setitem__(self, key, value):
        self.set(key, value)

    def __getitem__(self, key):
        value = self.get(key)
        if value is None:
            raise KeyError(f"Key '{key}' not found")
        return value

    def __contains__(self, key):
        return self.get(key) is not None


if __name__ == '__main__':
    with open("input.txt") as f:
        dct = Dict()

        for line in f:
            eng, latins = line.strip().split(" - ")
            latins = latins.split(", ")
            for latin in latins:
                if latin in dct:
                    dct[latin].append(eng)
                else:
                    dct[latin] = [eng]

    latins = sorted(dct.keys())
    print(len(latins))
    for latin in latins:
        print(latin, end=" - ")
        print(*sorted(dct[latin]), sep=", ")
