/**
 * @param {number[]} nums
 * @return {number}
 */
var missingNumber = function(nums) {
    const n = nums.length
    let remaining = (n * (n + 1)) / 2
    nums.forEach(num=> remaining-=num)
    return remaining
};