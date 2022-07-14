class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator % denominator == 0:
            return f'{numerator//denominator}'
        
        isNegetive = (numerator < 0 or denominator < 0) and not (numerator < 0 and denominator < 0)
        numerator = numerator if numerator >=0 else -numerator
        denominator = denominator if denominator >=0 else -denominator
        
        res = f"{int(numerator/denominator)}"
        result = (['-'] if isNegetive else []) + res.split()
        result.append('.')
        rem = (numerator % denominator)
        remainders = {rem: len(result)}
        # print(result)
        while rem:
            if rem < denominator:
                rem *= 10
            
            while rem < denominator:
                result.append("0")
                rem *= 10
            
            result.append(f"{int(rem/denominator)}")
            rem = (rem % denominator)
            if rem in remainders:
                break
            remainders[rem] = len(result)
        
        if not rem:
            return ''.join(result)
        
        result.insert(remainders[rem], '(')
        result.append(')')
        return "".join(result)
        