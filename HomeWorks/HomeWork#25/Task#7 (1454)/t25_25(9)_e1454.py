import sys
input = sys.stdin.readline

n, m = map(int, input().split())
edges = []
for _ in range(m):
    u, v, w = map(int, input().split())
    edges.append((u, v, w))

dist = [-float('inf')] * (n + 1)
dist[1] = 0

# Беллман-Форд (максимізація)
for i in range(n - 1):
    updated = False
    for u, v, w in edges:
        if dist[u] != -float('inf') and dist[u] + w > dist[v]:
            dist[v] = dist[u] + w
            updated = True
    if not updated:
        break

# Знаходимо вершини, де можна ще покращити dist (наявність позитивного циклу)
affected = [False] * (n + 1)
for u, v, w in edges:
    if dist[u] != -float('inf') and dist[u] + w > dist[v]:
        affected[v] = True

# Визначимо всі вершини, які доступні з цих "affected"
# Для цього будуємо граф для обходу
graph = [[] for _ in range(n + 1)]
for u, v, w in edges:
    graph[u].append(v)

from collections import deque

queue = deque([i for i in range(1, n+1) if affected[i]])
visited = [False] * (n + 1)
for i in queue:
    visited[i] = True

while queue:
    u = queue.popleft()
    for w_ in graph[u]:
        if not visited[w_]:
            visited[w_] = True
            queue.append(w_)

if visited[n]:
    print(":)")
elif dist[n] == -float('inf'):
    print(":(")
else:
    print(dist[n])
