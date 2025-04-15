class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def insert_bst(root, val):
    if root is None:
        return TreeNode(val)
    if val < root.val:
        root.left = insert_bst(root.left, val)
    else:
        root.right = insert_bst(root.right, val)
    return root


def preorder_traversal(node):
    if node is None:
        return ''
    return node.val + preorder_traversal(node.left) + preorder_traversal(node.right)


def restore_tree(lines):
    # Створення дерева із зворотного порядку
    nodes = []
    for line in reversed(lines):
        for ch in line.strip():
            nodes.append(ch)

    root = None
    for node in nodes:
        root = insert_bst(root, node)

    return preorder_traversal(root)


# Читання даних
lines = []
while True:
    line = input().strip()
    if line == '*':
        break
    lines.append(line)

# Виведення результату
print(restore_tree(lines))
