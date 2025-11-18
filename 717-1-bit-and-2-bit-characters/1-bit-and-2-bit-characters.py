class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        if len(bits) < 3:
            bits = [0,0] + bits
        
        if bits[-2] == 0:
            return True
        count = 0
        for i in range(len(bits) - 2, -1, -1):
            if bits[i] == 1:
                count += 1
            else:
                break
        return count % 2 == 0 
        