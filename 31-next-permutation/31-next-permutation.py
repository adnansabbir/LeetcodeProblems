class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        swapElementL = None
        smallest = []
        
        for i in reversed(range(len(nums)-1)):
            if nums[i] < nums[i+1]:
                swapElementL = i
                break
        
        if swapElementL == None:
            return nums.reverse()
        
        swapElementR = swapElementL + 1
        while swapElementR < len(nums)-1 and nums[swapElementR+1] > nums[swapElementL]:
            swapElementR +=1
        
        nums[swapElementR], nums[swapElementL] = nums[swapElementL], nums[swapElementR]
        nums[swapElementL+1:] = sorted(nums[swapElementL+1:])