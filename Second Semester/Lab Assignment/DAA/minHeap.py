class MinHeap:
    def __init__(self):
        self.heap = []

    def heapify(self, i):
        smallest = i
        left = 2 * i + 1
        right = 2 * i + 2
        n = len(self.heap)

        if left < n and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < n and self.heap[right] < self.heap[smallest]:
            smallest = right

        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self.heapify(smallest)

    def build_min_heap(self, arr):
        self.heap = arr
        n = len(self.heap)
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(i)

    def insert(self, key):
        self.heap.append(key)
        i = len(self.heap) - 1
        while i > 0:
            parent = (i - 1) // 2
            if self.heap[i] < self.heap[parent]:
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
        print(self.heap)

h = MinHeap()

#Below is some driver code to check the working 
'''
elements = [5, 3, 8, 4, 1, 2]
print("Building heap from:", elements)
h.build_min_heap(elements)
h.print_heap()

print("\nInserting 0 into heap...")
h.insert(0)
h.print_heap()

print("\nMinimum element:", h.get_min())

print("\nExtracting min...")
print("Extracted:", h.extract_min())
h.print_heap()
'''