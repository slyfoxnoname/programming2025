def hamming_distance(s1, s2):
    return sum(a != b for a, b in zip(s1, s2))

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
if __name__ == '__main__':
    with open('input.txt') as f:
        n, k = map(int, f.readline().split())
        dna = [f.readline().strip() for _ in range(n)]

        edges = []
        for i in range(n):
            for j in range(i + 1, n):
                d = hamming_distance(dna[i], dna[j])
                edges.append((d, i, j))

        edges.sort()

        parent = list(range(n))
        rank = [0] * n
        mst_weight = 0
        mst_edges = []

        for weight, u, v in edges:
            if union(parent, rank, u, v):
                mst_weight += weight
                mst_edges.append((u, v))
                if len(mst_edges) == n - 1:
                    break

        print(mst_weight)
        for u, v in mst_edges:
            print(u, v)