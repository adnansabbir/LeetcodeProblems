class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 1
        pointer = 1
        result = 1
        [1,1,2,2,2,3,4,4,4,5]
        for i, num in enumerate(nums[1:]):
            if num != nums[i] or count < 2:
                if num == nums[i]:
                    count +=1
                else:
                    count = 1

                nums[pointer] = num
                pointer +=1
                result +=1
        
        return result
            
        
        