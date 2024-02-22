class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        tt = [[0, 0] for _ in range(n + 1)]

        for pA, pB in trust:
            tt[pA][0] += 1
            tt[pB][1] += 1
        
        for i in range(1, n+1):
            peopleITrust, peopleTrustingMe = tt[i]
            if peopleITrust == 0 and peopleTrustingMe == n - 1:
                return i
        
        return -1