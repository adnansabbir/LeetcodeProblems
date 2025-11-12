class Solution:
    def minOperations(self, nums: List[int]) -> int:
        # if there is 1 or 1s, we can make all the nums 1 on total_len - count(1)
        # Since on each operation we can make one cell as 1
        # or if all even, the gcd will always be min 2

        one_count, even_count = 0, 0
        for num in nums:
            if num == 1:
                one_count += 1
            elif num % 2 == 0:
                even_count += 1

        one_count = sum([1 for num in nums if num == 1])
        if one_count:
            return len(nums) - one_count

        if even_count == len(nums):
            return -1

        # TODO: for each number we need to check which one gives the fastest 1
        def score_to_reduce_to_1(idx)-> int:
            result = float('-inf')

            if idx == 0:
                return result
            
            if nums[idx] == nums[idx-1]:
                return result

            num_prev, num = nums[idx-1], nums[idx]
            gcd = math.gcd(num_prev, num)
            
            if gcd == 1:
                return 1

            left_res, right_res = float('-inf'), float('-inf')
            if gcd != nums[idx-1]:
                nums[idx-1] = gcd
                res_prev = score_to_reduce_to_1(idx-1)

                if res_prev != float('-inf'):
                    left_res = res_prev + 1
            if gcd != nums[idx]:
                nums[idx] = gcd
                res_curr = score_to_reduce_to_1(idx)

                if res_curr != float('-inf'):
                    right_res = res_curr + 1

            nums[idx-1], nums[idx] = num_prev, num
            if left_res != float('-inf') and right_res != float('-inf'):
                return min(left_res, right_res)
            return max(left_res, right_res)
        
        min_op_for_first_one = float('inf')
        for i in range(1, len(nums)):
            if (op:= score_to_reduce_to_1(i)) != float('-inf'):
                min_op_for_first_one = min(min_op_for_first_one, op)
        #     print(i, min_op_for_first_one)
        # print('\n\n')
        # print(min_op_for_first_one)
        return min_op_for_first_one + len(nums) - 1 if min_op_for_first_one != float('inf') else -1