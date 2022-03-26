/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var search = function(nums, target) {
    let lowerBound = 0;
    let upperBound = nums.length - 1;
    let midPoint;
    
    while (lowerBound <= upperBound){
        midPoint = parseInt(lowerBound + (upperBound - lowerBound) / 2, 10);
        
        if(nums[midPoint] === target) return midPoint;
        if(nums[midPoint] > target) upperBound = midPoint-1;
        if(nums[midPoint] < target) lowerBound = midPoint+1;
    }
    return -1;
    
};