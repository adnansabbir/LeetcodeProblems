class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        i, j = 0, 0
        
        def next_char(char):
            return chr(ord(char) + 1) if char != 'z' else 'a'

        while i < len(str1) and j < len(str2):
            if str1[i] == str2[j] or next_char(str1[i]) == str2[j]:
                j += 1
            i += 1

            if j == len(str2):
                return True
        
        return False



        