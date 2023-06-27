# !/usr/bin/env python3

class Sandbox:
  def doit():
    nums = [num for num in range(0,1_000)]
    for num in nums:
      if num is 0:
        print(f"{num} is special")
        continue
      if num & 1:
        print(f"{num} is odd")
      else:
        print(f"{num} is even")

if __name__ == "__main__":
  s = Sandbox
  s.doit()
