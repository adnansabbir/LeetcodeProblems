class Solution:
    
    def deleteAndEarn(self, nums: List[int]) -> int:
        nums_map = defaultdict(int)
        max_num = 0
        
        for num in nums:
            nums_map[num] += num
            max_num = max(max_num, num)
    
        @cache
        def maxPoints(num: int)-> int:
            if num == 0:
                return 0

            if num == 1:
                return nums_map[1]

            return max(maxPoints(num-1), maxPoints(num-2) + nums_map[num])

        return maxPoints(max_num)