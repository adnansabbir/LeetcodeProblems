class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        num_set = set()
        pairs = set()
        count = 0
        
        for num in nums:
            t1 = k + num
            t2 = (k*-1) + num
            
            if t1 in num_set and f'{t1}-{num}' not in pairs:
                count +=1
                pairs.add(f'{t1}-{num}')
                pairs.add(f'{num}-{t1}')
                
            if t2 in num_set and f'{t2}-{num}' not in pairs:
                count +=1
                pairs.add(f'{t2}-{num}')
                pairs.add(f'{num}-{t2}')
            
            num_set.add(num)
        
        return count