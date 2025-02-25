def max_cyclic_shift(n):
    binary = bin(n)[2:]  #  Уявляємо число у двійковій системі без префікса '0b'
    max_val = n  # Початкове максимальне значення

    for _ in range(len(binary) - 1):  # Робимо len(binary)-1 зрушення
        binary = binary[1:] + binary[0]  # Лівий циклічний зрушення
        max_val = max(max_val, int(binary, 2))  # оновлюємо максимум

    return max_val

# Зчитуємо вхідні данні
n = int(input())
print(max_cyclic_shift(n))
