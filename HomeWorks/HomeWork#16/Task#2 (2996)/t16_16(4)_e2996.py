class Officer:
    def __init__(self, bribe):
        self.bribe = bribe
        self.subordinates = []

    def min_total_bribe(self):
        if not self.subordinates:
            return self.bribe
        min_sub_bribe = min(sub.min_total_bribe() for sub in self.subordinates)
        return self.bribe + min_sub_bribe


def read_input():
    n = int(input())
    officers = [None] * n
    raw_subordinates = [[] for _ in range(n)]

    for i in range(n):
        data = list(map(int, input().split()))
        bribe = data[0]
        k = data[1]
        subs = data[2:] if k > 0 else []
        officers[i] = Officer(bribe)
        raw_subordinates[i] = subs

    # Тепер зв'язуємо об'єкти між собою
    for i in range(n):
        for s in raw_subordinates[i]:
            officers[i].subordinates.append(officers[s - 1])  # 1-based → 0-based

    return officers[0]  # Міністр — перший (індекс 0)


if __name__ == "__main__":
    minister = read_input()
    print(minister.min_total_bribe())
