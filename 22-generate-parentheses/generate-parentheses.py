class Solution:
    def generateParenthesis(self, n: int) -> list[str]:

        result = []
        def generate(p: str, o: int, c: int):
            if o + c == 0:
                result.append(p)
                return

            if o > 0:
                generate(f'{p}(', o - 1, c)
            if c > o:
                generate(f'{p})', o, c - 1)

        generate('', n, n)
        return result

        
            
        
        