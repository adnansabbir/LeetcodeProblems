class Solution:
    def simplifyPath(self, path: str) -> str:
        result = []
        paths = [p for p in path.split('/') if p]
        
        for p in paths:
            if p == '.':
                continue
            elif p == '..':
                if result:
                    result.pop()
            else:
                result.append(p)
        
        return f'/{"/".join(result)}'