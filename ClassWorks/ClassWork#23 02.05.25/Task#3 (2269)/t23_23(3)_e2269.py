def dfs(v, visited, graph):
    visited[v] = True
    for u in range(len(graph)):
        if graph[v][u] == 1 and not visited[u]:
            dfs(u, visited,graph)

if __name__ == '__main__':
    with open("input.txt") as f:
        n = int(f.readline())
        graph = [list(map(int, f.readline().split())) for _ in range(n)]

        visited = [False] * n
        components = 0

        for v in range(n):
            if not visited[v]:
                dfs(v, visited,graph)
                components += 1

        print(components)

