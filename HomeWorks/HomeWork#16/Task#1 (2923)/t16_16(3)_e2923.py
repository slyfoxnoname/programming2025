class Node:
    def __init__(self, color):
        self.color = color
        self.children = []

n = int(input())
nodes = [None] * n
parents = [0] * n
colors = [0] * n
root = -1

# 1. Зчитуємо всіх батьків і кольори
for i in range(n):
    p, c = map(int, input().split())
    parents[i] = p
    colors[i] = c
    if p == 0:
        root = i

# 2. Створюємо всі вузли
for i in range(n):
    nodes[i] = Node(colors[i])

# 3. Будуємо дерево
for i in range(n):
    if parents[i] != 0:
        nodes[parents[i] - 1].children.append(nodes[i])

result = [0] * n

# 4. dfs з поверненням множини кольорів
def dfs(node, index_map):
    color_set = {node.color}
    for child in node.children:
        child_index = index_map[child]
        child_colors = dfs(child, index_map)
        if len(child_colors) > len(color_set):
            color_set, child_colors = child_colors, color_set
        color_set.update(child_colors)
    result[index_map[node]] = len(color_set)
    return color_set

index_map = {nodes[i]: i for i in range(n)}

dfs(nodes[root], index_map)
print(*result)
