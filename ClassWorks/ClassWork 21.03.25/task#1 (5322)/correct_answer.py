def convert(number: str, from_base: int, to_base: int) -> str:
    def get_char(n: int) -> str:
        if n < 10:
            return str(n)
        return chr(ord('A') + (n - 10))  # Для A-F в 16-ричной системе

    decimal = 0
    for d in number:
        decimal = decimal * from_base + int(d, from_base)

    if decimal == 0:  # Обрабатываем случай, когда число равно "0"
        return "0"

    stack = []
    while decimal > 0:
        stack.append(decimal % to_base)
        decimal //= to_base

    res = ""
    while stack:
        res += get_char(stack.pop())

    return res


if __name__ == '__main__':
    print(convert("1010", 2, 16))  # "A"
    print(convert("FF", 16, 10))   # "255"
    print(convert("0", 10, 2))     # "0"
