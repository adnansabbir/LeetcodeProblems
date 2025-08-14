class Solution:
    def largestGoodInteger(self, num: str) -> str:
        max_num = -1

        for i in range(3, len(num) + 1):
            curr_num = int(num[i-3:i])
            if curr_num % 111 == 0:
                max_num= max(max_num, curr_num)


        if max_num == -1:
            return ""
        elif max_num == 0:
            return "000"
        return str(max_num)
        