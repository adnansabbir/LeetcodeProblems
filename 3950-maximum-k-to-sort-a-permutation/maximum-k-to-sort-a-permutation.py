class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        ans = (1 << (len(nums).bit_length() + 2)) - 1
        print(ans)
        for i in range(len(nums)):
            if nums[i] != i:
                if ans == None:
                    ans = i 
                else:
                    ans = (ans & i) & nums[i]

                if ans == 0:
                    return 0
        return 0 if ans > len(nums) else ans
        