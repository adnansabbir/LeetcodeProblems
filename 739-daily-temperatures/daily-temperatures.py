class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        if len(temperatures) <= 1:
            return [0]
        stack = [len(temperatures)-1]
        ans = [0]
        for pos in range(len(temperatures)-2, -1, -1):
            while len(stack) > 0 and temperatures[stack[-1]] <= temperatures[pos]:
                stack.pop()
            if len(stack) == 0:
                ans.append(0)
            else:
                ans.append(stack[-1]-pos)
            stack.append(pos)
        ans.reverse()
        return ans