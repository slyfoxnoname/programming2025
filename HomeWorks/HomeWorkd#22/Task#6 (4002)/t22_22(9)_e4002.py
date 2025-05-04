from collections import deque

def is_bipartite(n, edges):
    graph = [[] for _ in range(n + 1)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    color = [0] * (n + 1)  # 0 - не відвідано, 1 і 2 - кольори

    for start in range(1, n + 1):
        if color[start] == 0:
            queue = deque([start])
            color[start] = 1
            while queue:
                u = queue.popleft()
                for v in graph[u]:
                    if color[v] == 0:
                        color[v] = 3 - color[u]  # чергуємо 1 і 2
                        queue.append(v)
                    elif color[v] == color[u]:
                        return False
    return True

# Зчитування з input.txt
with open('input.txt', 'r') as f:
    lines = f.read().splitlines()
    n, m = map(int, lines[0].split())
    edges = [tuple(map(int, line.split())) for line in lines[1:]]

if is_bipartite(n, edges):
    print("YES")
else:
    print("NO")
