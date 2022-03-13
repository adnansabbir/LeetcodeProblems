class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        result = [-1, -1]
        
        start = 0
        end = len(nums)-1
        
        # finding start
        while start<=end:
            mid = (start+end)//2
            
            if nums[mid] == target and (mid==0 or nums[mid] > nums[mid-1]):
                result[0] = mid
                start = end+1
            elif nums[mid]>=target:
                end = mid-1
            else:
                start = mid+1
        
        if result[0] == -1:
            return result
        
        
        start = 0
        end = len(nums)-1
        
        # finding end
        while start<=end:
            mid = (start+end)//2
            
            if nums[mid] == target and (mid==len(nums)-1 or nums[mid] < nums[mid+1]):
                result[1] = mid
                start = end+1
            elif nums[mid]>target:
                end = mid-1
            else:
                start = mid+1
        
        return result