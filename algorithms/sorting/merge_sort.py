def merge_sort(arr):
    arr_len = len(arr)
    if arr_len == 1:
        return arr
    mid = arr_len // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    left_index = right_index = 0
    merged = []
    while left_index < len(left_half) and right_index < len(right_half):
        if left_half[left_index] < right_half[right_index]:
            merged.append(left_half[left_index])
            left_index += 1
        else:
            merged.append(right_half[right_index])
            right_index += 1
    merged.extend(left_half[left_index:])
    merged.extend(right_half[right_index:])
    return merged


def benchmark_merge_sort(size=10000, seed=42):
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
        merge_sort(arr_copy)
        end_time = time.time()
        elapsed = end_time - start_time
        timings[case_name] = elapsed
        print(f"{case_name.title()} case ({size} elements): {elapsed:.6f} seconds")

    return timings


if __name__ == "__main__":
    benchmark_merge_sort(size=10000)