class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        sortedPoints = sorted(points, key = lambda x: x[0])
        return max([val[0] - sortedPoints[i][0] for i, val in enumerate(sortedPoints[1:])])
