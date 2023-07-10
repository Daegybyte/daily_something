class In_Place:
    def __init__(self, nums: list = [1,2,3,4,5], replacements: list = [10,20,30], r_loc : int = 1) -> None:
        self.nums = nums
        self.replacements = replacements
        self.r_loc_start = r_loc
        self.r_loc_end = len(replacements)
        
    
    def slice_assignment(self):
        id_before_insert = id(self.nums)
        print (f"{self.nums} is at {id_before_insert} and will be replaced with\n{self.replacements} starting at index {self.r_loc_start} and ending at {self.r_loc_end}")
        
        # nums[start:stop] = replacements 
        self.nums[self.r_loc_start:self.r_loc_end] = self.replacements
        
        id_after_insert = id(self.nums)
        print (f"{self.nums} is at {id_after_insert}\n")
        print(f"since these numbers are the same, it indicates the replacement was done in place")
        print(f"{id_before_insert}\n{id_after_insert}\n-----------------------------------")
        
        
        
if __name__ == "__main__":
    instance = In_Place()
    instance.slice_assignment()
    instance= In_Place(nums=[1,2], r_loc=1, replacements=[10,20,30])
    instance.slice_assignment()