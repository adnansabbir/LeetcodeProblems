class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        max_bits = max(nums).bit_length()
        bit_counts = [0] * max_bits

        def add_bit_frequency(num):
            bit_index = max_bits - 1

            while num:
                bit_counts[bit_index] += num & 1
                num >>= 1
                bit_index -= 1

        def get_largest_number():
            num = 0

            for bit_index, count in enumerate(bit_counts):
                num <<= 1

                if count > 0:
                    bit_counts[bit_index] -= 1
                    num |= 1

            return num

        for num in nums:
            add_bit_frequency(num)

        result = 0
        for _ in range(k):
            num = get_largest_number()
            result = (result + num ** 2) % MOD

        return result