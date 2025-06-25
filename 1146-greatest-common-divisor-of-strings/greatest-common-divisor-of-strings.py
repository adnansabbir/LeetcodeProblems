class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ''
        str1_len, str2_len = len(str1), len(str2)
        

        def is_string_repetative(main_str, sub_str):
            if len(main_str) % len(sub_str) == 0:
                return sub_str * (len(main_str) // len(sub_str)) == main_str
            return False
        
        gcd_str = str2
        for i in range(str2_len, 0, -1):
            if is_string_repetative(str2, str2[:i]) and is_string_repetative(str1, str2[:i]):
                return str2[:i]
        return ''
        