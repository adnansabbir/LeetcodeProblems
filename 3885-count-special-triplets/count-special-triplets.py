from collections import Counter, defaultdict

class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        freq_left = defaultdict(int)
        freq_right = Counter(nums)
        freq_right[nums[0]] -= 1
        freq_left[nums[0]] += 1

        result = 0
        for i in range(1, len(nums) - 1):
            freq_right[nums[i]] -= 1
            sugar_daddy = nums[i] * 2

            sugar_daddy_left = freq_left.get(sugar_daddy, 0)
            sugar_daddy_right = freq_right.get(sugar_daddy, 0)
            result += (sugar_daddy_left * sugar_daddy_right)
            result = result % (10**9 + 7)

            freq_left[nums[i]] += 1
        return result

            
        