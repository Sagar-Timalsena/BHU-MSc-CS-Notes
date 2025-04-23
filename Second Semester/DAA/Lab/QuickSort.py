import matplotlib.pyplot as plt
import random
import math

def quicksort(arr, counter):
    """Recursive QuickSort implementation with comparison counter."""
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left, right = [], []
    for x in arr[1:]:
        counter[0] += 1
        if x < pivot:
            left.append(x)
        else:
            right.append(x)
    return quicksort(left, counter) + [pivot] + quicksort(right, counter)

def run_quicksort_with_counter(n):
    """Generates random data and returns number of comparisons for QuickSort."""
    arr = random.sample(range(n * 2), n)
    counter = [0]
    quicksort(arr, counter)
    return counter[0]

# Generate data
sizes = list(range(1, 101))
qs_steps = [run_quicksort_with_counter(n) for n in sizes]
n_log_n = [n * math.log2(n) for n in sizes]
n_squared = [n ** 2 for n in sizes]

# Plot both graphs side by side
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

# Plot 1: QuickSort vs n log n
ax1.plot(sizes, qs_steps, label='QuickSort Steps', color='blue')
ax1.plot(sizes, n_log_n, label='n log n', color='red', linestyle='--')
ax1.set_title('QuickSort Steps vs n log n')
ax1.set_xlabel('Input Size (n)')
ax1.set_ylabel('Number of Comparisons')
ax1.legend()
ax1.grid(True)

# Plot 2: QuickSort vs n^2
ax2.plot(sizes, qs_steps, label='QuickSort Steps', color='blue')
ax2.plot(sizes, n_squared, label='n² (Worst Case)', color='green', linestyle=':')
ax2.set_title('QuickSort Steps vs n²')
ax2.set_xlabel('Input Size (n)')
ax2.set_ylabel('Number of Comparisons')
ax2.legend()
ax2.grid(True)

plt.tight_layout()
plt.show()
