class Solution:
    mapping = ['', '', 'abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
    def letterCombinations(self, digits: str) -> List[str]:

        result = []
        for digit in digits:
            if digit == '1':
                continue
            elif not result:
                result = [char for char in self.mapping[int(digit)]]
            else:
                newChars = [char for char in self.mapping[int(digit)]]
                size = len(result)
                for i in range(size):
                    word = result.pop(0)
                    for char in newChars:
                        result.append(f'{word}{char}')


        return result