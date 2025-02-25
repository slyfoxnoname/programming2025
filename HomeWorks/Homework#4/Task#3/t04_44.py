import math

def binary_search(func, left, right, eps=1e-6):
    while right - left > eps:
        mid = (left + right) / 2
        if func(mid):
            right = mid
        else:
            left = mid
    return left
# 4.4 Корінь рівняння sin(x) = x / 3 на [1.6, 3]
def f2(x):
    return math.sin(x) - x / 3

x2 = binary_search(lambda x: f2(x) > 0, 1.6, 3)
print(f" x = {x2:.6f}")