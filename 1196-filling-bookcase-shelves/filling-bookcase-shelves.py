from functools import lru_cache

class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        n = len(books)

        @lru_cache()
        def get_min_height(i: int):
            if i == n:
                return 0
            
            width_left = shelfWidth
            max_height = 0
            res = float("inf")

            for j in range(i, n):
                w, h = books[j]

                if width_left < w:
                    break
                
                width_left -= w
                max_height = max(max_height, h)

                res = min(res, get_min_height(j + 1) + max_height)
            
            return res
        
        return get_min_height(0)

