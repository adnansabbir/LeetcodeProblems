class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        modified = 0
        
        def getViolations() -> int:
            violations = 0
            idx = []
            for i in range(1, len(nums)):
                if nums[i] < nums[i-1]:
                    violations +=1
                    idx.append(i)
                    if violations > 1:
                        return [violations, idx]
            return [violations, idx]
        
        [violations, idx] = getViolations()
        
        if violations > 1:
            return False
        
        if violations == 0 or (violations == 1 and idx[0] == len(nums) - 1):
            return True
        

        leftAns = True
        rightAns = True
        left = nums[idx[0]-1]
        if idx[0] > 0:
            nums[idx[0]-1] = nums[idx[0]]
            leftAns = getViolations()[0] == 0
            
        if(leftAns):
            return True
        
        nums[idx[0]-1] = left
        nums[idx[0]] = nums[idx[0]+1]
        rightAns = getViolations()[0] == 0
        
        return leftAns or rightAns
        """
        :type nums: List[int]
        :rtype: bool
        """
        