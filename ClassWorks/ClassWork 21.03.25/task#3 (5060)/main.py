def evaluate_rpn(expression: str) -> int:
    stack = []
    tokens = expression.split()  # Розбиваємо рядок на окремі елементи
    operators = {"+", "-", "*", "/"}

    for token in tokens:
        if token not in operators:  # Якщо це число, кладемо у стек
            stack.append(int(token))
        else:  # Якщо це оператор, виконуємо операцію
            b = stack.pop()
            a = stack.pop()

            if token == "+":
                stack.append(a + b)
            elif token == "-":
                stack.append(a - b)
            elif token == "*":
                stack.append(a * b)
            elif token == "/":
                stack.append(a // b)  # Цілочисельне ділення

    return stack.pop()
if __name__ == "__main__":
    input_string = input().strip()
    print(evaluate_rpn(input_string))