class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        left,right = [1, len(nums)-2]
        
        @cache
        def findMaxCoin(l: int, r: int)-> int:
            if l>r:
                return 0
            elif l==r:
                return nums[l]*nums[l-1]*nums[l+1]
            
            return max([(findMaxCoin(l, i-1) + nums[l-1]*nums[i]*nums[r+1] + findMaxCoin(i+1, r)) for i in range(l, r+1)])
        
        return findMaxCoin(left, right)
