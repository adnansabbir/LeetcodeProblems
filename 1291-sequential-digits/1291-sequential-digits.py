class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        
        def makeSeq(i: int, length: int)-> int:
            if i > 10-length:
                return int(''.join([f'{n}' for n in range(1, length+2)]))
            return int(''.join([f'{n}' for n in range(i, i+length)]))
        
        def yieldSeq():
            start = makeSeq(int(str(low)[0]), len(str(low)))
            if start<low:
                start = makeSeq(int(str(low)[0]) + 1, len(str(low)))
                
            while start<=high:
                yield start
                start = makeSeq(int(str(start)[0]) + 1, len(str(start)))
        
        result = []
        for num in yieldSeq():
            result.append(num)
        
        return result