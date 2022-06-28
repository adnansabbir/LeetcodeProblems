from collections import defaultdict

class Solution:
    def minDeletions(self, s: str) -> int:
        frequencies = [0] * 26
        for char in s:
            frequencies[ord(char) - 97] += 1
        
        result = 0
        freqSet = set()
        for i, freq in enumerate(frequencies):
            if not freq:
                continue
            
            if freq not in freqSet:
                freqSet.add(freq)
            else:
                for j in range(freq - 1, -1, -1):
                    result += 1
                    if j not in freqSet and i > 0:
                        freqSet.add(j)
                        break
        
        return result