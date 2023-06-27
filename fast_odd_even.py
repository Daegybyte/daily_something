# !/usr/bin/env python3

class Sandbox:
  def doit():
    nums = [num for num in range(-20,20)]
    for num in nums:
      if num == 0:
        # print(f"{num} is special")
        continue
      if num & 1:
        assert(num % 2 == 1)
        # print(f"{num} is odd")
      else:
        assert(num % 2 == 0)
        # print(f"{num} is even")
    
    print(f"finished checking {len(nums)} numbers")

if __name__ == "__main__":
  s = Sandbox
  s.doit()
