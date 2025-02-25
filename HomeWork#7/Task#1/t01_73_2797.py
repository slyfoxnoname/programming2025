def count_unique_numbers():
    unique_numbers = set()
    try:
        while True:  # Читаем данные построчно, если входные данные большие
            line = input().strip()
            numbers = map(int, line.split())
            unique_numbers.update(numbers)
    except EOFError:
        pass  # Заканчиваем, когда все данные прочитаны
    return len(unique_numbers)

if __name__ == '__main__':
    print(count_unique_numbers())  # Выводим количество уникальных номеров
