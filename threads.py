from threading import Thread
from time import sleep

class My_Thread_Exp:   
    
    def __init__(self, style: str, ttb: int, tmp_in_c: int) -> None: #ttb == time to brew
        self.style = style
        self.ttb = ttb
        self.tmp = tmp_in_c
        self.t1 = None
        self.t2 = None
    
    def grind_coffee(self):
        print(f"grinding beans.")
        sleep(2)
        print(f"beans are done!")
    
    def heat_water(self):
        print(f"heating water to {self.tmp}°c.")
        sleep(5)
        print(f"water heated!")
        
    def brew(self):
        print(f"brewing {self.style} for {self.ttb} minutes")
        sleep(self.ttb)
        print(f"Your coffee is ready. Enjoy!")

if __name__ == "__main__":
    morning_joe = My_Thread_Exp(style="French Press", ttb=5, tmp_in_c=93)
    
    t1 = Thread(target=morning_joe.grind_coffee)
    t1.start()

    t2 = Thread(target=morning_joe.heat_water)
    t2.start()
    
    # Threads must be joined before moving onto the next step.
    # You can't brew until the beans are ground AND the water is heated
    t1.join()
    t2.join()

    morning_joe.brew()
    