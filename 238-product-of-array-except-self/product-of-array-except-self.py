class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeroCount = 0

        product = 1
        for num in nums:
            if num == 0:
                zeroCount += 1
                if zeroCount >= 2:
                    break
            else:
                product *= num

        if zeroCount == 0:
            return [product//num for num in nums]
        elif zeroCount == 1:
            return [0 if num != 0 else product for num in nums]
        else:
            return [0] * len(nums)
        