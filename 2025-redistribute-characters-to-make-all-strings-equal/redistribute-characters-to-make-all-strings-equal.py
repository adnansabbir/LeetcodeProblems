class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        freq = [0 for i in range(26)]

        for word in words:
            for char in word:
                freq[ord(char) - ord('a')] += 1
        
        for count in freq:
            if count % len(words) != 0:
                return False
        return True

        