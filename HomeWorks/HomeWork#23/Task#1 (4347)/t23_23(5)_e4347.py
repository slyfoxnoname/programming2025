import sys
sys.setrecursionlimit(20000)

def dfs(v, visited, adj, banned_edges, u=None):
    visited[v] = True
    for to in adj[v]:
        edge = (min(v, to), max(v, to))
        if edge not in banned_edges and not visited[to]:
            dfs(to, visited, adj, banned_edges)

if __name__ == '__main__':
    input = sys.stdin.read
    data = input().split()

    idx = 0
    n = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1

    edges = []
    adj = [[] for _ in range(n + 1)]

    for i in range(m):
        a = int(data[idx]); idx += 1
        b = int(data[idx]); idx += 1
        edges.append((a, b))
        adj[a].append(b)
        adj[b].append(a)

    k = int(data[idx]); idx += 1
    output = []

    for _ in range(k):
        c = int(data[idx]); idx += 1
        banned_edges = set()
        for _ in range(c):
            e_idx = int(data[idx]) - 1; idx += 1
            a, b = edges[e_idx]
            banned_edges.add((min(a, b), max(a, b)))

        visited = [False] * (n + 1)
        dfs(1, visited, adj, banned_edges)
        if all(visited[1:]):
            output.append("Connected")
        else:
            output.append("Disconnected")

    print("\n".join(output))