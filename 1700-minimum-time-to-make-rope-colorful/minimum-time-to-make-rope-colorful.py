class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        colors = colors + ('z' if colors[-1] != 'z' else 'a')
        neededTime.append(1)

        totalTime = neededTime[0]
        maxTime = neededTime[0]

        result = 0

        for i in range(1, len(colors)):
            if colors[i] == colors[i-1]:
                totalTime += neededTime[i]

                if neededTime[i] > maxTime:
                    maxTime = neededTime[i]
            else:
                result += totalTime - maxTime
                totalTime = neededTime[i]
                maxTime = neededTime[i]
        
        return result
        