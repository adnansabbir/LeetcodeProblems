function numSquares(n: number): number {
    let dp = new Array(n+1).fill(Infinity);
    dp[0] = 0;
    let p = 1;
    while(p*p <= n) {
        let sq = p*p;
        for(let i = sq; i < n+1; i++) {
            dp[i] = Math.min(dp[i-sq] + 1,dp[i]);
        }
        p++;
    }
    return dp[n];
};