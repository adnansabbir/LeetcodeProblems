class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        matchesLoseFrequency = {}  # Dictionary to track the number of losses for each user

        # Iterate over each match
        for winner, loser in matches:
            # Initialize the frequency for winners and losers, if not present
            if winner not in matchesLoseFrequency:
                matchesLoseFrequency[winner] = 0
            if loser not in matchesLoseFrequency:
                matchesLoseFrequency[loser] = 0

            # Increment the loss count for the loser
            matchesLoseFrequency[loser] += 1

        # Lists to store users who lost no matches and exactly one match
        noLossUsers = []
        oneMatchLostUsers = []

        # Iterate over users in matchesLoseFrequency to categorize them
        for user in matchesLoseFrequency:
            if matchesLoseFrequency[user] == 0:
                noLossUsers.append(user)
            elif matchesLoseFrequency[user] == 1:
                oneMatchLostUsers.append(user)

        # Return the sorted list of users for each category
        return [sorted(noLossUsers), sorted(oneMatchLostUsers)]
