function rob(nums: number[]): number {
    if(nums.length <= 2) return Math.max(...nums)
    if(nums.length === 3) return Math.max(nums[0] + nums[2], nums[1])
    
    const dp = new Array<number>(nums.length).fill(0)
    dp[0] = nums[0]
    dp[1] = nums[1]
    dp[2] = nums[0] + nums[2]
    
    for(let i = 3; i<nums.length; i++){
        dp[i] = Math.max(nums[i] + dp[i-3], nums[i] + dp[i-2], dp[i-1])
    }
    return dp[nums.length - 1]
};