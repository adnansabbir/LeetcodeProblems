class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals.sort(key= lambda x: (x[1], x[1]-x[0], x[1]))

        result = []
        for interval in intervals:
            if not result or result[-1] < interval[0]:
                result.append(interval[-1] - 1)
                result.append(interval[-1])
            elif interval[0] <= result[-2] and interval[1] >= result[1]:
                continue
            elif interval[0] < result[-1]:
                if interval[0] <= result[-2]:
                    continue
                elif result[-2] > interval[0] <=  result[-1]:
                    result.append(interval[1])
                else:
                    result.append(interval[1])    
            elif interval[0] == result[-1]:
                result.append(interval[1])
        
        # print(intervals)
        # print()
        # print(result)
        return len(result)
        