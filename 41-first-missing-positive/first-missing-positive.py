class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        pointer = 0
        while pointer < len(nums):
            # print("Pointer -> ", pointer)
            if nums[pointer] <= 0 or nums[pointer] > len(nums):
                nums[pointer] = -1
                pointer += 1
            elif nums[pointer] == pointer + 1:
                pointer += 1
            else:
                left, right = pointer, nums[pointer] - 1
                # print(f'Swap {left}:{nums[left]} \twith {right}:{nums[right]}')
                if right + 1 == nums[right]:
                    nums[left] = -1
                    pointer += 1
                    continue
                nums[left], nums[right] = nums[right], nums[left]

            # print(pointer, nums)
        
        for i, num in enumerate(nums):
            if num == -1:
                return i + 1
        
        return len(nums) + 1

        