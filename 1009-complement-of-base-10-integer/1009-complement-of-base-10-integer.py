class Solution:
    def bitwiseComplement(self, n: int) -> int:
        a = 1
        for _ in range(n.bit_length()-1):
            a = (a<<1) + 1
        
        # print(bin(a))
        return n^a
        