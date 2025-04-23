if __name__ == '__main__':
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]

    edges = []
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 1:
                edges.append((i + 1, j + 1))  # Вершини нумеруються з 1
    edges.sort()  # Сортуємо спочатку по першій, потім по другій вершині
    for u, v in edges:
        print(u, v)