# BRACKETS = {')': '(', ']': '['}
def is_valid_bracket_sequence(s: str) -> str:
        stack = []
        BRACKETS = {')': '(', ']': '['}
        for bracket in s:
            if bracket in "([":
                stack.append(bracket)
            elif bracket in ")]":
                if not stack or stack[-1] != BRACKETS[bracket]:
                    return "No"
                stack.pop()

        return "Yes" if not stack else "No"


if __name__ == "__main__":
    n = int(input().strip())
    for _ in range(n):
        s = input().strip()
        print(is_valid_bracket_sequence(s))