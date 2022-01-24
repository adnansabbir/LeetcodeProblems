class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if len(word) < 2:
            return True
        
        first_letter_cap = False
        
        if ord('A') <= ord(word[0]) <= ord('Z'):
            first_letter_cap = True
            
        second_letter_cap = False
        if ord('A') <= ord(word[1]) <= ord('Z'):
            second_letter_cap = True
            
        
        restCap = False
        
        if first_letter_cap and second_letter_cap:
            restCap = True
            
        elif not first_letter_cap and second_letter_cap:
            return False
        
        for l in word[2:]:
            if ord('A') <= ord(l) <= ord('Z') and not restCap:
                return False
            elif not ord('A') <= ord(l) <= ord('Z') and restCap:
                return False
        
        return True