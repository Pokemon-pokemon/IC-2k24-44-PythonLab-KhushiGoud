import time
import random

def count_pairs_optimized(arr, target):

    freq = {}
    count = 0

    for x in arr:

        complement = target - x

        if complement in freq:
            count += freq[complement]

        freq[x] = freq.get(x, 0) + 1

    return count


random.seed(42)

N = 50000
arr = [random.randint(1, 20000) for _ in range(N)]
target = 20000

start = time.time()

result = count_pairs_optimized(arr, target)

print("Pairs found:", result)
print("Time taken:", time.time() - start)