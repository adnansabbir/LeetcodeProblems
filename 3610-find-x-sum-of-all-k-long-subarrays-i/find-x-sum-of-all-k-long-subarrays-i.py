from collections import Counter
class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        def find_x_sum(start, end)-> int:
            freq = Counter(nums[start:end])
            freq_val = [(freq, num) for num, freq in freq.items()]
            if len(freq_val) <= x:
                return sum(nums[start:end])

            freq_val.sort(key=lambda x: (-x[0], -x[1]))
            result = 0
            for i in range(x):
                result += (freq_val[i][0] * freq_val[i][1])
            return result

        result = []
        for i in range(k, len(nums) + 1):
            result.append(find_x_sum(i-k, i))
        return result