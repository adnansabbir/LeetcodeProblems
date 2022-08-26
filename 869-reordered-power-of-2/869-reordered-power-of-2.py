class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        freq = Counter(str(n))
        digitCount = len(str(n))
        window = [10**(digitCount-1), 10**(digitCount) - 1]
        possibleResults = set()
        for i in range(1000):
            if 2**i > window[1]:
                break
            if 2**i >= window[0]:
                possibleResults.add(''.join(sorted(str(2**i))))
        
        sortedN = ''.join(sorted(str(n)))
        return sortedN in possibleResults
            
        