class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1
        if n == 1:
            return 0
        
        helper = 2**n.bit_length()-1
        # print(helper, bin(helper))
        return n^helper
        