class Solution:
    def findComplement(self, num: int) -> int:
        bits_in_num = num.bit_length()
        return num ^ ((1 << bits_in_num) - 1)