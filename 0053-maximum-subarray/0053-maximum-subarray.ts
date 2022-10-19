function maxSubArray(nums: number[]): number {
    let maxSum = nums[0], sum = 0
    let left = 0, right = 0
    
    while(right < nums.length){
        sum += nums[right++]
        maxSum = Math.max(maxSum, sum)
        if(sum < 0){
            left = right
            sum = 0
        }
    }
    
    return maxSum
};