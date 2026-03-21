import time

import numpy as np

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Example usage
if __name__ == "__main__":
    #arr = np.random.randint(0, 100, size=10000) # Random array of 10,000 integers
    #arr = np.arange(10000, 0, -1)  # Worst case for insertion sort
    arr = np.arange(10000)  # Best case for insertion sort
    start_time = time.time()
    sorted_arr = insertion_sort(arr)
    end_time = time.time()
    print(f"Insertion sort execution time: {end_time - start_time} seconds")
    start_time = time.time()
    sorted_arr = np.sort(arr)
    end_time = time.time()
    print(f"NumPy sort execution time: {end_time - start_time} seconds")