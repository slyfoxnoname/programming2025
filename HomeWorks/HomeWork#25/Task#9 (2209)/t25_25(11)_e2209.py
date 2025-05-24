import heapq

N, U, D, I, J, L = map(int, input().split())

floors = []  # список ліфтів, кожен — це відсортований список поверхів
all_lift_floors = set()

for _ in range(L):
    data = list(map(int, input().split()))
    K = data[0]
    stops = data[1:]
    floors.append(stops)
    all_lift_floors.update(stops)

# Для кожного поверху ми маємо 2 вершини:
# 0..N-1 — пішохідні, N..2N-1 — ліфтові
offset = N
graph = [[] for _ in range(2 * N)]

# Додамо ребра між пішохідними поверхами (сходи)
for floor in range(1, N+1):
    if floor < N:
        # Вгору сходами
        graph[floor-1].append((floor, U))
        # Вниз сходами
        graph[floor].append((floor-1, D))

# Вхід у ліфт / вихід з ліфта на одному поверсі
for floor in range(1, N+1):
    # Вхід в ліфт
    graph[floor-1].append((floor-1 + offset, I))
    # Вихід з ліфта
    graph[floor-1 + offset].append((floor-1, J))

# Додамо ребра між ліфтовими вершинами кожного ліфта з вагою 0
for stops in floors:
    # ребра між усіма парами поверхів ліфта (повний граф)
    for i in range(len(stops)):
        for j in range(i+1, len(stops)):
            u = stops[i] - 1 + offset
            v = stops[j] - 1 + offset
            graph[u].append((v, 0))
            graph[v].append((u, 0))

# Алгоритм Дейкстри
dist = [float('inf')] * (2 * N)
dist[0] = 0
pq = [(0, 0)]  # (вартість, вершина)

while pq:
    cur_dist, u = heapq.heappop(pq)
    if cur_dist > dist[u]:
        continue
    for v, w in graph[u]:
        nd = cur_dist + w
        if nd < dist[v]:
            dist[v] = nd
            heapq.heappush(pq, (nd, v))

# Мінімальна вартість — мінімум між пішохідною та ліфтовою вершинами N-го поверху
answer = min(dist[N-1], dist[N-1 + offset])
print(answer)
