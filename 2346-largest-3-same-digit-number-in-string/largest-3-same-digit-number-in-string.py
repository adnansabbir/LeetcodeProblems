class Solution:
    def largestGoodInteger(self, num: str) -> str:
        max_num = -1
        result = ""

        for i in range(3, len(num) + 1):
            curr_num = int(num[i-3:i])
            if curr_num % 111 == 0:
                if curr_num > max_num:
                    max_num = curr_num
                    result = num[i-3:i]


        return result
        