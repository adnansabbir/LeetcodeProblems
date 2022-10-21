function containsNearbyDuplicate(nums: number[], k: number): boolean {
    const indexMap = {}
    for(let i = 0; i<nums.length; i++){
        if(indexMap[nums[i]] !== undefined && Math.abs(indexMap[nums[i]] - i) <= k ) return true    
        indexMap[nums[i]] = i
    }
    return false
};