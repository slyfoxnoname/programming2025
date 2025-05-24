n = int(input())
INF = 10**9
graph = [list(map(int, input().split())) for _ in range(n)]

dist = [0] * n
parent = [-1] * n

x = -1  # вершина, на которой произошло обновление на последней итерации

for _ in range(n):
    x = -1
    for u in range(n):
        for v in range(n):
            w = graph[u][v]
            if w != 100000 and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                parent[v] = u
                x = v

if x == -1:
    print("NO")
else:
    # Восстановим цикл
    # Чтобы быть уверенным, что мы внутри цикла, проходим parent x n раз
    for _ in range(n):
        x = parent[x]

    cycle = []
    cur = x
    while True:
        cycle.append(cur)
        if cur == x and len(cycle) > 1:
            break
        cur = parent[cur]

    cycle.reverse()
    print("YES")
    print(len(cycle))
    # Выводим вершины с индексами +1 (т.к. входные вершины 1..n)
    print(" ".join(str(c+1) for c in cycle))
