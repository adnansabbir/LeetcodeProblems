/**
 * @param {number[]} nums
 * @return {number[]}
 */
var sortArrayByParity = function(nums) {
    let start = 0
    let end = nums.length - 1
    
    while(start < end){
        
        if(nums[start] % 2 === 0){
            start++
        }
        
        if(nums[end] % 2 !== 0){
            end--
        }
        
        if(nums[start] % 2 !== 0 && nums[end] % 2 === 0 && start < end){
            const temp = nums[start]
            nums[start] = nums[end]
            nums[end] = temp
            start++
            end--
        }
    }
    
    return nums
};