def count_heights_in_range(n, heights, a, b):
    count = 0
    for h in heights:
        if a <= h <= b:
            count += 1
    return count

while True:
    try:
        n = int(input().strip())  # Кількість членів делегаціі
        heights = list(map(int, input().strip().split()))  # Список зростань
        a, b = map(int, input().strip().split())  # Границі діапазону


        print(count_heights_in_range(n, heights, a, b))
    except EOFError:
        break