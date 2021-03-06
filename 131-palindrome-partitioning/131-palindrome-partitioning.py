class Solution:
    def partition(self, s: str) -> List[List[str]]:
        partition = []
        result = []
        palindromes = {}
    
        def isPalindrome(s: str, start: int, end: int):
            if start == end or end<start:
                return True
            
            key = f"{start}-{end}"
            if key in palindromes:
                return palindromes[key]
            
            palindromes[key] = s[start] == s[end] and isPalindrome(s, start+1, end-1)
            return palindromes[key]
    
        def dfs(i: int):
            if i >= len(s):
                result.append(partition.copy())
                return
            
            for j in range(i, len(s)):
                if isPalindrome(s, i, j):
                    partition.append(s[i: j+1])
                    dfs(j+1)
                    partition.pop()
        
        dfs(0)
        return result
    