import random
import time
import matplotlib.pyplot as plt

def counting_sort(numbers):
    if not numbers:
        return numbers.copy()
    small = min(numbers)
    large = max(numbers)
    counts = [0] * (large - small + 1)
    for num in numbers:
        counts[num - small] += 1
    result = []
    for i in range(len(counts)):
        result.extend([i + small] * counts[i])
    return result

# Test sizes
sizes = [1000, 5000, 10000, 15000, 20000]
results = {'Best': [], 'Average': [], 'Worst': []}

# Generate test data
def make_best(size):
    return [random.randint(0, 100) for x in range(size)]

def make_avg(size):
    return [random.randint(0, size) for x in range(size)]

def make_worst(size):
    return [random.randint(0, 100000) for x in range(size)]

# Run tests
for size in sizes:
    # Best case (small range)
    data = make_best(size)
    start = time.time()
    counting_sort(data)
    results['Best'].append((time.time() - start) * 1000)

    # Average case
    data = make_avg(size)
    start = time.time()
    counting_sort(data)
    results['Average'].append((time.time() - start) * 1000)

    # Worst case (large range)
    data = make_worst(size)
    start = time.time()
    counting_sort(data)
    results['Worst'].append((time.time() - start) * 1000)

# Calculate theoretical curves (scaled to match)
scale_n = results['Best'][-1] / sizes[-1]
scale_n2 = results['Worst'][-1] / (sizes[-1] ** 2)
theory_n = [size * scale_n for size in sizes]
theory_n2 = [(size ** 2) * scale_n2 for size in sizes]

# Plot results
plt.figure(figsize=(8, 5))
plt.plot(sizes, results['Best'], '-', label='Counting Sort Best (k=100)')
plt.plot(sizes, results['Average'], '--', label='Counting Sort Average')
plt.plot(sizes, results['Worst'], ':', label='Counting Sort Worst (k=100K)')
plt.plot(sizes, theory_n, '-.', label='Theoretical O(n)')
plt.plot(sizes, theory_n2, '-.', label='Theoretical O(n²)')
plt.title('Counting Sort vs Theoretical Complexities')
plt.xlabel('Input Size')
plt.ylabel('Time (ms)')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()