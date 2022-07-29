class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def patternMatched(word: str)-> bool:
            if len(word) != len(pattern):
                return False
            
            p_m = {}
            w_m = {}
            
            for i, ch in enumerate(pattern):     
                if ch not in p_m:
                    if word[i] not in w_m:
                        w_m[word[i]] = ch
                        p_m[ch] = word[i]
                    else:
                        return False
                        
                elif p_m[ch] != word[i]:
                    return False
            
            return True
        
        result = list(filter(patternMatched, words))
        
        return result
                    