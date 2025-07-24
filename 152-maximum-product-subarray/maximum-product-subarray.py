import math

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        has_zero = False

        def getMaxProduct(i, j):
            print(i, j, nums[i:j])
            if not j - i:
                return 0
            
            result = nums[i]
            forward_pass_prod = 1
            for idx in range(i, j):
                forward_pass_prod *= nums[idx]
                result = max(result, forward_pass_prod)
            
            back_pass_prod = 1
            for idx in range(j-1, i-1, -1):
                back_pass_prod *= nums[idx]
                result = max(result, back_pass_prod)
            
            return result


            
        
        left = 0
        result = nums[0]
        for right, num in enumerate(nums):
            if num == 0:
                has_zero = True
                result = max(result, getMaxProduct(left, right))
                left = right + 1
            elif right == len(nums) - 1:
                result = max(result, getMaxProduct(left, right + 1))
        
        return 0 if result < 0 and has_zero else result
            
            
        