class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pattern_word_match = {}
        s_split = s.split(' ')
        
        if len(pattern) != len(s_split):
            return False
        
        for i, l in enumerate(pattern):
            word = f'w_{s_split[i]}'
            
            if l not in pattern_word_match and word not in pattern_word_match:
                pattern_word_match[l] = word
                pattern_word_match[word] = l
            
            if l in pattern_word_match and word != pattern_word_match[l]:
                return False
            
            if word in pattern_word_match and l != pattern_word_match[word]:
                return False
        
        return True