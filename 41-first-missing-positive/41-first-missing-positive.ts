function firstMissingPositive(nums: number[]): number {
    const uniqueNums = new Set(nums)
    for(let i = 1; i<= nums.length; i++){
        if(!uniqueNums.has(i)) return i
    }
    
    return nums.length + 1
};