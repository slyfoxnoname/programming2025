def bellman_ford(n, edges, start=1):
    INF = 30000
    dist = [INF] * (n + 1)
    dist[start] = 0

    for _ in range(n - 1):
        for u, v, w in edges:
            if dist[u] < INF and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    return [dist[i] if dist[i] < INF else INF for i in range(1, n + 1)]

if __name__ == '__main__':
    import sys
    input = sys.stdin.read
    data = list(map(int, input().split()))

    n, m = data[0], data[1]
    edges = []

    for i in range(m):
        u, v, w = data[2 + i * 3], data[3 + i * 3], data[4 + i * 3]
        edges.append((u, v, w))

    result = bellman_ford(n, edges)
    print(" ".join(map(str, result)))
