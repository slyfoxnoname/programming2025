# Функція для злиття двох відсортованих списків
def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i][0] < right[j][0]:  # Якщо основний номер лівого елемента менший
            result.append(left[i])
            i += 1
        elif left[i][0] > right[j][0]:  # Якщо основний номер правого елемента менший
            result.append(right[j])
            j += 1
        else:  # Якщо основні номери рівні, зберігаємо початковий порядок
            result.append(left[i])
            i += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Функція для рекурсивного сортування злиттям
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])  # Рекурсивно сортуємо ліву частину
    right = merge_sort(arr[mid:])  # Рекурсивно сортуємо праву частину
    return merge(left, right)

n = int(input())  # Кількість робітників
robots = [tuple(map(int, input().split())) for _ in range(n)]

sorted_robots = merge_sort(robots)

for robot in sorted_robots:
    print(robot[0], robot[1])
