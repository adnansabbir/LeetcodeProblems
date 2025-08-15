class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = [0]*26
        offset = ord('A')
        result = 0

        def getMaxFreqChar():
            idx, val = max(enumerate(freq), key=lambda x: x[1])
            char = chr(idx + offset)
            return [char, val]

        left = 0
        for right in range(len(s)):
            idx = ord(s[right]) - offset
            freq[idx] += 1

            size = right - left + 1
            min_size = size - k

            max_char, max_char_freq = getMaxFreqChar()

            while max_char_freq < min_size:
                freq[ord(s[left]) - offset] -= 1
                left += 1
                size = right - left + 1
                min_size = size - k
                max_char, max_char_freq = getMaxFreqChar()
            result = max(result, size)
        return result


        