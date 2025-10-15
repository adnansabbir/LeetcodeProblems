class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        if len(nums) < 4:
            return 1

        result = 1
        nums.append(None)
        # streak, streak_no, end_index
        last_streak = (1, 0, 0)
        streak = 1
        for i in range(1, len(nums)):
            if nums[i] != None and nums[i] > nums[i-1]:
                streak += 1
            else:
                # compare with last streak
                result = max(result, min(last_streak[0], streak), streak//2)

                last_streak = (streak, last_streak[1] + 1, i-1)
                streak = 1
                # print(last_streak)
        return result
            