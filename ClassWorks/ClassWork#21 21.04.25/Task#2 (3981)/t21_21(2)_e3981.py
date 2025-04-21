def create_matrix(n, adj_list):
    matrix = [[0] * n for _ in range(n)]
    for i in range(n):
        for v in adj_list[i]:
            matrix[i][v - 1] = 1
    return matrix

if __name__ == '__main__':
    n = int(input())
    adj_list = []
    for _ in range(n):
        parts = list(map(int, input().split()))
        count = parts[0]
        neighbors = parts[1:]
        adj_list.append(neighbors)

    matrix = create_matrix(n, adj_list)
    for row in matrix:
        print(' '.join(map(str, row)))