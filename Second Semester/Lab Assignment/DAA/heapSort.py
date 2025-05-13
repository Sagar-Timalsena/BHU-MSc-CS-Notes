from minHeap import MinHeap

def heap_sort(arr):
    h = MinHeap()
    h.build_min_heap(arr[:]) #Construct a heap out of the elements of the array
    sorted_arr = []
    while h.heap:
        sorted_arr.append(h.extract_min())
    return sorted_arr

# Example usage:
arr = [5, 3, 8, 4, 1, 2]
sorted_arr = heap_sort(arr)
print("Heap-sorted array:", sorted_arr)
