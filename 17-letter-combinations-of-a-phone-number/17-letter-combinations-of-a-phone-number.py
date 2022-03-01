class Solution:
    lettersInDigit = {
        2: 'abc',
        3: 'def',
        4: 'ghi',
        5: 'jkl',
        6: 'mno',
        7: 'pqrs',
        8: 'tuv',
        9: 'wxyz',
    }
    
    def appendCharToArray(self, digit: str, arr: List[str])-> List[str]:
        if not arr:
            return [c for c in self.lettersInDigit[int(digit)]]
        
        res = []
        
        for char in self.lettersInDigit[int(digit)]:
            for word in arr:
                res.append(f'{char}{word}')
        
        return res
    
    def letterCombinations(self, digits: str) -> List[str]:
        result = []
        
        for num in digits[::-1]:
            result = self.appendCharToArray(num, result)
        
        return result
            
            
            
        