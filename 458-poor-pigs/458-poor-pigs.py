class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        T = minutesToTest // minutesToDie
        N = buckets
        start = 0
        end = N
        
        def maxTestableBucket(T, pigs)-> int:
            return pow(T+1, pigs)
        
        while start < end:
            mid = (start + end) // 2
            if maxTestableBucket(T, mid) < N:
                start = mid + 1
            else:
                end = mid
        
        return end