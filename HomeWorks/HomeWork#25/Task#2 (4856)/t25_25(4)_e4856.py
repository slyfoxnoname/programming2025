import heapq

n, m = map(int, input().split())
s, f = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))  # неорієнтований граф

dist = [float('inf')] * (n + 1)
prev = [-1] * (n + 1)
dist[s] = 0

pq = [(0, s)]  # (відстань, вершина)

while pq:
    d, u = heapq.heappop(pq)
    if d > dist[u]:
        continue
    for v, w in graph[u]:
        if dist[u] + w < dist[v]:
            dist[v] = dist[u] + w
            prev[v] = u
            heapq.heappush(pq, (dist[v], v))

if dist[f] == float('inf'):
    print(-1)
else:
    print(dist[f])
    path = []
    cur = f
    while cur != -1:
        path.append(cur)
        cur = prev[cur]
    print(*reversed(path))
