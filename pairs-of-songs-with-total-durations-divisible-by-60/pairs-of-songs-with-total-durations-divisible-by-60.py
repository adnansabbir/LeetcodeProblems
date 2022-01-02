class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        cache = {}
        total = 0
        for t in time:
            ti = t%60
            target = 60-ti if ti else 0
            # print(t, target, cache)
            if target in cache:
                total += cache[target]
                
            if ti not in cache:
                cache[ti] = 1
            else:
                cache[ti]+=1
        
        # print(cache)
        return total