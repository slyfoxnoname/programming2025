from collections import deque

def allowed_moves(num):
    s = str(num)
    moves = []

    # Збільшити першу цифру
    if s[0] != '9':
        moves.append(str(int(s[0]) + 1) + s[1:])

    # Зменшити останню цифру
    if s[3] != '1':
        moves.append(s[:3] + str(int(s[3]) - 1))

    # Зсув праворуч
    moves.append(s[3] + s[:3])

    # Зсув ліворуч
    moves.append(s[1:] + s[0])

    # Відкинути числа з нулями
    return [m for m in moves if '0' not in m]

def bfs(start, end):
    queue = deque()
    visited = set()
    parent = {}

    queue.append(start)
    visited.add(start)
    parent[start] = None

    while queue:
        current = queue.popleft()

        if current == end:
            break

        for next_num in allowed_moves(current):
            if next_num not in visited:
                visited.add(next_num)
                parent[next_num] = current
                queue.append(next_num)

    # Відновлення шляху
    path = []
    cur = end
    while cur is not None:
        path.append(cur)
        cur = parent[cur]

    return path[::-1]

# Зчитування
start = input().strip()
end = input().strip()

# Обчислення та вивід
result = bfs(start, end)
for num in result:
    print(num)
