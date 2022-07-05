class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        seq = {}
        visited = set()
        cs = 0
        
        for i, num in enumerate(nums):
            if num not in seq:
                seq[num] = [i]
            else:
                seq[num].append(i)
        
        for num in nums:
            if num in visited:
                continue
            
            visited.add(num)
            csTemp = 1
            numTemp = num
            while numTemp + 1 in seq:
                csTemp +=1
                numTemp+=1
                visited.add(numTemp)
            
            numTemp = num
            while numTemp - 1 in seq:
                csTemp +=1
                numTemp-=1
                visited.add(numTemp)
            
            cs = max(cs, csTemp)
            
        return cs    
                