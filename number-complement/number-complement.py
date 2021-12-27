class Solution:
    def findComplement(self, num: int) -> int:
        # Generating a number full of all 1 same as the bit length of given num
        ones = (1<<num.bit_length()) - 1
        
        # Doing XOR to inverse
        return ones ^ num