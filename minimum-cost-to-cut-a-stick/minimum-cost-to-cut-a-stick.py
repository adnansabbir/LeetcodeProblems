import sys
class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts = [0] + sorted(cuts) + [n]

        @cache
        def cutCost(cutsLeftIndex, cutsRightIndex)-> int:
            if cutsLeftIndex + 1 == cutsRightIndex:
                return 0

            currCost = cuts[cutsRightIndex] - cuts[cutsLeftIndex]
            return min([cutCost(cutsLeftIndex, mid) + cutCost(mid, cutsRightIndex) + currCost for mid in range(cutsLeftIndex + 1, cutsRightIndex)])
        
        res = int(cutCost(0, len(cuts) - 1))
        # print(count)
        return res