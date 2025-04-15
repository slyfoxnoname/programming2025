class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.head = None

    def Insert(self, val):
        if self.head is None:
            self.head = TreeNode(val)
        else:
            self._insert_recursive(self.head, val)

    def _insert_recursive(self, node, val):
        if val < node.val:
            if node.left is None:
                node.left = TreeNode(val)
            else:
                self._insert_recursive(node.left, val)
        else:  # val >= node.val goes to the right subtree
            if node.right is None:
                node.right = TreeNode(val)
            else:
                self._insert_recursive(node.right, val)

    def IsSameTree(self, other_tree):
        return 1 if self._is_same(self.head, other_tree.head) else 0

    def _is_same(self, node1, node2):
        if not node1 and not node2:
            return True
        if not node1 or not node2:
            return False
        if node1.val != node2.val:
            return False
        return self._is_same(node1.left, node2.left) and self._is_same(node1.right, node2.right)

# Зчитуємо дані
n = int(input())  # кількість елементів у першому масиві
arr1 = list(map(int, input().split()))  # перший масив

m = int(input())  # кількість елементів у другому масиві
arr2 = list(map(int, input().split()))  # другий масив

# Створення двох дерев
tree1 = Tree()
tree2 = Tree()

# Вставляємо елементи в дерева
for val in arr1:
    tree1.Insert(val)

for val in arr2:
    tree2.Insert(val)

# Перевірка, чи дерева однакові
print(tree1.IsSameTree(tree2))