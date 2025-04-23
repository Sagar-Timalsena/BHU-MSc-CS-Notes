import matplotlib.pyplot as plt
import random

def bubble_sort(arr):
    """Bubble Sort with comparison counter."""
    count = 0
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            count += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return count

def run_bubble_sort_tests(max_size):
    """Run Bubble Sort for array sizes from 1 to max_size and collect comparison counts."""
    sizes = list(range(1, max_size + 1))
    comparisons = []

    for n in sizes:
        arr = [random.randint(1, 100) for _ in range(n)]
        comparisons.append(bubble_sort(arr))

    return sizes, comparisons

# Run and plot
max_size = 1000
x_values, count_values = run_bubble_sort_tests(max_size)
n_squared = [n ** 2 for n in x_values]

plt.figure(figsize=(10, 5))
plt.plot(x_values, count_values, label='Bubble Sort Steps', color='blue')
plt.plot(x_values, n_squared, label='O(n²)', color='green', linestyle='--')
plt.xlabel('Array Size (n)')
plt.ylabel('Number of Comparisons')
plt.title('Bubble Sort Steps vs O(n²)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()