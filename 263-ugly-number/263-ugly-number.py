class Solution:
    def isUgly(self, n: int) -> bool:
        if 0 < n < 2:
            return True
        elif n<=0:
            return False
        
        if n == 0:
            return True
        
        if n%2 == 0 and self.isUgly(n//2):
            return True
        
        if n%3 == 0 and self.isUgly(n//3):
            return True
        
        if n%5 == 0 and self.isUgly(n//5):
            return True
        
        return False