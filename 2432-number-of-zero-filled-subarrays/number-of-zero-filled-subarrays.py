class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        zeros = 0
        result = 0
        for num in nums:
            if num == 0:
                zeros += 1
            else:
                result += (zeros * (zeros + 1))//2
                zeros = 0
            
        result += (zeros * (zeros + 1))//2
        return result