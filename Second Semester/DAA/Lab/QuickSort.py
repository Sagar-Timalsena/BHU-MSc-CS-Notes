import time
import random
import matplotlib.pyplot as plt

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)

input_sizes = [100, 200, 300, 500, 1000]  
times = []

for size in input_sizes:
    arr = [random.randint(0, 10000) for _ in range(size)]
    start_time = time.time()
    quick_sort(arr)
    end_time = time.time()
    times.append(end_time - start_time)

# Plot the results
plt.plot(input_sizes, times, marker='o', linestyle='-', color='b')
plt.xlabel("Input Size")
plt.ylabel("Time (seconds)")
plt.title("Quick Sort: Input Size vs Execution Time")
plt.grid()
plt.show()

print("Hello Saagar")