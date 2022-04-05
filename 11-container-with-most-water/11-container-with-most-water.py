class Solution:
    def maxArea(self, height: List[int]) -> int:
        start = 0
        end = len(height) - 1
        maxArea = 0
        
        while start<end:
            area = min(height[start],height[end]) * (end-start)
            maxArea = max(area, maxArea)
            
            if height[start]<height[end]:
                ts = height[start]
                while ts>= height[start] and start<end:
                    start+=1
            else:
                te = height[end]
                while te>= height[end] and start<end:
                    end-=1
                # decrement end
            
        
        return maxArea