class NumArray:

    def __init__(self, nums: List[int]):
        self.num_array = [nums[0]]
        for i in range(1, len(nums)):
            self.num_array.append(self.num_array[i-1] + nums[i])
        

    def sumRange(self, left: int, right: int) -> int:
        if not left:
            return self.num_array[right]
        
        
        return self.num_array[right] - self.num_array[left-1]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)