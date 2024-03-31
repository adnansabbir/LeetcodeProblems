function countSubarrays(nums: number[], minK: number, maxK: number): number {
// [1,1,1,1,1,1,1,1]
// [1,2,3,4,5,0,0,0]
// left = 4, right = 4
// min = 1
// max = 1

// [1,1,1,2,2,3,3,1,1,1,2]
// [1,2,3,0,0,0,0,1,2,3,0]
// left = 8, right = 8
// min = 1
// max = 1

// [1,1,2,3,3,3]
// [0,0,0,2,2,2]
// left = 2, right = 5
// min = 0
// max = 2

// take previousValue
// decide from right pointer -> increase minMax/reset
// if ((left === right and same minMax) or minMax different) and minMax : increase by 1
// Increase left while less than right while minMax and keep increasing value


//Reset
// on out of range -> reset minMax, set left and right to right+1 and value to 0

    let result = 0
    let minMaxCount = [0, 0]
    const inRange = (num: number)=> num>=minK && num<=maxK
    const hasMinMax = ()=> !!(minMaxCount[0] * minMaxCount[1])
    let left = 0, right = 0
    const dp = []
    while(right < nums.length){
        dp.push(right ? dp[right-1] : 0)
        if(inRange(nums[right])){
            if(nums[right] === minK) minMaxCount[0]++
            if(nums[right] === maxK) minMaxCount[1]++
            if(((left === right && minK === maxK) || minK !== maxK) && hasMinMax()) dp[right]++
            while(left < right && hasMinMax()){
                if(nums[left] === minK) minMaxCount[0]--
                if(nums[left] === maxK) minMaxCount[1]--
                if(hasMinMax()) dp[right]++
                left++
            }
        }else{
            left = right+1
            minMaxCount = [0, 0]
            dp[right] = 0
        }
        result+=dp[right]
        right++
    }
    return result
};