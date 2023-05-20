class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        conversions = {}

        for i, [num, denum] in enumerate(equations):
            if not num in conversions:
                conversions[num] = {}
            
            if not denum in conversions:
                conversions[denum] = {}
            
            if not denum in conversions[num]:
                conversions[num][denum] = values[i]
            
            if not num in conversions[denum]:
                conversions[denum][num] = 1/values[i]
        
        def calculateDivision(num, denum):
            if not num in conversions or not denum in conversions:
                return -1
            
            if denum in conversions[num]:
                return conversions[num][denum]

            seen = set([num])
            queue = [[num, 1]]
            while queue:
                size = len(queue)
                for _ in range(size):
                    [curr, product] = queue.pop(0)
                    if curr == denum:
                        return product

                    for key, value in conversions[curr].items():
                        if key not in seen:
                            seen.add(key)
                            conversions[num][key] = value * product
                            queue.append([key, value * product])
            return -1

        return [calculateDivision(a, b) for a, b in queries]