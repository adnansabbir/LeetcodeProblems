class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        winner, count = nums[0], 0

        for num in nums:
            if count == 0:
                winner = num
                count += 1
            else:
                if num != winner:
                    count -= 1
                else:
                    count += 1
        return winner