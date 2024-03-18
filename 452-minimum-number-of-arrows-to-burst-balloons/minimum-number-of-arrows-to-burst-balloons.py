class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x: (x[0], -x[1]))
        
        left, right = points[0][0], points[0][1]

        shots = 1
        for start, end in points:
            left = max(left, start)
            right = min(right, end)

            if left > right:
                shots += 1
                left, right = start, end


        # print(points)
        return shots
        