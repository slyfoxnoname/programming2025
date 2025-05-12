def dfs(start, visited, adj, component):
    stack = [start]
    while stack:
        v = stack.pop()
        if not visited[v]:
            visited[v] = True
            component.append(v)
            for u in adj[v]:
                if not visited[u]:
                    stack.append(u)

n, m = map(int, input().split())
adj = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

visited = [False] * (n + 1)
components = []

for v in range(1, n + 1):
    if not visited[v]:
        comp = []
        dfs(v, visited, adj, comp)
        components.append(comp)

print(len(components))
for comp in components:
    print(len(comp))
    print(*comp)