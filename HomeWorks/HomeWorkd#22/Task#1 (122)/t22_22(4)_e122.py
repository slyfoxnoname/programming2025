def count_routes(n, graph, current, end, d, visited):
    if d < 0:
        return 0
    if current == end:
        return 1
    visited[current] = True
    total = 0
    for neighbor in graph[current]:
        if not visited[neighbor]:
            total += count_routes(n, graph, neighbor, end, d - 1, visited)
    visited[current] = False
    return total

if __name__ == '__main__':
    with open("input.txt") as f:
        n, k, a, b, d = map(int, f.readline().split())
        graph = [[] for _ in range(n + 1)]
        for _ in range(k):
            u, v = map(int, f.readline().split())
            graph[u].append(v)

        visited = [False] * (n + 1)
        result = count_routes(n, graph, a, b, d, visited)
        print(result)
