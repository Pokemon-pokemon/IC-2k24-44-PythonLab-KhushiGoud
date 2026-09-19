import time
import random


def count_pairs_le(arr, value):

    count = 0
    left = 0
    right = len(arr) - 1

    while left < right:

        if arr[left] + arr[right] <= value:

            count += right - left
            left += 1

        else:
            right -= 1

    return count


def kth_smallest_optimized(arr, K):

    arr.sort()

    low = arr[0] + arr[1]
    high = arr[-1] + arr[-2]

    while low < high:

        mid = (low + high) // 2

        if count_pairs_le(arr, mid) >= K:
            high = mid

        else:
            low = mid + 1

    return low


random.seed(42)

N = 5000
arr = [random.randint(1, 100000) for _ in range(N)]
K = 1000000

start = time.time()

result = kth_smallest_optimized(arr, K)

print("K-th smallest pairwise sum:", result)
print("Time taken:", time.time() - start)