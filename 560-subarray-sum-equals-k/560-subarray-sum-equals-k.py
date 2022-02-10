class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum_map = {0: 1}
        cu_sum = 0
        result = 0
        
        for num in nums:
            cu_sum+=num
            if cu_sum - k in sum_map:
                result +=sum_map[cu_sum - k]
            
            if cu_sum not in sum_map:
                sum_map[cu_sum] = 1
            else:
                sum_map[cu_sum] += 1
        
        return result