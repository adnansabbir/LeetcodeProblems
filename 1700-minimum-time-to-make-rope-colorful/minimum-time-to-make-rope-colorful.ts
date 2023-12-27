function minCost(colors: string, neededTime: number[]): number {
    // Append a different character at the end to simplify calculations
    colors += colors[colors.length - 1] !== 'z' ? 'z' : 'a';
    neededTime.push(0); // Append a dummy time

    let total_time: number = neededTime[0]; // Initialize total time with the first balloon's time
    let max_time: number = neededTime[0];   // Initialize max time with the first balloon's time
    let result: number = 0; // This will store the minimum time to remove the balloons

    for (let i = 1; i < colors.length; i++) {
        if (colors[i] === colors[i - 1]) {
            // Sum up the times and find the max time for consecutive balloons
            total_time += neededTime[i];
            max_time = Math.max(max_time, neededTime[i]);
        } else {
            // Calculate the cost for the previous group of same-colored balloons
            result += total_time - max_time;
            // Reset for the next group of balloons
            total_time = neededTime[i];
            max_time = neededTime[i];
        }
    }
    
    return result;
}
