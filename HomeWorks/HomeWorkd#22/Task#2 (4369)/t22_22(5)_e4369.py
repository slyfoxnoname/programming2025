from collections import deque
def main():
    with open("input.txt") as f:

        n, m = map(int, f.readline().split())
        graph = [[] for _ in range(n + 1)]

        for _ in range(m):
            u, v = map(int, f.readline().split())
            graph[u].append(v)
            graph[v].append(u)

        k = int(f.readline())
        fires = list(map(int, f.readline().split()))

        # Ініціалізація часу займання
        burn_time = [-1] * (n + 1)
        queue = deque()

        for f in fires:
            burn_time[f] = 0
            queue.append(f)

        # BFS
        while queue:
            u = queue.popleft()
            for v in graph[u]:
                if burn_time[v] == -1:
                    burn_time[v] = burn_time[u] + 1
                    queue.append(v)

        # Знаходимо максимальний час і мінімальну вершину
        max_time = max(burn_time[1:])
        candidates = [i for i, t in enumerate(burn_time) if t == max_time]
        print(max_time)
        print(min(candidates))

main()
