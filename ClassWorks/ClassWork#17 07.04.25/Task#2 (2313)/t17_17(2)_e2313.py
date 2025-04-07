class SearchTree:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def insert(self, key):
        node = self
        while True:
            if key < node.key:
                if node.left is None:
                    node.left = SearchTree(key)
                    break
                node = node.left
            elif key > node.key:
                if node.right is None:
                    node.right = SearchTree(key)
                    break
                node = node.right
            else:
                break  # ключ вже існує

    def size(self):
        count = 0
        stack = [self]
        while stack:
            node = stack.pop()
            if node:
                count += 1
                stack.append(node.left)
                stack.append(node.right)

        return count


if __name__ == '__main__':
    lst = list(map(int, input().split()))
    if lst and lst[0] != 0:
        tree = SearchTree(lst[0])
        for key in lst[1:]:
            if key == 0:
                break
            tree.insert(key)
        print(tree.size())
    else:
        print(0)
