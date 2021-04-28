import functools, sys
sys.setrecursionlimit(10000)

@functools.lru_cache(maxsize=None)
def fibonacci_recursive(n):
    # Base case
    if n == 0:
        return 0 
    elif n==1:
        return 1
    # Recursive case
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

print(fibonacci_recursive(4999))