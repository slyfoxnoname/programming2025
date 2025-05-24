import heapq
from collections import defaultdict

def find_earliest_arrival(n, d, v, r, routes):
    graph = defaultdict(list)
    for u, t1, w, t2 in routes:
        graph[u].append((t1, w, t2))

    earliest_time = [float('inf')] * (n + 1)
    earliest_time[d] = 0

    heap = [(0, d)]

    while heap:
        current_time, village = heapq.heappop(heap)
        if current_time > earliest_time[village]:
            continue
        for dep_time, dest, arr_time in graph[village]:
            if dep_time >= current_time and arr_time < earliest_time[dest]:
                earliest_time[dest] = arr_time
                heapq.heappush(heap, (arr_time, dest))

    return earliest_time[v] if earliest_time[v] != float('inf') else -1

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        n = int(f.readline())
        d, v = map(int, f.readline().split())
        r = int(f.readline())
        routes = [tuple(map(int, f.readline().split())) for _ in range(r)]

    result = find_earliest_arrival(n, d, v, r, routes)
    print(result)
