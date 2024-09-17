from collections import Counter
class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        result = []

        word_freq = Counter(s1.split(' ') + s2.split(' '))

        for word, freq in word_freq.items():
            if freq == 1:
                result.append(word)
        
        return result
        