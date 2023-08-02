class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def collect(numsLeft: Set[int], permutation: List[int]):
            # numsLeft is empty
                # Put permutation into result and return
            if not numsLeft:
                result.append(permutation[:])

            # Take a new number from numsLeft and put it into permutation
            # call collect with new list
            # revert back numsleft and permutation
            for num in list(numsLeft):
                numsLeft.remove(num)
                permutation.append(num)
                collect(numsLeft, permutation)
                numsLeft.add(num)
                permutation.pop()
        
        collect(set(nums), [])
        return result