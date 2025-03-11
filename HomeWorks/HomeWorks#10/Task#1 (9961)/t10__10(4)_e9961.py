def generate_permutations(n, k):
    def backtrack(path, used):
        if len(path) == k:
            print(*path)
            return
        for i in range(1, n + 1):
            if not used[i]:
                used[i] = True
                path.append(i)
                backtrack(path, used)
                path.pop()
                used[i] = False

    used = [False] * (n + 1)
    backtrack([], used)

n, k = map(int, input().split())
generate_permutations(n, k)
