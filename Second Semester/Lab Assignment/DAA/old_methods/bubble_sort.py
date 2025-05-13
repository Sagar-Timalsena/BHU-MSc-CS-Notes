import time
import matplotlib.pyplot as plt
import random
import statistics

def bubbleSort(lst):
    for i in range(len(lst) - 1):  
        for j in range(0, len(lst) - i - 1):  
            if lst[j] > lst[j + 1]:  # Correct comparison
                lst[j], lst[j + 1] = lst[j + 1], lst[j]  # Swap
    return lst

#Hyper-parameters
size = 200
repeats = 5

time_elapsed = []
x_values = []
for i in range(1,size+1):
    times = []
    for _ in range(0,repeats):
        temp_list = [random.randint(1,1000) for _ in range(1,i+1)]
        start = time.time()
        bubbleSort(temp_list)
        end = time.time()
        times.append(end-start)
    avg_time = statistics.mean(times)    
    time_elapsed.append(avg_time)
    x_values.append(i)
    
y_squared = [i**2 for i in range(1,size+1)]
factor = max(time_elapsed)/max(y_squared)
y_squared_scaled = [y*factor for y in y_squared]

plt.plot(x_values,time_elapsed,label="Bubble Sort",color="blue")
plt.plot(x_values,y_squared_scaled,label="y=n^2",color="red")
plt.title("Quick Sort")
plt.xlabel("Input Size")
plt.ylabel("Time Elapsed (seconds) ")
plt.legend()
plt.grid(True)
plt.show()
