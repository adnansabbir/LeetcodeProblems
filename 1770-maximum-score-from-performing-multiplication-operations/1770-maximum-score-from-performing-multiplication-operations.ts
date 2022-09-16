function maximumScore(nums: number[], multipliers: number[]): number {
    const M = multipliers.length
    const N = nums.length
    
    const dp = {}
    const calculate = (mIndex: number, nLeft: number): number =>{
        if(mIndex >= M){
            return 0
        }
        const key = `${mIndex}-${nLeft}`
        if(dp[key] !== undefined) return dp[key]
        
        const multiplier = multipliers[mIndex]
        const multiplicands = [nums[nLeft], nums[(N-1) - (mIndex - nLeft)]]
        
        const left = calculate(mIndex+1, nLeft+1) + (multiplier * multiplicands[0])
        const right = calculate(mIndex+1, nLeft) + (multiplier * multiplicands[1])
        dp[key] = Math.max(left, right)
        return dp[key]
    }
    return calculate(0,0)
};