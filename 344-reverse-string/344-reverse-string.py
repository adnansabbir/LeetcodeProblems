class Solution:
    def reverseString(self, s: List[str]) -> None:
        n = len(s) - 1
        mid = (n//2) if n%2 == 0 else n//2 + 1
        for i in range(mid):
            s[i], s[n-i] = s[n-i], s[i]
        