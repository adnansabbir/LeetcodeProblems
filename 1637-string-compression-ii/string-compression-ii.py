class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        cache = {}

        def count(i: int, k: int, prev: str, prev_count: int)-> int:
            key = (i, k, prev, prev_count)
            if key in cache:
                return cache[key]

            if k < 0:
                return float('inf')
            
            if i == len(s):
                return 0

            if s[i] == prev:
                incr = 1 if prev_count in [1, 9, 99] else 0
                res = incr + count(i + 1, k, prev, prev_count + 1)
            else:
                res = min(
                    count(i + 1, k - 1, prev, prev_count), #delete
                    1 + count(i + 1, k, s[i], 1) #keep
                )
            
            cache[key] = res
            return res
        
        return count(0, k, "", 0)
