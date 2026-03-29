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


def benchmark_insertion_sort(size=10000, seed=42):
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
        insertion_sort(arr_copy)
        end_time = time.time()
        elapsed = end_time - start_time
        timings[case_name] = elapsed
        print(f"{case_name.title()} case ({size} elements): {elapsed:.6f} seconds")

    return timings


if __name__ == "__main__":
    benchmark_insertion_sort(size=10000)