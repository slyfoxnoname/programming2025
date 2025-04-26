def main():
    with open("input.txt") as f:
        n, m = map(int, f.readline().split())
        degree = [0] * n
        for _ in range(m):
            a, b = map(int, f.readline().split())
            degree[a - 1] += 1
            degree[b - 1] += 1
        for d in degree:
            print(d)

if __name__ == '__main__':
    main()
