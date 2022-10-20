function climbStairs(n: number): number {
    const dp = new Array<number>(n+1)
    dp[0] = 0
    dp[1] = 1
    dp[2] = 2
    
    for(let i = 3; i <= n; i++){
        dp[i] = dp[i-1] + dp[i-2]
    }
    
    return dp[n]
};