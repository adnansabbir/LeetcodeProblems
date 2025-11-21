from collections import defaultdict
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        letter_idx_map = {}

        result = 0
        for i, letter in enumerate(s):
            if not letter_idx_map.get(letter):
                letter_idx_map[letter] = {'s': None, 'e': None}
            if letter_idx_map[letter]['s'] == None:
                letter_idx_map[letter]['s'] = i
            else:
                letter_idx_map[letter]['e'] = i

        for char in letter_idx_map.keys():
            if not letter_idx_map[char]['e']:
                continue
            
            uniq = set()
            for i in range(letter_idx_map[char]['s'] + 1, letter_idx_map[char]['e']):
                uniq.add(s[i])
            result += len(uniq)
        return result