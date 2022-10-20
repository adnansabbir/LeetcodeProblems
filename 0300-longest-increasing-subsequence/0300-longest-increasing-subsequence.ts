function lengthOfLIS(nums: number[]): number {
    const dp = new Array<number>(nums.length).fill(1)
    for(let i = 0; i<nums.length; i++){
        for(let j = 0; j<i; j++){
            if(nums[j] < nums[i] && dp[i] <= dp[j]){
                dp[i] = dp[j] + 1
            }
        }
    }
    
    return Math.max(...dp)
};