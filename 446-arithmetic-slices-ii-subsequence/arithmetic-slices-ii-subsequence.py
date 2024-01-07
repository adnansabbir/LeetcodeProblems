from collections import defaultdict
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        sequences = {}
        result = 0

        for i, val in enumerate(nums):
            for j in range(i):
                diff = val - nums[j]
                if i not in sequences or diff not in sequences[i]:
                    if i not in sequences:
                        sequences[i] = { diff: 0 }
                    else:
                        sequences[i][diff] = 0
                
                prevSeqCount = 0
                if j in sequences and diff in sequences[j]:
                    prevSeqCount = sequences[j][diff]

                sequences[i][diff] += 1 + prevSeqCount

                result += prevSeqCount
        return result