class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashResultMap = {}

        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
        def getHash(word: str) -> int:
            wordHash = 1
            for char in word:
                wordHash *= primes[ord(char) - ord('a')]
            return wordHash
        
        for word in strs:
            wordHash = getHash(word)
            if wordHash not in hashResultMap:
                hashResultMap[wordHash] = []

            hashResultMap[wordHash].append(word)
            
        return hashResultMap.values()