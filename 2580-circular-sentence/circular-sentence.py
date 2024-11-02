class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        if sentence[0] != sentence[-1]:
            return False
        
        for i, char in enumerate(sentence):
            if char == ' ' and sentence[i-1] != sentence[i+1]:
                return False

        return True

        