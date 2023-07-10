class In_Place:
    def __init__(self, nums: list = [1,2,3,4,5], replacements: list = [10,20,30], r_loc : int = 1) -> None:
        self.nums = nums
        self.replacements = replacements
        # self.r_loc = r_loc
        self.r_loc_start = r_loc
        self.r_loc_end = r_loc + len(replacements)
        
    
    def slice_assignment(self):
        id_before_insert = id(self.nums)
        print (f"{self.nums} is at {id_before_insert}")
        
        # nums[start:stop] = replacements 
        self.nums[self.r_loc_start:self.r_loc_end] = self.replacements
        
        id_after_insert = id(self.nums)
        print (f"{self.nums} is at {id_after_insert}")
        print(f"since these numbers are the same, it indicates the replacement was done in place")
        print(f"{id_before_insert}\n{id_after_insert}")
        
        
        
if __name__ == "__main__":
    instance = In_Place()
    instance.slice_assignment()
    instance_2 = In_Place(nums=[1,2], r_loc=1, replacements=[10,20,30])
    instance_2.slice_assignment()
