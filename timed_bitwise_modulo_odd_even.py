import timeit
import statistics

class Timed_Odd_Even:
    def __init__(self, NUMBER, REPS):
       self.num = NUMBER
       self.reps = REPS
    
    def bit_odd_even(self):
        t = timeit.repeat(lambda: 2 & 1 == 0, number=self.num, repeat=self.reps)  # 010 & 001 = 000
        return statistics.mean(t), min(t)
    
    def modulo_odd_even(self):
        t = timeit.repeat(lambda: 2 % 2 == 0, number=self.num, repeat=self.reps)  # 2 % 2 = 0        
        return statistics.mean(t), min(t)

    def warmup(self):
        i = 1_000_000_000
        while i != 0:
            i = i - 1
        

if __name__ == "__main__":
    NUMBER = 100_000
    REPS = 100_000
    
    instance = Timed_Odd_Even(NUMBER, REPS)
    instance.warmup()
    time_from_bitwise, min_bit = instance.bit_odd_even()
    time_from_modulo, min_mod = instance.modulo_odd_even()
    
    print(f"bitwise: {time_from_bitwise} min: {min_bit}\nmodulo: {time_from_modulo} min: {min_mod}")