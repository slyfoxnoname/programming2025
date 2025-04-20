class PriorityQueue:
    def __init__(self):
        self.heap = []
        self.id_to_index = {}

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
        self.id_to_index[self.heap[i][1]] = i
        self.id_to_index[self.heap[j][1]] = j

    def _sift_up(self, i):
        while i > 0 and self.heap[i][0] > self.heap[(i - 1) // 2][0]:
            self._swap(i, (i - 1) // 2)
            i = (i - 1) // 2

    def _sift_down(self, i):
        size = len(self.heap)
        while 2 * i + 1 < size:
            max_index = i
            l = 2 * i + 1
            r = 2 * i + 2

            if l < size and self.heap[l][0] > self.heap[max_index][0]:
                max_index = l
            if r < size and self.heap[r][0] > self.heap[max_index][0]:
                max_index = r

            if max_index == i:
                break

            self._swap(i, max_index)
            i = max_index

    def add(self, id_str, priority):
        self.heap.append((priority, id_str))
        self.id_to_index[id_str] = len(self.heap) - 1
        self._sift_up(len(self.heap) - 1)

    def pop(self):
        top = self.heap[0]
        self._swap(0, len(self.heap) - 1)
        self.heap.pop()
        del self.id_to_index[top[1]]
        if self.heap:
            self._sift_down(0)
        return top

    def change(self, id_str, new_priority):
        i = self.id_to_index[id_str]
        old_priority = self.heap[i][0]
        self.heap[i] = (new_priority, id_str)
        if new_priority > old_priority:
            self._sift_up(i)
        else:
            self._sift_down(i)


if __name__ == '__main__':
    pq = PriorityQueue()
    try:
        while True:
            line = input()
            if not line:
                break
            parts = line.strip().split()
            if parts[0] == 'ADD':
                pq.add(parts[1], int(parts[2]))
            elif parts[0] == 'POP':
                id_str, priority = pq.pop()
                print(f"{id_str} {priority}")
            elif parts[0] == 'CHANGE':
                pq.change(parts[1], int(parts[2]))
    except EOFError:
        pass
