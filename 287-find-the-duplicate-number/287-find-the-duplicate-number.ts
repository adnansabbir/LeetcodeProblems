function findDuplicate(nums: number[]): number {
    nums = nums.sort()
    for(let i = 1; i<nums.length; i++){
        if(nums[i] === nums[i-1]) return nums[i]
    }
};