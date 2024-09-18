class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def compare(x:int, y:int)->int:
            key1 = f"{x}{y}"
            key2 = f"{y}{x}"
            return 1 if key1 < key2 else -1
            
        nums.sort(key=functools.cmp_to_key(compare))
        result = ""
        for num in nums:
            if not result and not num:
                continue
            result += str(num)
        return result or '0'
        