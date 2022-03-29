class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        start = 1
        end = len(nums) - 1
        
        while start <= end:
            mid = (start+end)//2
            count = sum(num <= mid for num in nums)
            
            if count > mid:
                duplicate = mid
                end = mid - 1
            else:
                start = mid + 1
        
        return duplicate
        