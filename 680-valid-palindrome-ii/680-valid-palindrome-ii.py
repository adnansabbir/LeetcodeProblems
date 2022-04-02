class Solution:
    def validPalindrome(self, s: str, start = 0, end = None, canRemove = 1) -> bool:
        if end == None:
            end = len(s) - 1
        
        while start < end:
            if s[start] != s[end]:
                canRemove -=1
                return self.validPalindrome(s, start+1, end, canRemove) or self.validPalindrome(s, start, end-1, canRemove) if canRemove+1 else False
            
            start +=1
            end -=1
        
        return True
        