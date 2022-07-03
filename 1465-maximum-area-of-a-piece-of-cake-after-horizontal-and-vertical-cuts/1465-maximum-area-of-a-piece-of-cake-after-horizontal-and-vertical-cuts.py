class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        def getMaxGap(start: int, end: int, cuts: List[int]):
            gap = max(cuts[0] - start, end - cuts[-1])
            for i in range(1, len(cuts)):
                gap = max(gap, abs(cuts[i] - cuts[i-1]))

            return gap
        
        horizontalCuts.sort()
        verticalCuts.sort()
        horizontalMaxGap = getMaxGap(0, h, horizontalCuts)
        verticalMaxGap = getMaxGap(0, w, verticalCuts)
        return (horizontalMaxGap * verticalMaxGap) % (pow(10, 9) + 7)