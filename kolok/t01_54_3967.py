def can_cut(ropes, length, k):
    count = 0
    for rope in ropes:
        count += rope // length
    return count >= k

def solve(n, k, ropes):

    left, right = 1, max(ropes)
    best_length = 0

    while left <= right:
        mid = (left + right) // 2
        if can_cut(ropes, mid, k):
            best_length = mid
            left = mid + 1
        else:
            right = mid - 1

    return best_length

n, k = map(int, input().split())
ropes = [int(input()) for _ in range(n)]
print(solve(n, k, ropes))