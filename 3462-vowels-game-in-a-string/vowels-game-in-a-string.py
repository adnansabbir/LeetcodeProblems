class Solution:
    def doesAliceWin(self, s: str) -> bool:
        for char in s:
            if char in {'a','e','i','o','u'}:
                return True
        return False
        