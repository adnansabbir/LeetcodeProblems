from collections import Counter

class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        freq = Counter(arr)

        distinct_count = 0
        for word, count in freq.items():
            if count == 1:
                distinct_count += 1
            
                if distinct_count == k:
                    return word
        
        
        return ""
        