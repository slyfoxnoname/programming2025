class Directory:
    def __init__(self, name):
        self.name = name
        self.children = {}

    def add_path(self, parts):
        if not parts:
            return
        head, *tail = parts
        if head not in self.children:
            self.children[head] = Directory(head)
        self.children[head].add_path(tail)

    def print_tree(self, depth=0):
        print(' ' * depth + self.name)
        for child in sorted(self.children.values(), key=lambda d: d.name):
            child.print_tree(depth + 1)


def main():
    n = int(input())
    root = Directory(None)

    for _ in range(n):
        path = input().strip().split('\\')
        root.add_path(path)

    # Виводимо тільки дітей кореня без початкового відступу
    for child in sorted(root.children.values(), key=lambda d: d.name):
        child.print_tree(0)


if __name__ == "__main__":
    main()
