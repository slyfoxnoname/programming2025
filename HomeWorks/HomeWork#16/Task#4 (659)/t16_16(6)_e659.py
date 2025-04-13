class Node:
    def __init__(self, is_leaf, value=None):
        self.is_leaf = is_leaf  # чи є вузол листом
        self.value = value      # значення для листа (+1, -1, 0)
        self.children = []      # діти для внутрішнього вузла

    def add_child(self, child):
        self.children.append(child)

    def evaluate(self, depth=0):
        # Якщо це лист, повертаємо його значення
        if self.is_leaf:
            return self.value

        # Якщо це внутрішній вузол, залежно від глибини вибираємо максимальний або мінімальний результат
        if depth % 2 == 0:
            # Хід першого гравця (максимум)
            if self.children:
                return max(child.evaluate(depth + 1) for child in self.children)
            else:
                return 0  # якщо немає дочірніх вузлів, повертаємо нічийний результат
        else:
            # Хід другого гравця (мінімум)
            if self.children:
                return min(child.evaluate(depth + 1) for child in self.children)
            else:
                return 0  # якщо немає дочірніх вузлів, повертаємо нічийний результат


def main():
    n = int(input())  # кількість вузлів
    nodes = [Node(False) for _ in range(n)]  # список вузлів

    for i in range(1, n):
        line = input().split()
        if line[0] == "L":  # лист
            parent = int(line[1]) - 1
            value = int(line[2])
            node = Node(True, value)
            nodes[parent].add_child(node)
        else:  # внутрішній вузол
            parent = int(line[1]) - 1
            node = Node(False)
            nodes[parent].add_child(node)

    # корінь дерева
    root = nodes[0]
    print(root.evaluate())  # вивести результат для кореня


if __name__ == "__main__":
    main()
