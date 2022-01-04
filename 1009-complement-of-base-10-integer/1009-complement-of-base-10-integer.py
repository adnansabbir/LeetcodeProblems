class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1
        if n == 1:
            return 0
        
        return n^(2**n.bit_length()-1)
        