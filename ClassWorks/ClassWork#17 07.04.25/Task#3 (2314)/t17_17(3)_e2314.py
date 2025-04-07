class SearchTree:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def insert(self, key):
        if key < self.key:
            if self.left is None:
                self.left = SearchTree(key)
            else:
                self.left.insert(key)
        elif key > self.key:
            if self.right is None:
                self.right = SearchTree(key)
            else:
                self.right.insert(key)
        # Якщо key == self.key, нічого не робимо (повторів не додаємо)

    def find_second_largest(self):
        parent = None
        node = self

        # Знаходимо найбільший вузол
        while node.right:
            parent = node
            node = node.right

        # Випадок 1: найбільший вузол має ліве піддерево
        if node.left:
            node = node.left
            while node.right:
                node = node.right
            return node.key

        # Випадок 2: найбільший вузол — правий крайній, але без лівого піддерева
        if parent:
            return parent.key

        return None  # якщо чомусь не знайдено (хоча гарантується, що знайдеться)


if __name__ == "__main__":
    lst = [int(x) for x in input().split()]
    if lst[0] != 0:
        tree = SearchTree(lst[0])
        for num in lst[1:]:
            if num == 0:
                break
            tree.insert(num)
        print(tree.find_second_largest())
