class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)<3:
            return len(nums)
        
        s = e = 2
        
        while e<len(nums):
            if nums[e] != nums[s-2]:
                nums[s] = nums[e]
                s+=1
            e+=1
        
        return s
        