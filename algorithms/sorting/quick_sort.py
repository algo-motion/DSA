def quick_sort(arr, left, right):
    if left >= right:
        return arr
    pivot_index = partition(arr, left, right)
    quick_sort(arr, left, pivot_index - 1) 
    quick_sort(arr, pivot_index + 1, right)
    return arr

def partition(arr, left, right):
    pivot = arr[(left + right)//2]
    i = left - 1
    j = right + 1
    while True:
        i += 1
        while arr[i] < pivot:
            i += 1
        j -= 1
        while arr[j] > pivot:
            j -= 1

        if(i >= j):
            return j
        
        arr[i], arr[j] = arr[j], arr[i]
    

def testcase1(arr):
    print (quick_sort(arr, 0, len(arr)-1))

def benchmark_quick_sort(size=10000, seed=42):
    import time
    import numpy as np

    np.random.seed(seed)
    cases = {
        "best": np.arange(size),
        "average": np.random.randint(0, size, size=size),
        "worst": np.arange(size, 0, -1),
    }

    timings = {}
    for case_name, case_arr in cases.items():
        arr_copy = case_arr.copy()
        start_time = time.time()
        quick_sort(arr_copy, 0, len(arr_copy) - 1 )
        end_time = time.time()
        elapsed = end_time - start_time
        timings[case_name] = elapsed
        print(f"{case_name.title()} case ({size} elements): {elapsed:.6f} seconds")

    return timings

if __name__ == "__main__":
    testcase1([1,2,6,3,7])
    benchmark_quick_sort(size=10000)