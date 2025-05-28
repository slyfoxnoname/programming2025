import sys
from math import hypot

def main():
    input_lines = sys.stdin.read().splitlines()
    i = 0
    res = []

    while i < len(input_lines):
        if input_lines[i] == '0':
            break
        n = int(input_lines[i])
        i += 1
        pts = [tuple(map(int, input_lines[i + j].split())) for j in range(n)]
        i += n

        parent = list(range(n))
        rank = [0] * n

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            xroot = find(x)
            yroot = find(y)
            if xroot == yroot:
                return
            if rank[xroot] < rank[yroot]:
                parent[xroot] = yroot
            else:
                parent[yroot] = xroot
                if rank[xroot] == rank[yroot]:
                    rank[xroot] += 1

        edges = []
        for a in range(n):
            x1, y1 = pts[a]
            for b in range(a + 1, n):
                x2, y2 = pts[b]
                edges.append((hypot(x1 - x2, y1 - y2), a, b))
        edges.sort()

        total = 0.0
        count = 0
        for d, u, v in edges:
            if find(u) != find(v):
                union(u, v)
                total += d
                count += 1
                if count == n - 1:
                    break
        res.append(f"{total:.2f}")

    print('\n'.join(res))

main()
