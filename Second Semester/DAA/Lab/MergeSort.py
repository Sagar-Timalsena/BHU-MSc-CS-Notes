import matplotlib.pyplot as plt
import random
import math

def mergesort(arr, counter):
    """Performs MergeSort and counts comparison steps."""
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = mergesort(arr[:mid], counter)
    right = mergesort(arr[mid:], counter)
    return merge(left, right, counter)

def merge(left, right, counter):
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        counter[0] += 1
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

def run_mergesort_with_counter(n):
    arr = random.sample(range(n * 2), n)  #  generate random number
    counter = [0]
    mergesort(arr, counter)
    return counter[0]

# Main execution
sizes = list(range(1, 1001))
ms_steps = [run_mergesort_with_counter(n) for n in sizes]
n_log_n = [n * math.log2(n) for n in sizes]
n_squared = [n ** 2 for n in sizes]

# Plot both comparisons side by side
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 5))

# Plot 1: MergeSort vs n log n
ax1.plot(sizes, ms_steps, label='MergeSort Steps', color='purple')
ax1.plot(sizes, n_log_n, label='n log n', color='red', linestyle='--')
ax1.set_title('MergeSort Steps vs n log n')
ax1.set_xlabel('Input Size (n)')
ax1.set_ylabel('Number of Comparisons')
ax1.legend()
ax1.grid(True)

# Plot 2: MergeSort vs n^2
ax2.plot(sizes, ms_steps, label='MergeSort Steps', color='purple')
ax2.plot(sizes, n_squared, label='n^2 (Worst Case)', color='green', linestyle=':')
ax2.set_title('MergeSort Steps vs n^2')
ax2.set_xlabel('Input Size (n)')
ax2.set_ylabel('Number of Comparisons')
ax2.legend()
ax2.grid(True)

plt.tight_layout()
plt.show()
