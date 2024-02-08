class Solution:
    def numSquares(self, n: int) -> int:
        perfectSquares = [i*i for i in range(1, int(sqrt(n)) + 1) if i*i <= n]
        # print('Squares', perfectSquares)
        dp = [0 for _ in range(n + 1)]

        for square in perfectSquares:
            # print('\n\nsquare\t', square)
            for targetIdx in range(1, n + 1):
                if targetIdx % square == 0:
                    dp[targetIdx] = targetIdx // square
                else:
                    dp[targetIdx] = min((targetIdx // square) + dp[targetIdx%square], dp[targetIdx])
            # result = min(result, dp[-1])
            # print('After\t', dp, result)

        # print(dp)
        return dp[-1]
        