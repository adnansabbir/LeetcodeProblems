class Solution:
    def uniquePaths(self, m: int, n: int, cache = {}) -> int:
        
        if m<1 or n<1:
            return 0
        
        if m == 1 and n==1:
            return 1
        
        key = "{}.{}".format(m,n)
        
        if key in cache:
            return cache[key]
        
        top = self.uniquePaths(m-1, n, cache)
        left = self.uniquePaths(m, n-1, cache)
        
        cache[key] = left + top
        
        return cache[key]
        
        