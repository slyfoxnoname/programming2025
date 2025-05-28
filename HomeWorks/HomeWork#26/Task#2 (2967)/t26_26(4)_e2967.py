import math
import heapq

n = int(input())
cities = [tuple(map(int, input().split())) for _ in range(n)]

visited = [False] * n
min_edge = [float('inf')] * n
min_edge[0] = 0

pq = [(0, 0)]  # (distance, city index)
total = 0.0

while pq:
    cost, u = heapq.heappop(pq)
    if visited[u]:
        continue
    visited[u] = True
    total += cost

    for v in range(n):
        if not visited[v]:
            dist = math.hypot(cities[u][0] - cities[v][0], cities[u][1] - cities[v][1])
            if dist < min_edge[v]:
                min_edge[v] = dist
                heapq.heappush(pq, (dist, v))

print(f"{total:.10f}")
