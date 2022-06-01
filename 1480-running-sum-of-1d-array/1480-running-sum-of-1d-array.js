/**
 * @param {number[]} nums
 * @return {number[]}
 */
var runningSum = function(nums) {
    nums.forEach((num, idx) => nums[idx] = idx === 0 ? num : num + nums[idx-1])
    return nums
};