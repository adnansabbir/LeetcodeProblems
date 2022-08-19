class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        sequences = defaultdict(int)
        remaining = Counter(nums)
        
        for num in nums:
            if not remaining[num]:
                continue
            
            if sequences[num-1]:
                sequences[num-1]-=1
                sequences[num]+=1
                remaining[num]-=1
            else:
                if not remaining[num+1] or not remaining[num+2]:
                    return False
                
                remaining[num]-=1
                remaining[num+1]-=1
                remaining[num+2]-=1
                sequences[num+2]+=1
            
        return True