class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill = sorted(skill)
        n = len(skill)
        # partition check
        result = skill[0] * skill[-1]
        for i in range(1, n//2):
            if skill[i] + skill[n-i - 1] != skill[i-1] + skill[n-i]:
                return -1
            else:
                result += skill[i] * skill[n-i - 1]

        return result

        
        