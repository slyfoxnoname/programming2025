def main():
    with open("input.txt") as f:
        n,m = map(int, f.readline().split())
        degree = [0] * n
        edges = set()
        for _ in range(m):
            a, b = map(int, f.readline().split())
            if (a, b) in edges:
                print("YES")
                exit()
            edges.add((a, b))
        print("NO")


if __name__ == '__main__':
    main()

