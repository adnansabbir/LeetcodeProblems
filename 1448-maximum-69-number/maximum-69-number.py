class Solution:
    def maximum69Number (self, num: int) -> int:
        num_str = str(num)
        result = num_str
        for i, char in enumerate(num_str):
            if char == '6':
                result = num_str[:i] + '9' + num_str[i+1:]
                break
        
        return int(result)
        