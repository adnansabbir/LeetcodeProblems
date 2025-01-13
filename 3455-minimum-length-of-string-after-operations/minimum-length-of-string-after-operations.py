from collections import Counter

class Solution:
    def minimumLength(self, s: str) -> int:
        freq = Counter(s)
        
        result = 0
        for count in freq.values():
            if count <= 2:
                result += count
            elif count % 2 == 0:
                result += 2
            else:
                result += 1
        return result

        