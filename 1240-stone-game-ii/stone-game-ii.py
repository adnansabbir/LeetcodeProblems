from functools import lru_cache

class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)

        @lru_cache(maxsize=None)
        def get_max(i: int, M: int, alice = True)-> int:
            if i >= len(piles):
                return 0
            
            res = 0 if alice else float('inf')
            total = 0
            for X in range(1, 2 * M + 1):
                if i + X > n:
                    break
                total += piles[i + X - 1]

                if alice:
                    res = max(res, total + get_max(i + X, max(X, M), not alice))
                else:
                    res = min(res, get_max(i + X, max(X, M), not alice))
            return res


        return get_max(0, 1)
        