class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def get_max_val(from_to: List[str])-> int:
            a, b, ab, ba = 0, 0, 0, 0

            for i in range(from_to[0], from_to[1]):
                if s[i] == 'a':
                    a += 1
                    if b:
                        ba += 1
                        b -= 1
                        a -= 1
                    elif y > x and ab:
                        ab -= 1
                        ba += 1
                else:
                    b += 1
                    if a:
                        ab += 1
                        a -= 1
                        b -= 1
                    elif x > y and ba:
                        ab += 1
                        ba -= 1
            return (ab * x) + (ba * y)
        
        result = 0
        left, right = 0, 0
        while right < len(s):
            if s[right] not in ['a', 'b']:
                if right - left > 0:
                    result += get_max_val([left, right])
                left = right + 1

            right += 1

        if right - left > 0:
            result += get_max_val([left, right])

        return result



                