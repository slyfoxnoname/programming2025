def binary_search(func, left, right, eps=1e-6):
    while right - left > eps:
        mid = (left + right) / 2
        if func(mid):
            right = mid
        else:
            left = mid
    return left

# 4.5 Корінь рівняння x³ + 4x² + x - 6 = 0 на [0, 2]
def f3(x):
    return x**3 + 4*x**2 + x - 6

x3 = binary_search(lambda x: f3(x) > 0, 0, 2)
print(f"x = {x3:.6f}")
