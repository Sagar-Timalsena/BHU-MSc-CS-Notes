import random
import time
import matplotlib.pyplot as plt

def bucket_sort(arr):
	num_buckets = 10
	max_val = max(arr)
	min_val = min(arr)
	bucket_range = (max_val - min_val + 1) / num_buckets
	buckets = []
	for bucket_index in range(num_buckets):
		buckets.append([])
	for num in arr:
		index = min(int((num - min_val) / bucket_range), num_buckets - 1)
		buckets[index].append(num)
	for bucket in buckets:
		bucket.sort()
	sorted_arr = []
	for bucket in buckets:
		for num in bucket:
			sorted_arr.append(num)
	return sorted_arr

# Input sizes
input_sizes = list(range(5000, 50001, 5000))

# Generate test cases
def generate_best_case(size):
	return [random.uniform(0, size) for number in range(size)]

def generate_average_case(size):
	return [random.randint(0, size) for number in range(size)]

def generate_worst_case(size):
	return [size // 2 for number in range(size)]

# Measure performance
best_times = []
avg_times = []
worst_times = []

for size in input_sizes:
	arr = generate_best_case(size)
	start = time.time()
	bucket_sort(arr)
	best_times.append((time.time() - start) * 1000)

	arr = generate_average_case(size)
	start = time.time()
	bucket_sort(arr)
	avg_times.append((time.time() - start) * 1000)

	arr = generate_worst_case(size)
	start = time.time()
	bucket_sort(arr)
	worst_times.append((time.time() - start) * 1000)

	print(f"Size: {size:5d}, Best: {best_times[-1]:6.2f} ms, Avg: {avg_times[-1]:6.2f} ms, Worst: {worst_times[-1]:6.2f} ms")

# Normalization
max_time = max(best_times + avg_times + worst_times)
max_n = max(input_sizes)
max_n_squared = max_n ** 2

# Plotting
plt.figure(figsize=(12, 6))
plt.plot(input_sizes, [t/max_time for t in best_times], 'g-', label="Best Case")
plt.plot(input_sizes, [t/max_time for t in avg_times], 'b--', label="Average Case")
plt.plot(input_sizes, [t/max_time for t in worst_times], 'r:', label="Worst Case")
plt.plot(input_sizes, [n/max_n for n in input_sizes], 'k-.', label="O(n)")
plt.plot(input_sizes, [(n**2)/max_n_squared for n in input_sizes], 'm-.', label="O(n²)")
plt.title("Bucket Sort Performance (Normalized)")
plt.xlabel("Input Size")
plt.ylabel("Normalized Time")
plt.legend()
plt.grid(True)
plt.show()