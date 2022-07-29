/**
 * @param {number[]} nums
 * @return {number[]}
 */
var findDisappearedNumbers = function(nums) {
    result = []
    numbers = new Set(nums)
    for (let i = 1; i<=nums.length; i++){
        if(!numbers.has(i)){
            result.push(i)
        }
    }
    
    return result
};