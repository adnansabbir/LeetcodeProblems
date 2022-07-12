class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total = sum(matchsticks)
        length = total // 4
        if total/4 != length:
            return False
        
        sides = [0]*4
        matchsticks.sort(reverse=True)
        
        def backtrack(idx)-> bool:
            if idx == len(matchsticks):
                return True
            
            for j in range(4):
                if sides[j] + matchsticks[idx] <= length:
                    sides[j] += matchsticks[idx]
                    if backtrack(idx + 1):
                        return True
                    sides[j] -= matchsticks[idx]
                    if sides[j] == 0:
                        break
            return False
        
        return backtrack(0)
                    
                
            