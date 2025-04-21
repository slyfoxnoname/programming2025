def main():
    n = int(input())
    k = int(input())
    graph = [[] for _ in range(n + 1)]

    for _ in range(k):
        parts = input().split()
        if parts[0] == '1':
            u = int(parts[1])
            v = int(parts[2])
            graph[u].append(v)
            graph[v].append(u)
        elif parts[0] == '2':
            u = int(parts[1])
            print(' '.join(map(str, graph[u])))

main()