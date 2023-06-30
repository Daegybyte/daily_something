# !/usr/bin/env python3
import time
import statistics

class Timed_Odd_Even:
    range_number = 100_000_000
    nums = range(-range_number, range_number)
    
    def __init__(self, nums) -> None:
       self.nums = nums
    
    @classmethod
    def bit_odd_even(self):
        t = []
        for num in self.nums:
            start = time.time()
            if num & 1:
                pass
            else:
                pass
            end = time.time()
            t.append(end - start)
        return statistics.mean(t)
    
    @classmethod
    def modulo_odd_even(self):
        t = []
        for num in self.nums:
            start = time.time()
            if num % 2 == 0:
                pass
            else:
                pass
            end = time.time()
            t.append(end - start)
        return statistics.mean(t)
            
    def warmup():
        i = 100_000_000
        while i != 0:
            i = i - 1

if __name__ == "__main__":
    
    Timed_Odd_Even.warmup()
    t1 = Timed_Odd_Even.bit_odd_even()
    t2 = Timed_Odd_Even.modulo_odd_even()
    print(f"bitwise: {t1}\nmodulo: {t2}")