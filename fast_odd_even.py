# !/usr/bin/env python3
from tqdm import tqdm  
from time import sleep
class Sandbox:
  def doit():
    nums = range(-100_000_000,100_000_000)
    progress_bar = tqdm(nums, desc="checking odds and evens", total=len(nums))

    for num in nums:
      if num & 1:
        assert(num % 2 == 1)
        # print(f"{num} is odd")
      else:
        assert(num % 2 == 0)
        # print(f"{num} is even")
      progress_bar.update()
  
    progress_bar.close()

if __name__ == "__main__":
  s = Sandbox
  s.doit()
