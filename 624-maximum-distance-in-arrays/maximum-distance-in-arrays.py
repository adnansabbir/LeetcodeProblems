class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        high1, high2 = (-1, -10**5), (-1, -10**5)
        low1, low2 = (-1, 10**5), (-1, 10**5)

        for i in range(len(arrays)):
            if arrays[i][0] < low1[1]:
                low2 = low1
                low1 = (i, arrays[i][0])
            elif arrays[i][0] < low2[1]:
                low2 = (i, arrays[i][0])

            if arrays[i][-1] > high1[1]:
                high2 = high1
                high1 = (i, arrays[i][-1])
            elif arrays[i][-1] > high2[1]:
                high2 = (i, arrays[i][-1])

        if high1[0] != low1[0]:
            return high1[1] - low1[1]
        
        return max(abs(high1[1] - low2[1]), abs(high2[1] - low1[1]))
        