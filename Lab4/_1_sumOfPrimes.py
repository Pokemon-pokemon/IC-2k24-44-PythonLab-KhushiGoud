import time

def sum_primes_sieve(N):
    if N <= 2:
        return 0
    if N == 3:
        return 2

    size = N // 2
    is_prime = [True] * size
    is_prime[0] = False

    limit = int(N**0.5) // 2
    for i in range(1, limit + 1):
        if is_prime[i]:
            val = 2 * i + 1
            start_idx = (val * val) // 2
            is_prime[start_idx : size : val] = [False] * len(range(start_idx, size, val))

    return 2 + sum(2 * i + 1 for i in range(1, size) if is_prime[i])

N = int(input("Enter N: "))
start = time.time()
result = sum_primes_sieve(N)

print("Sum of primes:", result)
print("Time taken:", time.time() - start)