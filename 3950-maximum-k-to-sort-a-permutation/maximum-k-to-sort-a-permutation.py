class Solution:
    def sortPermutation(self, nums: List[int]) -> int:

        # 3 = 11
        # 2 = 10
        # 1 = 01
        # 0 = 00
        ans = None
        for i in range(len(nums)):
            if nums[i] != i:
                if ans == None:
                    ans = i 
                else:
                    ans = (ans & i) & nums[i]
        return 0 if ans == None else ans
        