from collections import deque

def main():
    with open("input.txt") as f:
        n, x = map(int, f.readline().split())
        adj_matrix = [list(map(int, f.readline().split())) for _ in range(n)]

        dist = [-1] * n
        dist[x - 1] = 0

        queue = deque([x - 1])

        while queue:
            u = queue.popleft()
            for v in range(n):
                if adj_matrix[u][v] == 1 and dist[v] == -1:
                    dist[v] = dist[u] + 1
                    queue.append(v)

        print(' '.join(map(str, dist)))

main()
