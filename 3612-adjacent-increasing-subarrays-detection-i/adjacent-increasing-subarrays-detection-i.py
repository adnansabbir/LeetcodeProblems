class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        if k == 1:
            return True

        nums.append(-2000)
        incs = []

        streak = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                streak += 1
            else:
                if streak >= k:
                    if incs and incs[-1][1] == i-streak:
                        return True
                    incs.append((i-streak,i))
                streak = 1
            if streak // 2 >= k:
                return True
        # print(incs)      
        return False
        