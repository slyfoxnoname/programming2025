class Library:
    def __init__(self, size=1000):
        self.size = size
        self.table = [None] * size
        self.occupied = 0

    def _hash(self, author, title):
        return (hash(author) + hash(title)) % self.size

    def _probe(self, index):
        return (index + 1) % self.size

    def addBook(self, author, title):
        if self.occupied >= self.size:
            raise Exception("Library is full")

        index = self._hash(author, title)

        while self.table[index] is not None and self.table[index] != "DELETED":
            if self.table[index] == (author, title):
                return  # Book already in library
            index = self._probe(index)

        self.table[index] = (author, title)
        self.occupied += 1

    def find(self, author, title):
        index = self._hash(author, title)

        for _ in range(self.size):
            if self.table[index] is None:
                return False
            if self.table[index] == (author, title):
                return True
            index = self._probe(index)

        return False

    def delete(self, author, title):
        index = self._hash(author, title)

        for _ in range(self.size):
            if self.table[index] is None:
                return
            if self.table[index] == (author, title):
                self.table[index] = "DELETED"
                self.occupied -= 1
                return
            index = self._probe(index)

    def findByAuthor(self, author):
        books = []
        for entry in self.table:
            if entry is not None and entry != "DELETED" and entry[0] == author:
                books.append(entry[1])
        return sorted(books)


table = None


def init():
    global table
    table = Library()


def addBook(author, title):
    table.addBook(author, title)


def find(author, title):
    return table.find(author, title)


def delete(author, title):
    table.delete(author, title)


def findByAuthor(author):
    return table.findByAuthor(author)
