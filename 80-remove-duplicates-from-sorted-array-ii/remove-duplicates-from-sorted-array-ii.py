class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        p = 1
        counter = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                counter += 1
            else:
                counter = 1

            if counter < 3:
                nums[p] = nums[i]
                p+=1
        return p
            
        
        