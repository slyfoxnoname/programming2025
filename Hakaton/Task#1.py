def solve(N, max_value, curr, index):
    if N == 0:
        print("+".join(map(str, curr[:index])))
        return
    for i in range(min(N, max_value), 0, -1):
        curr[index] = i
        solve(N - i, i, curr + [i], index + 1)

def main():
    N = int(input())
    curr = [0] * N
    solve(N, N - 1, curr, 0)
main()