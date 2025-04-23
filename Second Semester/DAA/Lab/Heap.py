import random
import time
import math
import matplotlib.pyplot as plt

# Heapify function to maintain max-heap property
def heapify(arr, n, i):
    largest = i
    # Left child index
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

# Heap sort algorithm
def heap_sort(arr):
    n = len(arr)

    # Build max-heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

# Test case generators
def best_case(size):
    return list(range(size))  # Already sorted

def worst_case(size):
    return list(range(size, 0, -1))  # Reverse sorted

def average_case(size):
    arr = list(range(size))
    random.shuffle(arr)
    return arr

# Input sizes to test
input_sizes = list(range(5000, 200001, 15000))

# Lists to hold execution times
best_times = []
worst_times = []
avg_times = []

# Benchmarking loop
for size in input_sizes:
    # Best Case
    arr = best_case(size)
    start = time.time()
    heap_sort(arr)
    best_times.append((time.time() - start) * 1000)

    # Worst Case
    arr = worst_case(size)
    start = time.time()
    heap_sort(arr)
    worst_times.append((time.time() - start) * 1000)

    # Average Case
    arr = average_case(size)
    start = time.time()
    heap_sort(arr)
    avg_times.append((time.time() - start) * 1000)

    print(f"Size: {size:6}, Best: {best_times[-1]:7.2f} ms, "
          f"Worst: {worst_times[-1]:7.2f} ms, Avg: {avg_times[-1]:7.2f} ms")

# Theoretical n log n curve for comparison
n_log_n = [size * math.log2(size) for size in input_sizes]
scale = avg_times[-1] / n_log_n[-1]
n_log_n_scaled = [x * scale for x in n_log_n]

# Plotting results
plt.figure(figsize=(12, 6))
plt.plot(input_sizes, best_times, label='Best Case (Sorted)', linestyle='-')
plt.plot(input_sizes, avg_times, label='Average Case (Random)', linestyle='--')
plt.plot(input_sizes, worst_times, label='Worst Case (Reverse)', linestyle=':')
plt.plot(input_sizes, n_log_n_scaled, label='Theoretical O(n log n)', linestyle='-.')

plt.title('Heap Sort Performance Analysis')
plt.xlabel('Input Size (n)')
plt.ylabel('Execution Time (ms)')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()
