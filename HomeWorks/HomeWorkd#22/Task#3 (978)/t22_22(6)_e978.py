def main():
    with open("input.txt") as f:
        n, m = map(int, f.readline().split())
        graph = [[] for _ in range(n + 1)]

        edges = []
        for _ in range(m):
            u, v = map(int, f.readline().split())
            graph[u].append(v)
            graph[v].append(u)

        visited = [False] * (n + 1)
        tree_edges = []

    def dfs(u):
        visited[u] = True
        for v in graph[u]:
            if not visited[v]:
                tree_edges.append((u, v))
                dfs(v)

    dfs(1)

    for u, v in tree_edges:
        print(u, v)


main()

