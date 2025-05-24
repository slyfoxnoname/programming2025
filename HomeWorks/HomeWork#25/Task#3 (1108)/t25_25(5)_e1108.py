if __name__ == '__main__':
    with open("input.txt") as f:
        n, m = map(int, f.readline().split())
        edges = []

        for _ in range(m):
            x, y, t = map(int, f.readline().split())
            edges.append((x, y, t))

        dist = [float('inf')] * n
        dist[0] = 0

        for _ in range(n - 1):
            for u, v, w in edges:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w

        # Ще одна ітерація для перевірки на негативний цикл
        for u, v, w in edges:
            if dist[u] + w < dist[v]:
                print("possible")
                break
        else:
            print("not possible")
