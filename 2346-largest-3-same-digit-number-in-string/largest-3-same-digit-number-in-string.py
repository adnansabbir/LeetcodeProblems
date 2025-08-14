class Solution:
    def largestGoodInteger(self, num: str) -> str:
        max_digit = ""

        for i in range(3, len(num) + 1):
            curr_num = int(num[i-3:i])
            if curr_num % 111 == 0:
                max_digit= max(max_digit, num[i-2])


        return max_digit * 3
        