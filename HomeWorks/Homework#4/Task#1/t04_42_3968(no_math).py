def sqrt_approx(x, eps=1e-7):
    if x == 0:
        return 0
    r = x
    while abs(r * r - x) > eps:
        r = (r + x / r) / 2
    return r

def binary_search(C):
    l, r = 0, max(1, C)
    while r - l > 1e-7:  # Точность 10^(-6)
        m = (l + r) / 2
        if m * m + sqrt_approx(m) < C:
            l = m
        else:
            r = m
    print(f"{l:.6f}")

C = float(input().strip())
binary_search(C)