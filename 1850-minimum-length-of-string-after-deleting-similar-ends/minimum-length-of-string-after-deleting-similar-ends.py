class Solution:
    def minimumLength(self, s: str) -> int:
        left, right = 0, len(s) - 1

        while left < right and s[left] == s[right]:
            currChar = s[left]
            while left <= right and s[left] == currChar:
                left += 1
            
            while left <= right and s[right] == currChar:
                right -= 1        

        return (right - left) + 1
        