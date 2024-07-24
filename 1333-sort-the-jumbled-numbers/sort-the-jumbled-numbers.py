class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        def transform(num):
            new_num = ''
            while num:
                last_digit = num % 10
                num = (num - last_digit) // 10
                new_num = f'{mapping[last_digit]}' + new_num
            return int(new_num) if new_num else mapping[num]
        
        # print([transform(x) for x in nums])
        return sorted(nums, key=transform)
                
        