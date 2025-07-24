class Solution:
    def findMin(self, nums: List[int]) -> int:
        # [4,5,1,2,3]
        # # if mid-1 is > and mid+1 is <, this is the target
        
        # [5,1,2,3,4]
        # # if left is > mid, result is in between

        # [3,4,5,1,2]
        # # if right < mid target is between

        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if ((mid-1 < 0) or nums[mid-1] > nums[mid]) and ((mid+1 == len(nums)) or nums[mid+1] >= nums[mid]):
                return nums[mid]
            elif nums[left] > nums[mid]:
                right = mid - 1
            elif nums[right] < nums[mid]:
                left = mid + 1
            elif nums[left] <= nums[mid]:
                right = mid - 1
            else:
                 left = mid + 1
        
        