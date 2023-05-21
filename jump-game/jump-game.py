class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True

        currPos = 0
        maxPos = nums[0]
        
        while maxPos and currPos <= maxPos:
           maxPos = max(maxPos, currPos + nums[currPos])
           currPos +=1
           if maxPos >= len(nums) - 1:
               return True

        return False
