class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        pointer = 0
        while pointer < len(nums):
            if nums[pointer] <= 0 or nums[pointer] > len(nums) or nums[pointer] == pointer + 1:
                pointer += 1
            else:
                left, right = pointer, nums[pointer] - 1
                if right + 1 == nums[right]:
                    nums[left] = -1
                    pointer += 1
                    continue
                nums[left], nums[right] = nums[right], nums[left]
        
        for i, num in enumerate(nums):
            if num != i + 1:
                return i + 1
        
        return len(nums) + 1

        