class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        result = []

        for i, ast in enumerate(asteroids):
            if ast < 0:
                while result and result[-1] > 0 and result[-1] < abs(ast):
                    result.pop()
                if not result or result[-1] < 0:
                    result.append(ast)
                elif result[-1] == abs(ast):
                    result.pop()
            else:
                result.append(ast)
        
        return result
        
