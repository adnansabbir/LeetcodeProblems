class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        # THe problem statement is confusing
        # Here we need to find out 2 values x = Flower count in Lane 1
        # and y = Flower count in lane 2
        # x and y has to be such that Alice wins at the end of the game
        return (n*m) // 2
        