class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        result = []
        min_start, max_end = intervals[0][0], intervals[0][1]

        for st, en in intervals:
            if st > max_end:
                result.append([min_start, max_end])
                min_start = st
                max_end = en
            else:
                min_start = min(min_start, st)
                max_end = max(max_end, en)
        
        result.append([min_start, max_end])
        return result


        print(intervals)
        return []
        