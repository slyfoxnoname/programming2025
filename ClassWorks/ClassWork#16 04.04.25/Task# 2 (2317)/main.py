class TreeNode:
    def __init__(self, key, parent=None, depth=0):
        self.key = key
        self.parent = parent
        self.depth = depth

class TreeManager:
    def __init__(self):
        root = TreeNode(1)
        self.nodes = {1: root}

    def add(self, parent_key, child_key):
        parent = self.nodes[parent_key]
        new_node = TreeNode(child_key, parent, parent.depth + 1)
        self.nodes[child_key] = new_node

    def lca(self, a, b):
        node_a = self.nodes[a]
        node_b = self.nodes[b]

        # Вирівнюємо глибини
        while node_a.depth > node_b.depth:
            node_a = node_a.parent
        while node_b.depth > node_a.depth:
            node_b = node_b.parent

        # Піднімаємось одночасно
        while node_a != node_b:
            node_a = node_a.parent
            node_b = node_b.parent

        return node_a.key

if __name__ == '__main__':
    import sys
    input = sys.stdin.read
    data = input().splitlines()

    k = int(data[0])
    tree = TreeManager()
    for line in data[1:]:
        if not line.strip():
            continue
        cmd, a, b = line.split()
        a, b = int(a), int(b)
        if cmd == 'ADD':
            tree.add(a, b)
        elif cmd == 'GET':
            print(tree.lca(a, b))
