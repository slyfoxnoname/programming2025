# Функція для реалізації алгоритму швидкого сортування
def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)  # Отримуємо індекс для опорного елемента
        quick_sort(arr, low, pi - 1)  # Сортуємо ліву частину
        quick_sort(arr, pi + 1, high)  # Сортуємо праву частину

# Функція для розподілу елементів на дві частини
import random

def partition(arr, low, high):
    pivot_index = random.randint(low, high)  # Вибір випадкового опорного елемента
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

n = int(input())  # Кількість чисел
arr = list(map(int, input().split()))  # Читаємо список чисел

quick_sort(arr, 0, n - 1)
print(*arr)
