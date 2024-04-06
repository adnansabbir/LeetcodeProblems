class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        openingIndexesToRemove = []
        closingIndexesToRemove = []
        indexesToRemove = set()

        for i, char in enumerate(s):
            if char == "(":
                openingIndexesToRemove.append(i)
                indexesToRemove.add(i)
            elif char == ")":
                if len(openingIndexesToRemove):
                    indexesToRemove.remove(openingIndexesToRemove.pop())
                else:
                    closingIndexesToRemove.append(i)
                    indexesToRemove.add(i)
        
        result = ""
        for i, char in enumerate(s):
            if i not in indexesToRemove:
                result += char
        return result

        