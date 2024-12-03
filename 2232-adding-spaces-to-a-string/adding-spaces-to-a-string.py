class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        result = []
        prev_point = 0
        s_pointer = 0
        for next_point in spaces:
            result.append(s[prev_point: next_point])
            prev_point = next_point
            s_pointer += 1

        result.append(s[prev_point:])
        return ' '.join(result)