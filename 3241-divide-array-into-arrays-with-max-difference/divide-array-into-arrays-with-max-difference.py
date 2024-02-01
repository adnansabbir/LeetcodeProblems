class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums = sorted(nums)
        # print(nums)
        result = [[] for _ in range(len(nums)//3)]

        for i in range(0, len(nums), 3):
            if nums[i+2] - nums[i] > k:
                return []
            else:
                resultIdx = i // 3
                result[resultIdx].append(nums[i])
                result[resultIdx].append(nums[i+1])
                result[resultIdx].append(nums[i+2])
            # print(i, result)
        return result
        