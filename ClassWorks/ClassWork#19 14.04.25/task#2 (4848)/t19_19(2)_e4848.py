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

    def insert(self, item):
        self._items.append(item)
        self._sift_up(len(self._items) - 1)

    def extract_max(self):
        self._swap(1, len(self._items) - 1)
        max_item = self._items.pop()
        self._sift_down(1)
        return max_item

    def is_empty(self):
        return len(self._items) == 1  #тільки dummy 0 left


def heap_sort(arr):
    heap = Heap()
    for x in arr:
        heap.insert(x)
    sorted_arr = []
    while not heap.is_empty():
        sorted_arr.append(heap.extract_max())
    return list(reversed(sorted_arr))


if __name__ == '__main__':
    with open("input.txt") as f:
        arr = list(map(int, f.read().strip().split()))
    sorted_arr = heap_sort(arr)
    print(" ".join(map(str, sorted_arr)))
