from collections import defaultdict
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq = defaultdict(int)
        max_freq = 0
        max_freq_count = 0

        for num in nums:
            freq[num] += 1
            if freq[num] == max_freq:
                max_freq_count += 1
            elif freq[num] > max_freq:
                max_freq = freq[num]
                max_freq_count = 1

        return max_freq * max_freq_count
        