from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        freq = Counter(s)
        sortedFreq = sorted(list(freq.items()), key = lambda x: x[1], reverse = True)
        result = ''.join([ char*freq for char, freq in sortedFreq])
        return result

