function coinChange(coins: number[], amount: number): number {
    const dp = new Array<number>(amount + 1).fill(Number.MAX_SAFE_INTEGER)
    dp[0] = 0
    
    for(let i = 1; i<= amount; i++){
        for(let coin of coins){
            if(i - coin < 0) continue
            dp[i] = Math.min(dp[i], 1 + dp[i-coin])
        }
    }
    
    return dp[amount] === Number.MAX_SAFE_INTEGER ? -1 : dp[amount]
};