class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        
        memo = {-1: 0}
        count = 0
        def helper(i1, i2, i3):
            # print(i1, s1[i1:], i2, s2[i2:], i3, s3[i3:])
            # print(i1, i2, i3)
            if i3 == len(s3):
                return True
            
            if f'{i1}-{i2}' in memo:
                return memo[f'{i1}-{i2}']
            
            memo[-1] +=1
            
            if i1 < len(s1) and s1[i1] == s3[i3]:
                matched = helper(i1+1, i2, i3+1)
                memo[f'{i1}-{i2}'] = matched
                if matched:
                    return True
            
            if i2 < len(s2) and s2[i2] == s3[i3]:
                matched = helper(i1, i2+1, i3+1)
                memo[f'{i1}-{i2}'] = matched
                if matched:
                    return True
                
            memo[f'{i1}-{i2}'] = False
            return False
        
        result = helper(0,0,0)
        return result