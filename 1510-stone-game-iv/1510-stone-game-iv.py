class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        
        @lru_cache(maxsize=None)
        def canWin(leftStones):
            if leftStones == 0:
                return False
            
            sqrt = int(leftStones ** 0.5)
            
            for i in range(1, sqrt+1):
                if not canWin(leftStones - i*i):
                    return True
            
            return False
        
        return canWin(n)
        