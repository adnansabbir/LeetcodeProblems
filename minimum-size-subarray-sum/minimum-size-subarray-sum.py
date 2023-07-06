import sys

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        result, start, total = sys.maxsize, 0, 0
        
        for i, num in enumerate(nums):
            total += num
            
            while start <= i and total >= target:
                result = min(result, i - start + 1)
                total -= nums[start]
                start +=1
        
        return 0 if result == sys.maxsize else result
        