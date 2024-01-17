from collections import Counter

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        numFrequency = Counter(arr)
        
        return len(numFrequency) == len(set(numFrequency.values()))
