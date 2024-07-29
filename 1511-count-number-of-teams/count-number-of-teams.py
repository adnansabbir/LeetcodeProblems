class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        
        result = 0
        for i in range(1, n-1):
            ls, lg, rs, rg = 0, 0, 0, 0
            for j in range(i):
                ls += 1 if rating[j] < rating[i] else 0
                lg += 1 if rating[j] > rating[i] else 0
            
            for j in range(i+1, n):
                rs += 1 if rating[j] < rating[i] else 0
                rg += 1 if rating[j] > rating[i] else 0
        
            result += (ls * rg) + (lg * rs)
        
        return result