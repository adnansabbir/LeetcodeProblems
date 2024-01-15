class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        matchesLoseFrequency = {}

        for winner, looser in matches:
            if winner not in matchesLoseFrequency:
                matchesLoseFrequency[winner] = 0
            if looser not in matchesLoseFrequency:
                matchesLoseFrequency[looser] = 0
            
            matchesLoseFrequency[looser] += 1

        noLossUsers = []
        oneMatchLostUsers = []

        for user in matchesLoseFrequency:
            if matchesLoseFrequency[user] == 0:
                noLossUsers.append(user)
            if matchesLoseFrequency[user] == 1:
                oneMatchLostUsers.append(user)
        
        return [sorted(noLossUsers), sorted(oneMatchLostUsers)]