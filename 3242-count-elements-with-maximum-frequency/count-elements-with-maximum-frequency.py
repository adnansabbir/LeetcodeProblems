class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        maxFreq = 0

        freq = [0 for _ in range(101)]

        for num in nums:
            freq[num] += 1
            maxFreq = max(maxFreq, freq[num])

        return sum([f for f in freq if f == maxFreq])
        