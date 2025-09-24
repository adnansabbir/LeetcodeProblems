class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator >= denominator and numerator % denominator == 0:
            return str(numerator // denominator)
        
        result_is_neg = False
        if numerator < 0:
            result_is_neg = True
            numerator = abs(numerator)
        if denominator < 0:
            if result_is_neg:
                result_is_neg = False
            else:
                result_is_neg = True
            denominator = abs(denominator)

        result = str(numerator//denominator)
        numerator = numerator % denominator

        has_decimal = False
        seen_numerators = {}
        while numerator and numerator not in seen_numerators:
            if numerator < denominator and not has_decimal:
                result+='.'
                has_decimal = True
                numerator *=10

                while numerator < denominator:
                    result += '0'
                    numerator *=10
            elif numerator < denominator:
                numerator = numerator*10

                while numerator < denominator:
                    result += '0'
                    numerator *=10
            else:
                digit = numerator // denominator
                seen_numerators[numerator] = len(result)
                numerator = numerator % denominator
                result+= str(digit)
        
        if numerator in seen_numerators:
            idx = seen_numerators[numerator]
            result = result[:idx] + '(' +  result[idx:] + ')'
        return result if not result_is_neg else '-' + result
            
        