import time

import numpy as np


def bubble_sort(arr):
    flag = True
    i = 0
    while flag:
        flag = False
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                flag = True
        i += 1
    return arr


def benchmark_bubble_sort(size=10000, seed=42):
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
        bubble_sort(arr_copy)
        end_time = time.time()
        elapsed = end_time - start_time
        timings[case_name] = elapsed
        print(f"{case_name.title()} case ({size} elements): {elapsed:.6f} seconds")

    return timings


if __name__ == "__main__":
    benchmark_bubble_sort(size=10000)