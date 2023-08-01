class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []

        def collectCombination(curr: int, collected: List[int])-> None:
            if len(collected) == k:
                result.append(collected.copy())
                return
            
            for i in range(curr, n + 1):
                collected.append(i)
                collectCombination(i+1, collected)
                collected.pop()

        collectCombination(1, [])
        return result
            