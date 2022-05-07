/**
 * @param {number[]} nums
 * @return {boolean}
 */
var find132pattern = function(nums) {
    if(nums.length < 3) return false
    
    const stack = [{val: nums[0], min: nums[0]}]
    let currMin = nums[0]
    
    for(let i = 1; i< nums.length; i++){
        const num = nums[i]

        while(stack.length && stack.at(-1).val <= num){
            stack.pop()
        }
        
        if(stack.length && num > stack.at(-1).min) return true
        
        stack.push({val: num, min: currMin})
        currMin = Math.min(currMin, num)
    }
    
    return false
};