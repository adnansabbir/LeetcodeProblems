class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def patternMatched(word: str)-> bool:
            if len(word) != len(pattern):
                return False
            
            p_m = {}
            w_m = {}
            
            for i, ch in enumerate(pattern):
                if ch not in p_m:
                    p_m[ch] = word[i]
                if word[i] not in w_m:
                    w_m[word[i]] = ch    
                
                if p_m[ch] != word[i] or w_m[word[i]] != ch:
                    return False
            
            return True
        
        result = list(filter(patternMatched, words))
        
        return result
                    