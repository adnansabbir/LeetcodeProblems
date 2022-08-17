class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        codes = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        def transform(word: str)-> str:
            return ''.join([codes[ord(ch) - ord('a')] for ch in word])
        
        return len(set([transform(word) for word in words]))
        