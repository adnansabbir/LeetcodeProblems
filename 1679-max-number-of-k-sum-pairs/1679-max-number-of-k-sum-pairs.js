/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var maxOperations = function(nums, k) {
    let start = 0
    let end = nums.length - 1
    
    nums.sort((a, b)=> parseInt(a) - parseInt(b))
    
    let op = 0
    while(start < end){
        const sum = nums[start] + nums[end]
        if(sum === k){
            op++
            end--
            start++
        }else if(sum > k){
            end--
        }else{
            start++
        }
    }
    
    return op
};