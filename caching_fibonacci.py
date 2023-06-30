# !/usr/bin/env python3
from functools import lru_cache

class Caching_Fib_Recursive:
    @classmethod
    @lru_cache(maxsize=None)
    def fib(cls, n):
        if n <= 1:
            return n
        else:
            return cls.fib(n - 1) + cls.fib(n - 2)
        
    @classmethod
    def print_fib(cls, n):
        for i in range(n):
            print(cls.fib(i), sep="\n")
    
if __name__ == "__main__":
    # res = Cache_Fib_Recursive.fib(10)
    Caching_Fib_Recursive.print_fib(100)