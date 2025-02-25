# Функція для знаходження першого входження елемента (аналог bisect_left)
def lower_bound(arr, target):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left

# Функція для знаходження першого елемента, більшого за target (аналог bisect_right)
def upper_bound(arr, target):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] <= target:
            left = mid + 1
        else:
            right = mid
    return left

n = int(input().strip())
colors = list(map(int, input().strip().split())) if n > 0 else []
m = int(input().strip())
queries = list(map(int, input().strip().split()))

for q in queries:
    print(upper_bound(colors, q) - lower_bound(colors, q))
