class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        maxFreqNum = None
        left, freq = 0, {}
        result = 0

        for right, num in enumerate(nums):
            freq[num] = freq.get(num, 0) + 1

            while freq[num] > k:
                freq[nums[left]] -= 1
                left += 1
            result = max(result, right - left + 1)
        
        return result
        
        