from minHeap import MinHeap

class PriorityQueue:
    def __init__(self):
        self.heap = MinHeap()
        self.counter = 0  #FIFO for same-priority elements

    def enqueue(self, item, priority):
        '''
        Wrap the item in a tuple: (priority, counter, item)
        We need not modify our original minHeap code as self.heap[i][0]
        to obtain priority as Python compares tuples lexographically, i.e.
        one-by-one. In this case it will compare priority, if equal, then counter.
        '''
        self.heap.insert((priority, self.counter, item))
        self.counter += 1

    def dequeue(self):
        if self.is_empty():
            return None
        return self.heap.extract_min()[2]

    def peek(self):
        if self.is_empty():
            return None
        return self.heap.get_min()[2]

    def is_empty(self):
        return len(self.heap.heap) == 0

    def size(self):
        return len(self.heap.heap)

    def print_queue(self):
        print([x[2] for x in self.heap.heap])

pq = PriorityQueue()
tasks = [("task1",3), ("task2",1), ("task3",1), ("task4",2), ("task5",4), ("task6",5)]
for t in tasks:
    pq.enqueue(t[0], t[1])

pq.print_queue()
print("Dequeued:", pq.dequeue())

pq.print_queue()
print("Next task:", pq.peek())
print("Queue size:", pq.size())