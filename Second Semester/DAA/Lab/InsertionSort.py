import matplotlib.pyplot as plt
import random

def insertion_sort(arr, counter):
    """Insertion Sort with comparison counter."""
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            counter[0] += 1
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def run_insertion_sort(n):
    """Run Insertion Sort and return number of comparisons."""
    arr = random.sample(range(2 * n), n)
    counter = [0]
    insertion_sort(arr, counter)
    return counter[0]

# Generate input sizes and step counts
sizes = list(range(1, 1001))
is_steps = [run_insertion_sort(n) for n in sizes]
n_squared = [n ** 2 for n in sizes]

# Plotting
plt.figure(figsize=(10, 5))
plt.plot(sizes, is_steps, label='Insertion Sort Steps', color='purple')
plt.plot(sizes, n_squared, label='n² (Theoretical Worst Case)', color='red', linestyle='--')
plt.xlabel('Input Size (n)')
plt.ylabel('Number of Comparisons')
plt.title('Insertion Sort Steps vs n²')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
