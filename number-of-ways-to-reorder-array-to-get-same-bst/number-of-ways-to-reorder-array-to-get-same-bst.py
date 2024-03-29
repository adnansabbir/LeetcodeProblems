import math

class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        def divideTree(arr: List[int])-> int:
            left, right = [], []
            for num in arr:
                if num < arr[0]:
                    left.append(num)
                elif num > arr[0]:
                    right.append(num)
            return [left, right]
        
        def countPermutation(left: List[int], right: List[int])-> int:
            if not left and not right:
                return 1
            
            lSize, rSize = len(left), len(right)
            currPermutation = math.factorial(lSize + rSize) // (math.factorial(lSize) * math.factorial(rSize))

            leftTree = divideTree(left)
            leftPermutation = countPermutation(leftTree[0], leftTree[1])

            rightTree = divideTree(right)
            rightPermutation = countPermutation(rightTree[0], rightTree[1])

            return (currPermutation * leftPermutation * rightPermutation)
        
        left, right = divideTree(nums)
        return (countPermutation(left, right) % MOD) - 1