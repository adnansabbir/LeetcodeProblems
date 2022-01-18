class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        for i, f in enumerate(flowerbed):
            start, end = max(0, i-1), min(len(flowerbed), i+2)
            if not sum(flowerbed[start: end]):
                flowerbed[i] = 1
                n -= 1
            
            if n <= 0:
                return True
        
        return False