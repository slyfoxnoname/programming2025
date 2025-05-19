def hamming_distance(s1, s2):
    return sum(a != b for a, b in zip(s1, s2))

if __name__ == '__main__':
    with open('input.txt') as f:
        n, k = map(int, f.readline().split())
        dna = [f.readline().strip() for _ in range(n)]

    # Побудова повного графа: для кожної вершини зберігаємо суміжні ребра
    graph = [[] for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            d = hamming_distance(dna[i], dna[j])
            graph[i].append((d, j))
            graph[j].append((d, i))

    # Ініціалізація для алгоритму Прима
    visited = [False] * n
    mst_weight = 0
    mst_edges = []

    # Пріоритетна черга (містить пари (вага, вершина, звідки))
    heap = [(0, 0, -1)]  # Починаємо з вершини 0

    while heap and len(mst_edges) < n - 1:
        # Вибираємо найкоротніше ребро
        min_weight = float('inf')
        min_index = -1
        for i in range(len(heap)):
            if heap[i][0] < min_weight:
                min_weight = heap[i][0]
                min_index = i
        weight, u, from_v = heap[min_index]
        heap[min_index] = heap[-1]
        heap.pop()

        if visited[u]:
            continue

        visited[u] = True
        mst_weight += weight
        if from_v != -1:
            mst_edges.append((from_v, u))

        for w, v in graph[u]:
            if not visited[v]:
                heap.append((w, v, u))

    # Вивід результату
    print(mst_weight)
    for u, v in mst_edges:
        print(u, v)
