class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        freq = [0]* max(nums).bit_length()
        def add_frequency(num):
            pointer = len(freq) - 1
            while num:
                freq[pointer] += num & 1
                num = num >> 1
                pointer -= 1

        for num in nums:
            add_frequency(num)
        
        # print(freq)
        def get_largest_int():
            # print(freq)
            num = 0
            for i, f in enumerate(freq):
                num = (num << 1)
                # print('before if', num, bin(num))
                if f:
                    freq[i] -= 1
                    num = num | 1
                # print(i, f, num, bin(num), freq)
            # print(num)
            return num

        result = 0
        for i in range(k):
            num = get_largest_int()
            result += num ** 2
            result = result % (10**9 + 7)
        return result
        