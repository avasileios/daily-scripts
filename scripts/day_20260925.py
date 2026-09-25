"""Daily experiment: memoized fibonacci"""
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    return n if n < 2 else fib(n - 1) + fib(n - 2)

if __name__ == "__main__":
    for n in range(24, 32):
        print(f"fib({n}) = {fib(n)}")
