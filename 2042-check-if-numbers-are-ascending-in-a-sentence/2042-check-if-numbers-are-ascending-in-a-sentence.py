class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        numbers = [int(num) for num in s.split(' ') if num.isdigit()]
        
        for i in range(1, len(numbers)):
            if (numbers[i]<= numbers[i-1]):
                return False
        
        return True