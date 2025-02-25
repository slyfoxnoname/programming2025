import math

def binary_search(C):
    l, r = 0, max(1, C)
    while r - l > 1e-7:  # Точність 10^(-6)
        m = (l + r) / 2
        if m * m + math.sqrt(m) < C:
            l = m
        else:
            r = m
    print(f"{l:.6f}")

C = float(input().strip())
binary_search(C)
