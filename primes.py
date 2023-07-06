class Py_Primes:
    def __init__(self, nums: list = [1,2,3,4,5,6,7,8,9,10,11]) -> None:
        self.nums = nums
    
    def is_prime(self, num):
        # even numbers are not prime except for 2
        # This check speeds up the function
        if num % 2 == 0 and num != 2: 
            return False
        
        for x in range(2, num):
            if num % x == 0:
                return False
        return True
    

if __name__ == "__main__":
    inst = Py_Primes()
    
    # filter returns an iterator of those which return true, 
    # a list is needed because filter shows a filter object
    primes = list(filter(inst.is_prime, inst.nums))
    print(primes)
    
    nums = range(1, 1_000)
    inst = Py_Primes(nums = nums)
    primes = list(filter(inst.is_prime, nums))
    print(primes)