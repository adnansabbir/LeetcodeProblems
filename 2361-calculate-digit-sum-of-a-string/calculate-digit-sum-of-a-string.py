class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            new_s = []

            temp_k = k
            temp_sum = 0
            for num_str in s:
                temp_sum += int(num_str)
                temp_k -= 1

                if temp_k == 0:
                    new_s.append(temp_sum)
                    temp_k = k
                    temp_sum = 0
            if temp_k < k:
                new_s.append(temp_sum)
            s = "".join(map(str, new_s))


        return s
        