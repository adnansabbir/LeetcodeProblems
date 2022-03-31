class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        n = len(nums)
        
        accu_sum = [0] + list(itertools.accumulate(nums))
        
        @cache
        def get_min_max(curr_idx: int, m_left: int):
            if m_left == 1:
                return accu_sum[n] - accu_sum[curr_idx]
            
            result = accu_sum[n]
            
            for i in range(curr_idx, n - (m_left-1)):
                left_sum = accu_sum[i+1] - accu_sum[curr_idx]
                largest_split_sum = max(left_sum, get_min_max(i+1, m_left-1))
                
                result = min(result, largest_split_sum)
                
                if left_sum >= result:
                    break
            return result
        
        return get_min_max(0, m)
            
            
        