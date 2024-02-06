class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashResultMap = {}

        def getHash(word: str) -> Tuple[int]:
            freq = [0 for _ in range(26)]
            for char in word:
                freq[ord(char) - ord('a')] += 1
            return tuple(freq)
        
        result = []
        for word in strs:
            wordHash = getHash(word)
            # print(word, wordHash)
            if wordHash not in hashResultMap:
                result.append([])
                hashResultMap[wordHash] = len(result) - 1
            
            result[hashResultMap[wordHash]].append(word)
        return result