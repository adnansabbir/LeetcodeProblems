class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        result = 0
        
        for num in nums:
            if num not in nums_set:
                continue
            
            next_num = num
            seq_size = 0
            while next_num in nums_set:
                nums_set.remove(next_num)
                seq_size += 1
                next_num += 1
            
            prev_num = num - 1
            while prev_num in nums_set:
                nums_set.remove(prev_num)
                seq_size += 1
                prev_num -= 1
            result = max(result, seq_size)
        
        return result
