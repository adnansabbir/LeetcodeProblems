class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        freq = [0,0,0]

        for bill in bills:
            change = bill - 5

            if change == 0:
                freq[0] += 1
            elif change == 5:
                if not freq[0]:
                    return False
                else:
                    freq[0] = freq[0] - 1
                    freq[1] += 1
            else:
                if freq[0] and freq[1]:
                    freq[0] -= 1
                    freq[1] -= 1
                    freq[2] += 1
                elif freq[0] >= 3:
                    freq[0] -= 3
                    freq[2] += 1
                else:
                    return False

        return True
        