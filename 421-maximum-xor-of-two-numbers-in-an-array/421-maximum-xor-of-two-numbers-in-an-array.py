class TrieNode:
    def __init__(self):
        self.children = {}

class Solution:
    def __init__(self):
        self.root = None
    
    def insertBitsIntoTrie(self, num: int):
        num_bits = bin(num)[2:].zfill(32)
        node = self.root
        
        for bit in num_bits:
            if not bit in node.children:
                node.children[bit] = TrieNode()
            node = node.children[bit]
            
    
    def findMaxXor(self, num: int)-> int:
        num_bits = bin(num)[2:].zfill(32)
        node = self.root
        
        target = {'0':'1', '1':'0'}
        max_xor = ''
        
        for bit in num_bits:
            if target[bit] in node.children:
                max_xor+=target[bit]
                node = node.children[target[bit]]
            else:
                max_xor+=bit
                node = node.children[bit]
        
        return int(max_xor, 2) ^ num
        
    
    def findMaximumXOR(self, nums: List[int]) -> int:
        self.root = TrieNode()
        
        max_ = 0
        
        for num in nums:
            self.insertBitsIntoTrie(num)
            
        for num in nums:
            max_ = max(max_, self.findMaxXor(num))
            
        return max_
        
        
            
        