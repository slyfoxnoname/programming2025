def main():
    with open("input.txt") as f:
        n, m = map(int, f.readline().split())
        edges = set()
        for _ in range(m):
            a, b = map(int, f.readline().split())
            if a > b:
                a, b = b, a
            edges.add((a, b))

        required_edges = n * (n - 1) // 2
        if len(edges) == required_edges:
            print("YES")
        else:
            print("NO")

if __name__ == '__main__':
    main()
