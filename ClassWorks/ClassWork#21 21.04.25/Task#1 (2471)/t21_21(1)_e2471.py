def create_graph(n, matrix):
    edges = []
    for i in range(n):
        for j in range(i + 1, n):  # беремо тільки верхній трикутник, бо граф неорієнтований
            if matrix[i][j] == 1:
                edges.append((i + 1, j + 1))  # вершини нумеруються з 1
    return edges

if __name__ == '__main__':
    n = int(input())
    matrix = []
    for _ in range(n):
        row = list(map(int, input().split()))
        matrix.append(row)

    edges = create_graph(n, matrix)
    for u, v in edges:
        print(u, v)