from typing import List

class Binary_Search:
    def __init__(self):
        self.nums = list(range(1, 10_000_000))
        self.target = 3
        
    def search_insert_index(self, target: int = None, nums: List[int] = None) -> int:
        if nums is None:
            nums = self.nums
        if target is None:
            target = self.target

        low = 0
        high = len(nums) - 1
        
        while low <= high:
            mid = (low + high) // 2
            curr = nums[mid]          
            if curr < target:
                low = mid + 1
            elif curr > target:
                high = mid - 1
            else:
                return mid
        return low


if __name__ == "__main__":
    instance = Binary_Search()
    print(instance.search_insert_index(target=6))  # Output: 5
    nums = list(range(0, 10))
    print(instance.search_insert_index(target=112, nums=nums))  # Output: 10
