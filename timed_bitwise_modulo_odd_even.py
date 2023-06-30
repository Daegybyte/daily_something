# !/usr/bin/env python3
import timeit
import statistics

class Timed_Odd_Even:
    range_number = 100_000_000
    nums = range(-range_number, range_number)
    
    def __init__(cls, nums) -> None:
       cls.nums = nums
    
    @classmethod
    def bit_odd_even(cls):
        times = []
        for num in cls.nums:
            t = timeit.timeit(lambda: num & 1 != 0, number=1) 
            times.append(t)
        return statistics.mean(times)
    
    @classmethod
    def modulo_odd_even(cls):
        times = []
        for num in cls.nums:
            t = timeit.timeit(lambda: num % 2 == 0, number=1)
            times.append(t)
        return statistics.mean(times)
            
    def warmup():
        i = 100_000_000
        while i != 0:
            i = i - 1

if __name__ == "__main__":
    
    Timed_Odd_Even.warmup()
    time_from_bitwise = Timed_Odd_Even.bit_odd_even()
    time_from_modulo = Timed_Odd_Even.modulo_odd_even()
    print(f"bitwise: {time_from_bitwise}\nmodulo: {time_from_modulo}")
    
    '''
    Results:
    bitwise: 3.387022477137342e-07
    modulo: 1.2299952507019042e-07
    '''