import matplotlib.pyplot as plt
import random

#Global Variable
steps = 0

def insertionSort(lst): 
    global steps
    for i in range(1,len(lst)):
        key = lst[i]
        j = i-1
        while(j>=0 and lst[j]>key):
            steps+=1
            lst[j+1] = lst[j]
            j = j-1
        lst[j+1] = key
    return lst

def run_insertionSort(n):
    global steps
    steps = 0
    arr = random.sample(range(2*n),n)
    insertionSort(arr)
    return steps

sizes = [x for x in range(1,1001)]
is_steps = [run_insertionSort(x) for x in sizes]
n_squared = [x**2 for x in sizes]

plt.plot(sizes,is_steps,label='Insertion Sort',color='purple')
plt.plot(sizes,n_squared,label='n^2',color='red',linestyle='dashed')
plt.grid(True)
plt.show()
