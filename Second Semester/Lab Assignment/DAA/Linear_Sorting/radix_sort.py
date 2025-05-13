# Function to perform counting sort based on the digit represented by exp (10^i)
def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n  # Output array to store sorted values
    count = [0] * 10  # Count array for digits (0-9)

    # Count occurrences of digits
    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1

    # Change count[i] to be the actual position of this digit in output[]
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build the output array
    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    # Copy the output array
    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    # Find the maximum number to know the number of digits
    max_num = max(arr)

    # Do counting sort for every digit. The exp is 10^i for current digit.
    exp = 1
    while max_num // exp > 0:
        counting_sort(arr, exp)
        exp *= 10

arr = [170, 45, 75, 90, 802, 24, 2, 66]
radix_sort(arr)
print("Sorted array:", arr)
