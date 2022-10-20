function climbStairs(n: number, memo = {}): number {
    if(n <= 3 ) return n
    if(memo[n] !== undefined) return memo[n]
    memo[n] = climbStairs(n-1, memo) + climbStairs(n-2,memo)
    return memo[n]
};