function combinationSum4(nums: number[], target: number): number {
    const dp = new Array<number>(target + 1).fill(0)
    dp[0] = 1
    
    for(let i = 1; i<=target; i++){
        for(let num of nums){
             if(i >= num){
                 dp[i] += dp[i-num]
             }
        }
    }
    
    return dp[target]
};