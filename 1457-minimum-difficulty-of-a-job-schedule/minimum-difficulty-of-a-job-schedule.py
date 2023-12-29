from functools import lru_cache

class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        maxIdx = len(jobDifficulty) - 1
        if len(jobDifficulty) < d:
            return -1

        @lru_cache(maxsize=None)
        def minTime(idx: int, dLeft: int)-> int: 
            if dLeft == 1:
                return max(jobDifficulty[idx:])
            
            if idx > maxIdx:
                return 0
            
            maxDifficulty = jobDifficulty[idx]
            res = maxDifficulty + minTime(idx + 1, dLeft - 1)

            for i in range(idx + 1, maxIdx + 1 - (dLeft - 1)):
                currMaxDifficulty = max(maxDifficulty, jobDifficulty[i])
                currentRes = currMaxDifficulty + minTime(i + 1, dLeft - 1)
                maxDifficulty = currMaxDifficulty
                res = min(res, currentRes)
                # print(f'Idx: {idx} i: {i} dL: {dLeft} cd: {currMaxDifficulty} res: {res}, taken:{jobDifficulty[idx: i+1]}')
            return res
        
        
        return minTime(0, d)
