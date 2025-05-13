import matplotlib.pyplot as plt
import random
import math

# Counter to track number of comparisons
steps = 0

def quicksort(arr):
    global steps
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = []
    right = []
    for x in arr[1:]:
        steps += 1
        if x < pivot:
            left.append(x)
        else:
            right.append(x)
    return quicksort(left) + [pivot] + quicksort(right)

def run_quicksort_with_steps(n):
    global steps
    steps = 0
    arr = random.sample(range(n * 2), n)  # Unique random elements
    quicksort(arr)
    return steps

# Input sizes
sizes = list(range(1, 101))
qs_steps = [run_quicksort_with_steps(n) for n in sizes]
nlogn = [n * math.log2(n) for n in sizes]
n_squared = [n ** 2 for n in sizes]

# Plot 1: QuickSort Steps vs n log n
plt.figure(figsize=(10, 5))
plt.plot(sizes, qs_steps, label='QuickSort Steps (comparisons)', color='blue')
plt.plot(sizes, nlogn, label='n log n', color='red', linestyle='--')
plt.xlabel('Input Size (n)')
plt.ylabel('Number of Steps')
plt.title('QuickSort Steps vs n log n')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Plot 2: QuickSort Steps vs n^2
plt.figure(figsize=(10, 5))
plt.plot(sizes, qs_steps, label='QuickSort Steps (comparisons)', color='blue')
plt.plot(sizes, n_squared, label='n^2 (Worst Case)', color='green', linestyle=':')
plt.xlabel('Input Size (n)')
plt.ylabel('Number of Steps')
plt.title('QuickSort Steps vs n^2')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
