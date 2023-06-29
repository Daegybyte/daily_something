class Fizz_Buzz:
    def __init__(self, n):
        self.n = n + 1
    
    def doit(self):
        for i in range(1, self.n):
            if i % 15 == 0:
                print(f"{i} fizz buzz")
            elif i % 3 == 0:
                print(f"{i} fizz")
            elif i % 5 == 0:
                print(f"{i} buzz")
            else:
                print(f"{i}") 
                
if __name__ == "__main__":
    fb = Fizz_Buzz(20)
    fb.doit()