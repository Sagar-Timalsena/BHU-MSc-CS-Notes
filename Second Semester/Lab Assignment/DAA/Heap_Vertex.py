class MinHeap:
    def __init__(self):
        self.heap = []

    def heapify(self, i):
        smallest = i
        left = 2 * i + 1
        right = 2 * i + 2
        n = len(self.heap)

        if left < n and self.heap[left][0] < self.heap[smallest][0]:
            smallest = left
        if right < n and self.heap[right][0] < self.heap[smallest][0]:
            smallest = right

        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self.heapify(smallest)

    def build_min_heap(self, arr):
        self.heap = arr
        n = len(self.heap)
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(i)

    def insert(self, priority, vertex_pair):
        self.heap.append((priority, vertex_pair))
        i = len(self.heap) - 1
        while i > 0:
            parent = (i - 1) // 2
            if self.heap[i][0] < self.heap[parent][0]:
                self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
                i = parent
            else:
                break

    def extract_min(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapify(0)
        return root

    def get_min(self):
        return self.heap[0] if self.heap else None

    def print_heap(self):
        print("Heap array:", self.heap)


h = MinHeap()
elements = [
    (10, (1, 2)),
    (4, (0, 1)),
    (15, (2, 3)),
    (7, (1, 3)),
    (2, (0, 2))
]

print("Building heap from elements:")
for item in elements:
    print(item)
h.build_min_heap(elements)
h.print_heap()

print("\nInserting (1, (3, 4))...")
h.insert(1, (3, 4))
h.print_heap()

print("\nMinimum element:", h.get_min())

print("\nExtracting min...")
print("Extracted:", h.extract_min())
h.print_heap()
