class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        wordInitials = [[] for _ in range(26)]
        for word in words:
            wordInitials[ord(word[0]) - 97].append(word)
        
        count = 0
        for ch in s:
            idx = ord(ch) - 97
            
            n = len(wordInitials[idx])
            for _ in range(n):
                word = wordInitials[idx].pop(0)
                if len(word) == 1:
                    count +=1
                else:
                    word = word[1:]
                    wordInitials[ord(word[0]) - 97].append(word)
                    
        
        def isSubsequence(word)-> bool:
            return True
        
        return count