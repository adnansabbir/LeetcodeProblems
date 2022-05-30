/**
 * @param {number} target
 * @param {number[]} nums
 * @return {number}
 */
var minSubArrayLen = function(target, nums) {
    let currSum = 0
    let start = 0
    let end = 0
    let min_length = Infinity
    
    while(end < nums.length || currSum > target){
        if(currSum < target){
            currSum += nums[end++]   
        }else {
            min_length = Math.min(min_length, end - start)
            currSum -= nums[start++]
        }
        
        if(currSum === target){
            min_length = Math.min(min_length, end - start)
        }
        
    }
    
    return min_length === Infinity ? 0 : min_length
};