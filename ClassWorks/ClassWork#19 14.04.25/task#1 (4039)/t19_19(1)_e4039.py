class Heap:
    def __init__(self):
        self._items = [0]  # 1-based indexing

    def _swap(self, i, j):
        self._items[i], self._items[j] = self._items[j], self._items[i]

    def _sift_up(self, i):
        while i > 1 and self._items[i] > self._items[i // 2]:
            self._swap(i, i // 2)
            i //= 2

    def _sift_down(self, i):
        while 2 * i < len(self._items):
            max_index = i
            left = 2 * i
            right = 2 * i + 1

            if left < len(self._items) and self._items[left] > self._items[max_index]:
                max_index = left
            if right < len(self._items) and self._items[right] > self._items[max_index]:
                max_index = right

            if max_index == i:
                break

            self._swap(i, max_index)
            i = max_index

    def extract_max(self):
        self._swap(1, len(self._items) - 1)
        item = self._items.pop()
        self._sift_down(1)
        return item

    def insert(self, item):
        self._items.append(item)
        self._sift_up(len(self._items) - 1)

if __name__ == '__main__':
    heap = Heap()
    with open("input.txt") as f:
        n = int(f.readline())
        for _ in range(n):
            line = f.readline()
            parts = line.strip().split()
            if parts[0] == '0':
                heap.insert(int(parts[1]))
            elif parts[0] == '1':
                print(heap.extract_max())

