import matplotlib.pyplot as plt
import random
import math

# MergeSort with step counting
steps = 0

def mergesort(arr):
    global steps
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = mergesort(arr[:mid])
    right = mergesort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    global steps
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        steps += 1
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

def run_mergesort_with_steps(n):
    global steps
    steps = 0
    arr = random.sample(range(n * 2), n)
    mergesort(arr)
    return steps

# Input sizes
sizes = list(range(1, 1001))
ms_steps = [run_mergesort_with_steps(n) for n in sizes]
nlogn = [n * math.log2(n) for n in sizes]
n_squared = [n ** 2 for n in sizes]

# Plot 1: MergeSort Steps vs n log n
plt.figure(figsize=(10, 5))
plt.plot(sizes, ms_steps, label='MergeSort Steps (comparisons)', color='purple')
plt.plot(sizes, nlogn, label='n log n', color='red', linestyle='--')
plt.xlabel('Input Size (n)')
plt.ylabel('Number of Steps')
plt.title('MergeSort Steps vs n log n')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Plot 2: MergeSort Steps vs n^2
plt.figure(figsize=(10, 5))
plt.plot(sizes, ms_steps, label='MergeSort Steps (comparisons)', color='purple')
plt.plot(sizes, n_squared, label='n^2 (Worst Case)', color='green', linestyle=':')
plt.xlabel('Input Size (n)')
plt.ylabel('Number of Steps')
plt.title('MergeSort Steps vs n^2')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
