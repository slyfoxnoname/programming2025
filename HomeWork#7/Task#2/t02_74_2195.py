import re

def check_essay():
    # Читаем первые два числа
    n, m = map(int, input().split())

    # Читаем N слов из словаря и приводим к нижнему регистру
    vocabulary = {input().strip().lower() for _ in range(n)}

    # Читаем M строк сочинения и объединяем их в один текст
    text = " ".join(input().strip() for _ in range(m)).lower()

    # Извлекаем слова из текста (оставляем только латинские буквы)
    words_in_text = set(re.findall(r"[a-z]+", text))

    # Проверяем условия
    if not words_in_text.issubset(vocabulary):
        print("Some words from the text are unknown.")
    elif not vocabulary.issubset(words_in_text):
        print("The usage of the vocabulary is not perfect.")
    else:
        print("Everything is going to be OK.")

if __name__ == "__main__":
    check_essay()
    