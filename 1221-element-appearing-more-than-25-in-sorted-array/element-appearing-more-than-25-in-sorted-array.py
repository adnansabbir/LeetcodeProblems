class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        if len(arr)<2:
            return arr[0]

        freq = 1
        highestFreq = 1
        result = arr[0]

        for i, num in enumerate(arr[1:]):
            if num == arr[i]:
                freq += 1
            else:
                freq = 1

            if freq > highestFreq:
                highestFreq = freq
                result = num

        return result