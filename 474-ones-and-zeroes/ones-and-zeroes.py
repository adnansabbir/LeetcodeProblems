from functools import lru_cache

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:

        freq = []
        for s in strs:
            freq.append((s.count('0'), s.count('1')))

        @lru_cache(maxsize=None)
        def count_max(idx = 0, f_0 = 0, f_1 = 0, count = 0):
            if f_0 > m or f_1 > n:
                return 0
            if idx >= len(freq):
                return count
            
            return max(
                count_max(idx + 1, f_0 + freq[idx][0], f_1 + freq[idx][1], count + 1),
                count_max(idx + 1, f_0, f_1, count)
            )
        return count_max()