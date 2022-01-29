class Solution:

    def getRightMaxLimit(self, heights: List[int], width: List[int])-> List[int]:
        stack = [len(heights)-1]
        width[-1] = len(heights) - width[-1]

        for i in reversed(range(len(heights)-1)):
            while stack:
                if heights[stack[-1]] >= heights[i]:
                    stack.pop()
                else:
                    width[i] = stack[-1] - width[i]
                    break
            if not stack:
                width[i] = len(heights) - width[i]
            
            stack.append(i)
        
        return width

    def getLeftMaxLimit(self, heights: List[int])-> List[int]:
        stack = [0]
        left = [0]

        for i in range(1, len(heights)):
            while stack:
                if heights[stack[-1]] >= heights[i]:
                    stack.pop()
                else:
                    left.append(stack[-1]+1)
                    break
            if not stack:
                left.append(0)
            
            stack.append(i)
        
        return left


    def largestRectangleArea(self, heights: List[int]) -> int:
        widths = self.getLeftMaxLimit(heights)
        self.getRightMaxLimit(heights, widths)
        
        max_ = 0
        for i, height in enumerate(heights):
            max_ = max(max_, height*widths[i])
        
        return max_