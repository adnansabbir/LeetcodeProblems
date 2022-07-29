/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function(nums) {
    const contains = new Set()
    for (let i = 0; i < nums.length; i++){
        if(contains.has(nums[i])) return true
        contains.add(nums[i])
    }
    
    return false
};