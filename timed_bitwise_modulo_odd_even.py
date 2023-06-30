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
        T = []
        for num in self.nums:
            start = time.time()
            if num & 1:
                pass
            else:
                pass
            end = time.time()
            T.append(end - start)
        return statistics.mean(T)
    
    @classmethod
    def modulo_odd_even(self):
        T = []
        for num in self.nums:
            start = time.time()
            if num % 2 == 0:
                pass
            else:
                pass
            end = time.time()
            T.append(end - start)
        return statistics.mean(T)
            
    def warmup():
        i = 100_000_000
        while i != 0:
            i = i - 1

if __name__ == "__main__":
    
    Timed_Odd_Even.warmup()
    time_from_bitwise = Timed_Odd_Even.bit_odd_even()
    time_from_modulo = Timed_Odd_Even.modulo_odd_even()
    print(f"bitwise: {time_from_bitwise}\nmodulo: {time_from_modulo}")