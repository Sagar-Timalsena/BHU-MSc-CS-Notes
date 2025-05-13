import matplotlib.pyplot as plt
import random
import math

def bubbleSort(lst):
    count = 0
    for i in range(len(lst) - 1):
        for j in range(0, len(lst) - i - 1):
            count+=1
            if lst[j] > lst[j + 1]:  # Correct comparison
                lst[j], lst[j + 1] = lst[j + 1], lst[j]  # Swap
    return count

size = 1000

count_values = []
x_values = []

for i in range(1,size+1):
    arr = [ random.randint(1,100) for _ in range(1,i+1)]
    count = bubbleSort(arr)
    x_values.append(i)
    count_values.append(count)

n_squared = [n**2 for n in range(1,size+1)]

plt.plot(x_values, count_values, label='Bubble Sort',color='blue')
plt.plot(x_values, n_squared, label='O(n^2)',color='green')
plt.xlabel('Array Size')
plt.ylabel('Number of Comparisons')
plt.title('Bubble Sort vs. O(n^2)')
plt.legend()
plt.grid(True)
plt.show()