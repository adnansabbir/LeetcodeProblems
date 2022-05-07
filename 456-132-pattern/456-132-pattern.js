/**
 * @param {number[]} nums
 * @return {boolean}
 */
var find132pattern = function(nums) {
    if(nums.length < 3) return false
    const arr = []
    let j = -Infinity
    
    for(let i = nums.length - 1; i >= 0; i--){
        if(nums[i] < j) return true
        
        while(arr.length && nums[i] > arr.at(-1)){
            j = arr.pop()
        }
        
        arr.push(nums[i])
    }
    
    return false
};