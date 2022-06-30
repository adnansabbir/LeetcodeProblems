class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        target = nums[len(nums)//2]
        result = 0
        for num in nums:
            result += abs(target - num)
            
        return result
        