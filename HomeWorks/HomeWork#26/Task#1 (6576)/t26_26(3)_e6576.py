import sys
sys.setrecursionlimit(100000)

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, rank, x, y):
    x_root = find(parent, x)
    y_root = find(parent, y)
    if x_root == y_root:
        return False
    if rank[x_root] < rank[y_root]:
        parent[x_root] = y_root
    else:
        parent[y_root] = x_root
        if rank[x_root] == rank[y_root]:
            rank[x_root] += 1
    return True

def dfs(u, target, visited, graph, max_weight):
    if u == target:
        return True, max_weight
    visited[u] = True
    for v, w in graph[u]:
        if not visited[v]:
            found, path_max = dfs(v, target, visited, graph, max(max_weight, w))
            if found:
                return True, path_max
    return False, 0

t = int(input())
for _ in range(t):
    n, m, p, q = map(int, input().split())
    edges = []
    edge_map = {}
    for _ in range(m):
        u, v, w = map(int, input().split())
        edges.append((w, u, v))
        edge_map[(min(u, v), max(u, v))] = w

    edges.sort()  # для алгоритму Крускала
    parent = list(range(n + 1))
    rank = [0] * (n + 1)
    mst = [[] for _ in range(n + 1)]
    mst_edges = set()

    for w, u, v in edges:
        if union(parent, rank, u, v):
            mst[u].append((v, w))
            mst[v].append((u, w))
            mst_edges.add((min(u, v), max(u, v)))

    key = (min(p, q), max(p, q))
    w_new = edge_map.get(key, None)

    if key in mst_edges:
        print("YES")
    else:
        visited = [False] * (n + 1)
        _, max_on_path = dfs(p, q, visited, mst, 0)
        if w_new is not None and w_new < max_on_path:
            print("YES")
        else:
            print("NO")