class SegmentTree:
    def __init__(self, array, operation, default):
        self.n = len(array)
        self.tree = [default] * (2 * self.n)
        self.operation = operation
        self.default = default

        # Заповнюємо листи дерева
        for i in range(self.n):
            self.tree[self.n + i] = array[i]

        # Будуємо дерево
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.operation(self.tree[2 * i], self.tree[2 * i + 1])

    def query(self, left, right):
        """Обчислює результат операції на відрізку [left, right]"""
        res = self.default
        left += self.n
        right += self.n
        while left <= right:
            if left % 2 == 1:
                res = self.operation(res, self.tree[left])
                left += 1
            if right % 2 == 0:
                res = self.operation(res, self.tree[right])
                right -= 1
            left //= 2
            right //= 2
        return res

    def update(self, idx, value):
        """Оновлює значення в масиві на позиції idx"""
        idx += self.n
        self.tree[idx] = value
        while idx > 1:
            idx //= 2
            self.tree[idx] = self.operation(self.tree[2 * idx], self.tree[2 * idx + 1])


def gcd(a, b):
    """Обчислення НСД за алгоритмом Евкліда"""
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    """Обчислення НСК через НСД"""
    return a * b // gcd(a, b)

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    m = int(input())

    # Створюємо два дерева відрізків: для НСД та НСК
    gcd_tree = SegmentTree(arr, gcd, 0)  # для НСД
    lcm_tree = SegmentTree(arr, lcm, 1)  # для НСК

    for _ in range(m):
        q, l, r = map(int, input().split())
        if q == 1:
            # Обчислюємо НСД і НСК на відрізку [l-1, r-1]
            gcd_result = gcd_tree.query(l - 1, r - 1)
            lcm_result = lcm_tree.query(l - 1, r - 1)

            if gcd_result < lcm_result:
                print("wins")
            elif gcd_result > lcm_result:
                print("loser")
            else:
                print("draw")
        elif q == 2:
            # Оновлення елемента на позиції l-1
            arr[l - 1] = r  # Спочатку оновлюємо масив arr
            lcm_tree.update(l - 1, arr[l - 1])  # В оновленому дереві НСК
            gcd_tree.update(l - 1, arr[l - 1])  # В оновленому дереві НСД


if __name__ == "__main__":
    main()
