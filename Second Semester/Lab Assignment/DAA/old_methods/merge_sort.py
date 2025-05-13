import random
import matplotlib.pyplot as plt
import time
import math
import statistics

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2  #Find the middle index
    left_half = merge_sort(arr[:mid]) #Recursively sort the left half
    right_half = merge_sort(arr[mid:]) #Recursively sort the right half

    return merge(left_half, right_half)

def merge(left, right):
    sorted_list = []
    i = j = 0

    # Merge two sorted lists
    while i < len(left) and j < len(right):
        if left[i] < right[j]:  
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1

    # Append any remaining elements from both lists
    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])

    return sorted_list

#Hyper-parameters
size = 1000
repeats = 5

time_elapsed = []
x_values = []
for i in range(1,size+1):
    times = []
    for _ in range(0,repeats):
        temp_list = [random.randint(1,1000) for _ in range(1,i+1)]
        start = time.time()
        merge_sort(temp_list)
        end = time.time()
        times.append(end-start)
    avg_time = statistics.mean(times)    
    time_elapsed.append(avg_time)
    x_values.append(i)
    
nlogn = [n*math.log2(n) for n in x_values]
factor = max(time_elapsed)/max(nlogn)
nlogn_scaled = [y*factor for y in nlogn]

plt.plot(x_values,time_elapsed,label="Merge Sort",color="blue")
plt.plot(x_values,nlogn_scaled,label="y=nlogn",color="red")
plt.title("Merge Sort")
plt.xlabel("Input Size")
plt.ylabel("Time Elapsed (seconds) ")
plt.legend()
plt.grid(True)
plt.show()
