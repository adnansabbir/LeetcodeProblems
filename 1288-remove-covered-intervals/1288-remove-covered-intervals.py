class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        sorted_intervals = sorted(intervals, key=lambda x: [x[0], -x[1]])
        
        max_range = 0
        count = 0

        for interval in sorted_intervals:
            if interval[0]>max_range or interval[1]>max_range:
                count+=1
                max_range = max(max_range, interval[1])
        
        return count