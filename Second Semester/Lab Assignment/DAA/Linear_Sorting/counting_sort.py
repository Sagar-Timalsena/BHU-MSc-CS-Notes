import random
import matplotlib.pyplot as plt

steps = 0

#k represents the range of the elements in the array
def countingSort(arr, k):
    global steps
    count = [0 for _ in range(k+1)]
    result = [-1 for _ in range(len(arr))]

    #Counting no. of times each element appears in the array
    for j in range(len(arr)):
        steps+=1
        count[arr[j]] += 1

    #Counting no of values less than or equal current element
    for i in range(1,len(count)):
        steps+=1
        count[i]+=count[i-1]

    #Placing the elements accordingly into the result array
    for j in range(len(arr)-1,-1,-1):
        steps+=1
        result[count[arr[j]]-1] = arr[j]
        count[arr[j]] -= 1
    return result

def run_counting_sort(n):
    global steps
    lst = random.sample(range(2*n))
    countingSort(lst)
    return steps
    
#Hyper-parameters
sampleSize = 1000

n_values = [n for n in range(1,sampleSize+1)]
bs_steps = [run_bucket_sort(n) for n in n_values]
linear_n = [n for n in n_values]
three_linear_n = [3*n for n in n_values]

n_squared = [n**2 for n in n_values]

plt.plot(n_values,bs_steps,label='Bucket Sort',color='purple')
plt.plot(n_values,linear_n,label='n',color='black',linestyle='dashed')
plt.plot(n_values,three_linear_n,label='3n',color='red',linestyle='dashed')

plt.xlabel("Input Size (n)")
plt.ylabel("No of Steps")
plt.grid(True)
plt.legend()
plt.show()