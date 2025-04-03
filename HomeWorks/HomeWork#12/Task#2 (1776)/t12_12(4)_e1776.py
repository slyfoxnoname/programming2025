import sys


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        return self.stack.pop() if self.stack else None

    def top(self):
        return self.stack[-1] if self.stack else None

    def is_empty(self):
        return len(self.stack) == 0


def can_reorder(train, n):
    stack = Stack()
    current = 1

    for wagon in train:
        while current <= n and (stack.is_empty() or stack.top() != wagon):
            stack.push(current)
            current += 1

        if stack.top() == wagon:
            stack.pop()
        else:
            return "No"

    return "Yes"


def main():
    input_data = sys.stdin.read().strip().split("\n")
    index = 0

    while index < len(input_data):
        n = int(input_data[index])
        if n == 0:
            break
        index += 1
        results = []

        while index < len(input_data) and input_data[index] != "0":
            train = list(map(int, input_data[index].split()))
            results.append(can_reorder(train, n))
            index += 1

        print("\n".join(results))
        print()
        index += 1


if __name__ == "__main__":
    main()
