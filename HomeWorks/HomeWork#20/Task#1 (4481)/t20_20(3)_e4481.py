import math


# Функция для побудови дерева відрізків з підтримкою ленивих оновлень
def build_segment_tree(arr, n):
    tree = [0] * (4 * n)
    lazy = [None] * (4 * n)  # Лінивий масив

    def build(v, tl, tr):
        if tl == tr:
            tree[v] = arr[tl]
        else:
            tm = (tl + tr) // 2
            build(2 * v, tl, tm)
            build(2 * v + 1, tm + 1, tr)
            tree[v] = math.gcd(tree[2 * v], tree[2 * v + 1])

    build(1, 0, n - 1)
    return tree, lazy


# Функція для застосування лінивого оновлення
def apply_lazy(tree, lazy, v, tl, tr):
    if lazy[v] is not None:
        tree[v] = lazy[v]
        if tl != tr:
            lazy[2 * v] = lazy[v]
            lazy[2 * v + 1] = lazy[v]
        lazy[v] = None


# Функція для запиту НСД на відрізку [l, r]
def query(tree, lazy, v, tl, tr, l, r):
    apply_lazy(tree, lazy, v, tl, tr)
    if l > r:
        return 0  # Повертаємо 0, щоб ігнорувати цю частину
    if l == tl and r == tr:
        return tree[v]
    tm = (tl + tr) // 2
    left_gcd = query(tree, lazy, 2 * v, tl, tm, l, min(r, tm))
    right_gcd = query(tree, lazy, 2 * v + 1, tm + 1, tr, max(l, tm + 1), r)
    return math.gcd(left_gcd, right_gcd)


# Функція для оновлення значення на позиції pos
def update(tree, lazy, v, tl, tr, pos, new_value):
    apply_lazy(tree, lazy, v, tl, tr)
    if tl == tr:
        tree[v] = new_value
    else:
        tm = (tl + tr) // 2
        if pos <= tm:
            update(tree, lazy, 2 * v, tl, tm, pos, new_value)
        else:
            update(tree, lazy, 2 * v + 1, tm + 1, tr, pos, new_value)
        tree[v] = math.gcd(tree[2 * v], tree[2 * v + 1])


# Основна функція для обробки запитів
def solve():
    n = int(input())  # Кількість елементів масиву
    arr = list(map(int, input().split()))  # Масив
    m = int(input())  # Кількість запитів

    # Створюємо дерево відрізків з лінивими оновленнями
    tree, lazy = build_segment_tree(arr, n)

    for _ in range(m):
        query_info = list(map(int, input().split()))
        q = query_info[0]
        l = query_info[1] - 1  # Переведемо в 0-індексацію
        r = query_info[2]

        if q == 1:
            # Запит НСД на відрізку [l, r]
            print(query(tree, lazy, 1, 0, n - 1, l, r - 1))
        elif q == 2:
            # Оновлення елемента на позиції l
            update(tree, lazy, 1, 0, n - 1, l, r)


# Викликаємо основну функцію для виконання
if __name__ == "__main__":
    solve()
