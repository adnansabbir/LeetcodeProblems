from collections import Counter

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        numFrequency = Counter(arr)
        uniqueFrequencies = set()

        for value in numFrequency.values():
            if value not in uniqueFrequencies:
                uniqueFrequencies.add(value)
            else:
                return False
        
        return True
