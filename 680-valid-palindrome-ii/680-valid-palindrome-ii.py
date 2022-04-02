class Solution:
    def validPalindrome(self, s: str) -> bool:
        def valid(s: str) -> bool:
            start, end = 0, len(s) - 1

            canRemove = 1
            while start<end:

                if s[start] == s[end]:
                    pass
                elif canRemove and s[start+1] == s[end]:
                    start+=1
                    canRemove -=1
                elif canRemove and s[start] == s[end-1]:
                    canRemove -=1
                    end-=1
                else:
                    return False

                start+=1
                end-=1

            return True
        
        return valid(s) or valid(s[::-1])
        