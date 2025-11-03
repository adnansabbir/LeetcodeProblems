class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        result = 0
        l, r = 0, 1
        while r < len(colors):
            if colors[l] == colors[r]:
                result += min(neededTime[l], neededTime[r])
                if neededTime[l] < neededTime[r]:
                    l = r
            else:
                l = r
            r += 1
        return result

        