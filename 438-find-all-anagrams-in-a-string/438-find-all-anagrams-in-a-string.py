class Solution:
    @staticmethod
    def getStrFrequency(text: str)-> List[int]:
        frequency = [0]*26
        for ch in text:
            frequency[ord(ch) - ord('a')] +=1
        return frequency
    
    @staticmethod
    def compareFrequency(f1: List[int], f2: List[int])-> bool:
        for a,b in zip(f1, f2):
            if a!=b:
                return False
        return True
    
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p)>len(s):
            return []
        
        p_length = len(p)
        s_length = len(s)
        
        p_frequency = self.getStrFrequency(p)
        s_frequency = self.getStrFrequency(s[0:p_length])
        
        anagram_indexes = []
        
        if self.compareFrequency(p_frequency, s_frequency):
            anagram_indexes.append(0)

        for index in range(1, (s_length - p_length + 1)):
            s_frequency[ord(s[index - 1]) - ord('a')] -= 1
            s_frequency[ord(s[index + p_length - 1]) - ord('a')] += 1

            if self.compareFrequency(p_frequency, s_frequency):
                anagram_indexes.append(index)

        return anagram_indexes