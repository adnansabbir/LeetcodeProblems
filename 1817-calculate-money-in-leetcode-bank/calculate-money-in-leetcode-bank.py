class Solution:
    def totalMoney(self, n: int) -> int:
        noOffullWeeks = n // 7
        sumOnFirstWeek = 28
        sumOfAllFullWeeks = (noOffullWeeks * sumOnFirstWeek)
        extraForEachWeek = (((noOffullWeeks - 1) * (noOffullWeeks))//2) * 7
        totalSavings = sumOfAllFullWeeks + extraForEachWeek
        print(noOffullWeeks, sumOfAllFullWeeks, extraForEachWeek)

        currentWeek = noOffullWeeks + 1
        for i in range(n % 7):
            totalSavings += currentWeek
            currentWeek += 1
        return totalSavings
        
        