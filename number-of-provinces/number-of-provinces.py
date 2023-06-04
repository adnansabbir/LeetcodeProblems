class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        provinces = 0
        n = len(isConnected)

        #     0   1   2   3

        # 0   1   1   0   1
        # 1   1   1   0   0
        # 2   0   0   1   0
        # 3   1   0   0   1

        def markProvince(curr: int)-> int:
            if isConnected[curr][curr] != 1:
                return 0
            isConnected[curr][curr] = 2

            for i in range(n):
                if isConnected[curr][i] == 1:
                    markProvince(i)
            
            return 1

        for i in range(n):
            provinces += markProvince(i)
        
        return provinces
