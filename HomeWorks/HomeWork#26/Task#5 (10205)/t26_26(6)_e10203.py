import sys
import math

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, rank, x, y):
    xroot = find(parent, x)
    yroot = find(parent, y)
    if xroot == yroot:
        return False
    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    else:
        parent[yroot] = xroot
        if rank[xroot] == rank[yroot]:
            rank[xroot] += 1
    return True

T = int(sys.stdin.readline())
for _ in range(T):
    s, p = map(int, sys.stdin.readline().split())
    points = [tuple(map(int, sys.stdin.readline().split())) for _ in range(p)]

    edges = []
    for i in range(p):
        for j in range(i + 1, p):
            dist = math.hypot(points[i][0] - points[j][0], points[i][1] - points[j][1])
            edges.append((dist, i, j))

    edges.sort()  # Краскал

    parent = list(range(p))
    rank = [0] * p
    mst_edges = []

    for edge in edges:
        d, u, v = edge
        if union(parent, rank, u, v):
            mst_edges.append(d)

    # Видаляємо s-1 найдовших ребер
    mst_edges.sort(reverse=True)
    answer = mst_edges[s - 1] if len(mst_edges) >= s else 0.0

    print(f"{answer:.2f}")
