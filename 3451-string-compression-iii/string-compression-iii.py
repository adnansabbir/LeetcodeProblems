class Solution:
    def compressedString(self, word: str) -> str:
        comp = ''

        last_char, count = '', 0
        for char in word:
            if char != last_char:
                if last_char:
                    comp += f'{count}{last_char}'
                last_char = char
                count = 1
            elif count == 9:
                comp += f'{count}{last_char}'
                count = 1
            else:
                count += 1
            
        if count:
            comp += f'{count}{last_char}'
            # print(comp, last_char, count)

        return comp
        