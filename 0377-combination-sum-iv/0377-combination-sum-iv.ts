function combinationSum4(nums: number[], target: number): number {
    const dp = new Array<number>(target + 1).fill(0)
    dp[0] = 1
    
    for(let i = 1; i<=target; i++){
        for(let num of nums){
             const num_before = i - num
             if(num_before >= 0){
                 dp[i] += dp[num_before]
             }
        }
    }
    
    return dp[target]
};