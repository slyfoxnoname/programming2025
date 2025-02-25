class HashTable:
    def __init__(self, size=1000):
        self.size = size
        self.table = [None] * size

    def _hash(self, key, attempt=0):
        return (hash(key) + attempt) % self.size

    def insert(self, key, value):
        attempt = 0
        while attempt < self.size:
            idx = self._hash(key, attempt)
            if self.table[idx] is None or self.table[idx][0] == key:
                self.table[idx] = (key, value)
                return
            attempt += 1
        raise Exception("HashTable is full")

    def get(self, key):
        attempt = 0
        while attempt < self.size:
            idx = self._hash(key, attempt)
            if self.table[idx] is None:
                return None
            if self.table[idx][0] == key:
                return self.table[idx][1]
            attempt += 1
        return None

    def delete(self, key):
        attempt = 0
        while attempt < self.size:
            idx = self._hash(key, attempt)
            if self.table[idx] is None:
                return
            if self.table[idx][0] == key:
                self.table[idx] = None
                return
            attempt += 1


library = HashTable()


def init():
    global library
    library = HashTable()


def addBook(author, title):
    books = library.get(author) or []
    if title not in books:
        books.append(title)
        books.sort()
    library.insert(author, books)


def find(author, title):
    books = library.get(author)
    return title in books if books else False


def delete(author, title):
    books = library.get(author)
    if books and title in books:
        books.remove(title)
        if books:
            library.insert(author, books)
        else:
            library.delete(author)


def findByAuthor(author):
    return sorted(library.get(author) or [])
