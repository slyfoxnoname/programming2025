if __name__ == '__main__':
    with open("input.txt") as f:
        n, m = map(int, f.readline().split())
        graph = [[] for _ in range(n + 1)]
        for _ in range(m):
            a, b, c = map(int, f.readline().split())
            graph[a].append((b, c))
            graph[b].append((a, c))

    visited = [False] * (n + 1)
    key = [float('inf')] * (n + 1)
    key[1] = 0
    total_weight = 0

    for _ in range(n):
        u = -1
        min_key = float('inf')
        for v in range(1, n + 1):
            if not visited[v] and key[v] < min_key:
                min_key = key[v]
                u = v
        if u == -1:
            break

        visited[u] = True
        total_weight += key[u]

        for neighbor, weight in graph[u]:
            if not visited[neighbor] and weight < key[neighbor]:
                key[neighbor] = weight

    print(total_weight)
