class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert_path(node, path, index, low, high):
    if index == len(path):
        return True

    val = path[index]
    if val <= low or val >= high:
        return False

    if val < node.value:
        node.left = Node(val)
        return insert_path(node.left, path, index + 1, low, node.value)
    else:
        node.right = Node(val)
        return insert_path(node.right, path, index + 1, node.value, high)

def is_bst_path(path):
    if not path:
        return "NO"
    root = Node(path[0])
    if insert_path(root, path, 1, float('-inf'), float('inf')):
        return "YES"
    else:
        return "NO"

# Зчитування вхідних даних
import sys
data = list(map(int, sys.stdin.read().split()))
print(is_bst_path(data))