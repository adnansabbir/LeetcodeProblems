class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        result = 0
        start = 0
        for i, char in enumerate(s):
            if char in seen:
                while char in seen:
                    seen.remove(s[start])
                    start += 1
            seen.add(char)
            result = max(result, len(seen))

        return result


        