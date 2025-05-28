import sys
import math

sys.setrecursionlimit(10000)

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, rank, u, v):
    root_u = find(parent, u)
    root_v = find(parent, v)
    if root_u == root_v:
        return False
    if rank[root_u] < rank[root_v]:
        parent[root_u] = root_v
    else:
        parent[root_v] = root_u
        if rank[root_u] == rank[root_v]:
            rank[root_u] += 1
    return True

def readints():
    return list(map(int, sys.stdin.readline().split()))

input_lines = sys.stdin.read().split('\n')
i = 0
T = int(input_lines[i])
i += 1

for test in range(T):
    while i < len(input_lines) and input_lines[i] == '':
        i += 1

    n = int(input_lines[i])
    i += 1
    coords = []
    for _ in range(n):
        x, y = map(int, input_lines[i].split())
        coords.append((x, y))
        i += 1

    parent = list(range(n))
    rank = [0] * n

    m = int(input_lines[i])
    i += 1
    for _ in range(m):
        u, v = map(int, input_lines[i].split())
        union(parent, rank, u-1, v-1)
        i += 1

    edges = []
    for u in range(n):
        for v in range(u+1, n):
            dist = math.hypot(coords[u][0] - coords[v][0], coords[u][1] - coords[v][1])
            edges.append((dist, u, v))

    edges.sort()
    result = []
    for dist, u, v in edges:
        if union(parent, rank, u, v):
            result.append((u+1, v+1))

    if result:
        for u, v in result:
            print(f"{u} {v}")
    else:
        print("No new highways need")

    if test < T - 1:
        print()
