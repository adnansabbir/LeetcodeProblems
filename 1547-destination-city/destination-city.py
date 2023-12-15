class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        initialcities = set()
        for path in paths:
            initialcities.add(path[0])
        for path in paths:
            destinationcity = path[1]
            if destinationcity not in initialcities:
                return destinationcity
        return ""