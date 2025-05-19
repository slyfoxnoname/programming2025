
import heapq
def prim(n, graph):
    visited = [False] * (n +1)
    min_heap = [(0,1)]
    total_weight = 0

    while min_heap:
        weight ,u = heapq.heappop(min_heap)
        if visited[u]:
            continue
        visited[u] = True
        total_weight += weight
        for w,v in graph[u]:
            if not visited[v]:
                heapq.heappush(min_heap,(w,v))

    return total_weight

if __name__ == '__main__':
    with open("input.txt") as f:
        n,m = map(int, f.readline().split())
        graph = [[]for _ in range(n+1)]
        for _ in range(m):
            a,b,c = map(int, f.readline().split())
            graph[a].append((c,b))
            graph[b].append((c,a))
        print(prim(n,graph))