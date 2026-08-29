"""Daily experiment: prime sieve"""
def primes_up_to(n):
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False
    return [i for i, ok in enumerate(sieve) if ok]

if __name__ == "__main__":
    ps = primes_up_to(370)
    print(f"count: {len(ps)} primes, largest: {ps[-1]}")
    print(ps)
