import operator
import math

class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        op = ['+', '-', '*', '/']
        ops = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': lambda x, y: x / y if y != 0 else None,  # need custom check for divide
        }

        def is_24(nums)-> bool:
            if not nums:
                return False
            
            for n1i,num1 in enumerate(nums):
                for o in op:
                    for n2i,num2 in enumerate(nums):
                        if n2i == n1i:
                            continue
                        op_res = ops[o](num1, num2)
                        if op_res == None:
                            continue
                        # if num1 == 8 and int(num2) == 0 and o == '/':
                        #     print('')
                        # if num1 == 3 and int(num2) == 2 and o == '-':
                        #     print('')
                        new_nums = [n for idx, n in enumerate(nums) if idx not in (n1i, n2i)] + [op_res]
                        # if num1 == 8 and num2 == 3 and o == '/' and 3 in new_nums and 8 in new_nums:
                        #     print(op_res)
                        if math.isclose(op_res, 24, rel_tol=1e-5) and len(new_nums) == 1:
                            return True
                        if is_24(new_nums):
                            return True
            return False

        return is_24(cards)
                        

        