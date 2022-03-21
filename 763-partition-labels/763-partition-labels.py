class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        range_map = {}
        result = []
        
        for i, c in enumerate(s):
            if c not in range_map:
                range_map[c] = [i, i]
            else:
                range_map[c][1] = i
        
        start = end = 0
        for i, c in enumerate(s):
            end = max(end, range_map[c][1])
            if end == i:
                result.append(end+1 - start)
                start = i+1
        
        return result