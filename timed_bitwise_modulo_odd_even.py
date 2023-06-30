# !/usr/bin/env python3
import timeit

class Timed_Odd_Even:
    ITERS = 100_000_000
    
    def __init__(cls, ITERS) -> None:
       cls.ITERS = ITERS
    
    @classmethod
    def bit_odd_even(cls):
        t = timeit.timeit(lambda: 2 & 1 == 0, number=cls.ITERS) # 010 & 001 = 000
        return t
    
    @classmethod
    def modulo_odd_even(cls):
        t = timeit.timeit(lambda: 2 % 2 == 0, number=cls.ITERS)
        return t
            
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