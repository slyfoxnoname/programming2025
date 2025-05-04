def dfs(v, visited, graph):
    visited[v] = True
    for u in graph[v]:
        if not visited[u]:
            dfs(u, visited, graph)

if __name__ == '__main__':
    with open("input.txt") as f:
        n, m = map(int, f.readline().split())
        graph = [[] for _ in range(n)]

        for _ in range(m):
            u, v = map(int, f.readline().split())
            graph[u - 1].append(v -1)
            graph[v - 1].append(u - 1)

        visited = [False] * n
        dfs(0, visited, graph)

        print("YES" if all(visited) else "NO")