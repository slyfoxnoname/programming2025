def dfs(v, visited, graph):
    visited[v] = True
    for u in range(len(graph)):
        if graph[v][u] == 1 and not visited[u]:
            dfs(u, visited, graph)

if __name__ == '__main__':
    n, s = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(n)]

    visited = [False] * n
    dfs(s - 1, visited, graph)

    print(sum(visited))