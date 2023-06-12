class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        result = []
        l = 0

        for i, num in enumerate(nums[1:]):
            if nums[i] + 1 != num:
                if i == l:
                    result.append(f'{nums[l]}')
                else:
                    result.append(f'{nums[l]}->{nums[i]}')
                l = i + 1
        
        if l == len(nums) - 1:
            result.append(f'{nums[-1]}')
        else:
            result.append(f'{nums[l]}->{nums[-1]}')
        return result

