from collections import Counter

class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        def get_char_count(word: str)-> str:
            freq = Counter(word)
            result = ''
            for char, freq in sorted(freq.items()):
                result += f'{char}{freq}'
            return result

        result = [words[0]]
        last_char_count = get_char_count(words[0])
        for i, word in enumerate(words[1:]):
            if last_char_count == get_char_count(word):
                continue
            else:
                result.append(word)
                last_char_count = get_char_count(word)
        return result

        