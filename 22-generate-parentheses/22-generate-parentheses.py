class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        
        def choose(opening: int, closing: int)-> str:
            if opening == 0 and closing == 0:
                return ''
            elif closing>opening and opening:
                return '()'
            elif closing>opening and not opening:
                return ')'
            else:
                return '('
                
        
        def makeParenthesis(p: str, o: int, c: int):
            choosen = choose(o,c)
            
            if not choosen:
                result.append(p)
            else:
                if choosen == '()':
                    makeParenthesis(p+'(', o-1, c)
                    makeParenthesis(p+')', o, c-1)
                elif choosen == '(':
                    makeParenthesis(p+'(', o-1, c)
                elif choosen == ')':
                    makeParenthesis(p+')', o, c-1)
        
        makeParenthesis('', n, n)
        return result