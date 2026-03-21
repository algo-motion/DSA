import time

import numpy as np


def bubble_sort(arr):
    flag = True
    while flag:
        flag = False
        i=0
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                flag = True
        i += 1
    return arr

# Example usage
if __name__ == "__main__":
    #arr = np.random.randint(0, 100, size=10000) # Random array of 10,000 integers
    arr = np.arange(10000, 0, -1)  # Worst case for bubble sort
    #arr = np.arange(10000)  # Best case for bubble sort
    start_time = time.time()
    sorted_arr = bubble_sort(arr)
    end_time = time.time()
    print(f"Bubble sort execution time: {end_time - start_time} seconds")
    start_time = time.time()
    sorted_arr = np.sort(arr)
    end_time = time.time()
    print(f"NumPy sort execution time: {end_time - start_time} seconds")