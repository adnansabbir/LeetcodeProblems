class Solution:
    def removeInitialSpace(self, s: str)-> str:
        start = 0
        while start<len(s) and s[start] == ' ':
            start+=1
        
        return s[start:]
    
    def getLastDigitIndex(self, s: str)-> str:
        end = 0
        while end<len(s) and s[end].isdigit():
            end+=1
        return end
    
    def myAtoi(self, s: str) -> int:
        if not s:
            return 0
        
        # White space check
        s = self.removeInitialSpace(s)
        if not s:
            return 0
        
        # NegetivityCheck
        isNegative = s[0] == '-'
        if s[0] == '+' or s[0] == '-':
            s = s[1:]
            
        if not s:
            return 0
        
        # Get till the digit ends
        s = s[:self.getLastDigitIndex(s)]
        if not s:
            return 0
        
        max_num = (2**31 - 1)//10
        max_last_num = 7 if isNegative else 6
        result = 0
        
        print(s, len(s))
        
        for ch in s:
            if result < max_num or (result == max_num and int(ch) <= max_last_num):
                result = (result*10) + int(ch)
            elif isNegative:
                return (2**31) * -1
            else:
                print(result, max_num, int(ch), max_last_num)
                return (2**31 - 1)
        
        if isNegative:
            return result *-1
        
        return result
        