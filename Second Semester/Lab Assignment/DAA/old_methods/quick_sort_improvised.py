import random
import time
import math
import matplotlib.pyplot as plt
import statistics

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[-1]
    left = [x for x in arr[:-1] if x < pivot]
    right = [x for x in arr[:-1] if x >= pivot]
    return quicksort(left) + [pivot] + quicksort(right)

# Hyper-parameters
size = 1000
repeats = 5  # Average over 5 runs per input size

x_values = []
time_taken = []

# Measure average time for each input size
for i in range(1, size+1):
    times = []
    for _ in range(repeats):
        arr = [random.randint(1, size) for _ in range(i)]
        start = time.time()
        quicksort(arr)
        end = time.time()
        times.append(end - start)
    avg_time = statistics.mean(times)
    x_values.append(i)
    time_taken.append(avg_time)

# Compute theoretical curves
nlogn = [n * math.log2(n) for n in x_values]
n_squared = [n ** 2 for n in x_values]

scale_nlogn = 3e-7   # Slightly higher to match quicksort better
scale_n_squared = 1e-8  # Much lower to avoid dominating

scaled_nlogn = [y * scale_nlogn for y in nlogn]
scaled_n_squared = [y * scale_n_squared for y in n_squared]
time_taken = []

# Measure average time for each input size

# Plot all curves
plt.plot(x_values, time_taken, label="Quicksort Time", color="blue")
plt.plot(x_values, scaled_nlogn, label="n log n (scaled)", color="green")
plt.plot(x_values, scaled_n_squared, label="n² (scaled)", color="red")

plt.xlabel("n (input size)")
plt.ylabel("Time (seconds)")
plt.title("Quicksort Time vs. Theoretical Curves")
plt.legend()
plt.grid(True)
plt.show()
