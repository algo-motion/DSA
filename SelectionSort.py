def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[min_index] > arr[j]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


def benchmark_selection_sort(size=10000, seed=42):
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
        selection_sort(arr_copy)
        end_time = time.time()
        elapsed = end_time - start_time
        timings[case_name] = elapsed
        print(f"{case_name.title()} case ({size} elements): {elapsed:.6f} seconds")

    return timings


if __name__ == "__main__":
    benchmark_selection_sort(size=10000)