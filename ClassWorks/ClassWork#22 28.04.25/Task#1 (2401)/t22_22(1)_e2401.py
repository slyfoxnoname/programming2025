from collections import deque
class Graph:
    def __init__(self, matrix):
        self.matrix = matrix

    def bfs(self, start, finish):
        dist = [-1] * len(self.matrix)
        queue = deque()
        queue.append(start)
        dist[start] = 0

        while queue:
            u = queue.popleft()
            for v in range(len(self.matrix)):
                if self.matrix[u][v] == 1 and dist[v] == -1:
                    dist[v] = dist[u] + 1
                    queue.append(v)

        return dist[finish] if dist[finish] != -1 else 0


if __name__ == '__main__':
    f = open("input.txt")
    n, s, f = map(int, f.readline().split())
    matrix = [
        (list(map(int, f.readline().split()))) for _ in range(n)
    ]

    graph = Graph(matrix)
    print(graph.bfs(s - 1, f - 1))
f.close()