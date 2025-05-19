import heapq

INF = 10**9

if __name__ == '__main__':
    n, s, f = map(int, input().split())
    s -= 1
    f -= 1

    # Побудова графа зі списком суміжності
    graph = [[] for _ in range(n)]
    for i in range(n):
        row = list(map(int, input().split()))
        for j in range(n):
            if row[j] != -1 and i != j:
                graph[i].append((j, row[j]))  # (сусід, вага)

    # Ініціалізація
    dist = [INF] * n
    dist[s] = 0
    pq = [(0, s)]  # (відстань, вершина)

    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v, weight in graph[u]:
            if dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight
                heapq.heappush(pq, (dist[v], v))

    print(-1 if dist[f] == INF else dist[f])
