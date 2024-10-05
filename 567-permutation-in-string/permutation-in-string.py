class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq1 = [0]*26
        freq2 = [0]*26
        matched = 0

        # count s1 freq
        for char in s1:
            freq1[ord(char) - ord('a')] += 1
        # count s2 freq and match
        for char in s2[:len(s1)]:
            freq2[ord(char) - ord('a')] += 1

        for i in range(26):
            if freq1[i] and freq2[i]:
                matched += min(freq1[i], freq2[i])

        if matched == len(s1):
            return True

        # slide to check if there is substring that matches
        for right in range(len(s1), len(s2)):
            # remove left char
            left = right - len(s1)
            idx = ord(s2[left]) - ord('a')
            if 0 < freq2[idx] <= freq1[idx]:
                matched -= 1
            freq2[idx] = max(freq2[idx] - 1, 0)

            # add right char
            idx = ord(s2[right]) - ord('a')
            freq2[idx] += 1
            if freq2[idx] <= freq1[idx]:
                matched += 1
            
            if matched == len(s1):
                return True

        return False
        