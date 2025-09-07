class Solution:
    def sumZero(self, n: int) -> List[int]:
        n_1 = n - 1
        sum_of_n_1 = (n_1 * (n_1 + 1))//2
        
        result = [-sum_of_n_1]
        for i in range(1, n):
            result.append(i)
        return result
        