class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def compare(x:int, y:int)->int:
            key1 = f"{x}{y}"
            key2 = f"{y}{x}"
            return 1 if key1 < key2 else -1
            
#         arr = list(map(lambda x: (str(x), str(x).ljust(10, str(x)[-1])), nums))
#         arr.sort(key=lambda x: x[1], reverse=True)
        
#         print(arr)
#         result = ""
#         for val,_ in arr:
#             result +=val
        nums.sort(key=functools.cmp_to_key(compare))
        return ''.join([str(num) for num in nums]).lstrip('0') or '0'
        