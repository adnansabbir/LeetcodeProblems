class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        result = []
        def generate(num:int, digitLeft=n-1):
            if k == 0:
                number = num
                for _ in range(digitLeft):
                    number = number * 10 + num
                result.append(number)
                return
                
                
            if not digitLeft:
                result.append(num)
                return
            
            tail = num%10
            
            if tail - k > -1:
                generate(num*10+tail-k, digitLeft-1)
            
            if tail + k < 10:
                generate(num*10+tail+k, digitLeft-1)
            
        for i in range(1,10):
            generate(i)
        
        return result