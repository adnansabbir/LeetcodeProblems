from collections import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        word1BiMap = [False for i in range(26)]
        word2BiMap = [False for i in range(26)]
        freq1 = [0 for i in range(26)]
        freq2 = [0 for i in range(26)]

        for i in range(len(word1)):
            word1Char = ord(word1[i]) - ord('a')
            word2Char = ord(word2[i]) - ord('a')

            word1BiMap[word1Char] = True
            freq1[word1Char] += 1
            word2BiMap[word2Char] = True
            freq2[word2Char] += 1

        freq1 = sorted(freq1)
        freq2 = sorted(freq2)
        print(word2BiMap, word2BiMap)
        return word1BiMap == word2BiMap and freq1 == freq2
        