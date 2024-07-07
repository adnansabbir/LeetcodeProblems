class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        time = time % ((n - 1)*2)
        
        if time >= n:
            time = time - (n - 1)
            return n - time
        else:
            return time + 1

        