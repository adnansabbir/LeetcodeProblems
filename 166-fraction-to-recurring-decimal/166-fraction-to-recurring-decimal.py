class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        # if numerator is divisible return the result
        if numerator % denominator == 0:
            return f'{numerator//denominator}'
        
        # Note: since numerator % denomintor is not zero, definately there will be fration part
        
        # result will be negetive if numerator or denominator is negetive but not both
        sign = '-' if (numerator < 0 or denominator < 0) and not (numerator < 0 and denominator < 0) else ''
        n = abs(numerator)
        d = abs(denominator)
        
        # extracting the result part that is before fraction by normal division
        res = f"{int(n/d)}"
        res += '.'
        
        # we already have result before fraction, so we have to calculate result after fraction
        n = (n % d)
        
        # dictionary to keep track of remainders and their position. 
        #If any remainder appears twice it means there is a pattern
        rems = {n: len(res)}
        
        # n will be zero of we can device without repetition 
        while n:
            # after fraction we can add an additional zero without adding a zero to result
            if n < d:
                n *= 10
            
            # still if numerator is less than denominator we add more zeros to it by adding zeros to result
            while n < d:
                res +="0"
                n *= 10
            
            res += f"{int(n/d)}"
            n = (n % d)
            
            # if we find a repeated reminder, we break the loop
            if n in rems:
                break
                
            rems[n] = len(res)
        
        # if the above loop broke because of n is zero, means there is no pattern
        if not n:
            return sign + res
        
        # Let's say the above loops broke with n = 4. Means we already encountered a 4 before which we can find in "rems" dict
        # We add opening and closing bracket
        return sign + res[:rems[n]] + f"({res[rems[n]:]})"
        