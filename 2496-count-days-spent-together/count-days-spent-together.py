from datetime import datetime

class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        alice = (
            int(datetime.strptime(arriveAlice + '-2026', "%m-%d-%Y").strftime("%j")), 
            int(datetime.strptime(leaveAlice + '-2026', "%m-%d-%Y").strftime("%j"))
        )
        bob = (
            int(datetime.strptime(arriveBob + '-2026', "%m-%d-%Y").strftime("%j")), 
            int(datetime.strptime(leaveBob + '-2026', "%m-%d-%Y").strftime("%j"))
        )
        ans = 0
        for i in range(1, 366):
            if alice[0] <= i <= alice[1] and bob[0] <= i <= bob[1]:
                ans += 1
        return ans