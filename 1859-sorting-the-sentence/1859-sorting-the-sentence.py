class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split(' ')
        words_sorted = sorted(words, key= lambda x: int(x[-1]))
        words_without_num = [word[:-1] for word in words_sorted]
        return ' '.join(words_without_num)