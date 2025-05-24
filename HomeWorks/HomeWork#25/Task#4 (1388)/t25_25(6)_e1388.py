import sys
import heapq
from collections import defaultdict

# Зчитування всіх чисел з вхідного потоку
data = list(map(int, sys.stdin.read().split()))

# Зчитуємо кількість міст
n = data[0]

# Зчитуємо ціни бензину
prices = data[1:n+1]

# Кількість доріг
m = data[n+1]

# Зчитуємо дороги
edges = data[n+2:]

# Побудова графа
graph = defaultdict(list)
for i in range(m):
    u = edges[2 * i] - 1
    v = edges[2 * i + 1] - 1
    graph[u].append(v)
    graph[v].append(u)

# Алгоритм Дейкстри
INF = float('inf')
dist = [INF] * n
dist[0] = 0
heap = [(0, 0)]  # (вартість, місто)

while heap:
    cost, u = heapq.heappop(heap)
    if cost > dist[u]:
        continue
    for v in graph[u]:
        new_cost = cost + prices[u]
        if new_cost < dist[v]:
            dist[v] = new_cost
            heapq.heappush(heap, (new_cost, v))

# Виведення результату
print(dist[n - 1] if dist[n - 1] != INF else -1)