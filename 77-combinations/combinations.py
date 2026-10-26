class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        result = []
        # i = 0, [1,2], [1,3],[2]
        def store_combination(i = 0, com = []): 
            if len(com) == k:
                result.append(com.copy())
                return
            if i > n:
                return

            for j in range(i + 1, n + 1):
                com.append(j)
                store_combination(j, com)
                com.pop()

        
        store_combination()
        return result 

        