class Solution:
    def findNextSeq(self, numStr: str)-> str:
        prev = numStr[0]
        count = 0
        newNumStr = ''
        for num in numStr:
            if num != prev:
                newNumStr +=str(count)+prev
                prev = num
                count = 1
            else:
                count +=1
        
        newNumStr +=str(count)+prev
        
        return newNumStr
                
    
    def countAndSay(self, n: int, sequence = None) -> str:
        if not sequence:
            sequence = {
                1:"1"
            }
        
        if n in sequence:
            return sequence[n]
        else:
            sequence[n] = self.findNextSeq(self.countAndSay(n-1, sequence))
            return sequence[n]