class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        # Append a different character at the end to simplify calculations
        colors += 'z' if colors[-1] != 'z' else 'a'
        neededTime.append(0)  # Append a dummy time

        total_time = neededTime[0]  # Initialize total time with the first balloon's time
        max_time = neededTime[0]    # Initialize max time with the first balloon's time
        result = 0  # This will store the minimum time to remove the balloons

        for i in range(1, len(colors)):
            if colors[i] == colors[i - 1]:
                # Sum up the times and find the max time for consecutive balloons
                total_time += neededTime[i]
                max_time = max(max_time, neededTime[i])
            else:
                # Calculate the cost for the previous group of same-colored balloons
                result += total_time - max_time
                # Reset for the next group of balloons
                total_time = neededTime[i]
                max_time = neededTime[i]
        
        return result