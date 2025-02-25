def binary_search(func, left, right, eps=1e-6):
    while right - left > eps:
        mid = (left + right) / 2
        if func(mid):
            right = mid
        else:
            left = mid
    return left

# 4.3 Найменше x ∈ [0, 10], що f(x) > 5
def f1(x):
    return x**3 + x + 1 > 5

x1 = binary_search(f1, 0, 10)
print(f" x = {x1:.6f}")
