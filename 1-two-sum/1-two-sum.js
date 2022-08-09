/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    const idx_map = {}
    
    for (let i=0; i<nums.length; i++){
        if(idx_map[target-nums[i]] !== undefined){
            return [idx_map[target-nums[i]], i]
        }
        else{
            idx_map[nums[i]] = i
        }
    }

};