class Solution:
    def findMin(self, nums: List[int]) -> int:
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
        
        