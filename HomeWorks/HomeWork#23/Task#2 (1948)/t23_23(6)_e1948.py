from collections import deque

n, m = map(int, input().split())
adj = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    adj[a].append(b)
    indegree[b] += 1

q = deque()
for v in range(1, n + 1):
    if indegree[v] == 0:
        q.append(v)

result = []

while q:
    v = q.popleft()
    result.append(v)
    for u in adj[v]:
        indegree[u] -= 1
        if indegree[u] == 0:
            q.append(u)

if len(result) == n:
    print(*result)
else:
    print(-1)
