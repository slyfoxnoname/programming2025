if __name__ == '__main__':
    with open("input.txt") as f:
        n, m = map(int, f.readline().split())
        in_deg = [0] * n
        out_deg = [0] * n

        for _ in range(m):
            u, v = map(int, f.readline().split())
            out_deg[u - 1] += 1
            in_deg[v - 1] += 1

    with open("output.txt", "w") as f:
        for i in range(n):
            f.write(f"{in_deg[i]} {out_deg[i]}\n")