class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # Sort the greed factor and size of cookies in non-decreasing order
        g.sort()
        s.sort()

        contentChildCount = 0  # Initialize the count of content children
        # Loop until we run out of either children or cookies
        while g and s:
            # If the smallest cookie can satisfy the least greedy child
            if s[0] >= g[0]:
                contentChildCount += 1  # Satisfy the child
                g.pop(0)  # Remove the child from the list
            s.pop(0)  # Remove the cookie from the list
        return contentChildCount  # Return the total number of content children