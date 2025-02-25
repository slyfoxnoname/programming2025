def binary_search(arr, target):
    left, right = 0, len(arr) - 1  # Визначаємо межі пошуку
    while left <= right:
        mid = (left + right) // 2  # Знаходимо середину поточного діапазону
        if arr[mid] == target:
            return True  # Якщо знайдено, повертаємо True
        elif arr[mid] < target:
            left = mid + 1  # Продовжуємо пошук у правій частині
        else:
            right = mid - 1  # Продовжуємо пошук у лівій частині
    return False  # Якщо не знайдено, повертаємо False

n = int(input().strip())  # Кількість видів метеликів у колекції
collection = list(map(int, input().strip().split()))  # Відсортований список метеликів
m = int(input().strip())  # Кількість запитів
queries = list(map(int, input().strip().split()))  # Запити на перевірку

for q in queries:
    if binary_search(collection, q):  # Виконуємо бінарний пошук
        print("YES")  # Якщо знайдено, виводимо "YES"
    else:
        print("NO")  # Якщо не знайдено, виводимо "NO"
