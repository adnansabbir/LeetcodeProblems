class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator % denominator == 0:
            return f'{numerator//denominator}'
        
        isNegetive = (numerator < 0 or denominator < 0) and not (numerator < 0 and denominator < 0)
        n = abs(numerator)
        d = abs(denominator)
        
        res = f"-{int(n/d)}" if isNegetive else f"{int(n/d)}"
        res += '.'
        n = (n % d)
        rems = {n: len(res)}
        
        while n:
            if n < d:
                n *= 10
            
            while n < d:
                res +="0"
                n *= 10
            
            res += f"{int(n/d)}"
            n = (n % d)
            if n in rems:
                break
            rems[n] = len(res)
        
        if not n:
            return res
        
        return res[:rems[n]] + f"({res[rems[n]:]})"
        