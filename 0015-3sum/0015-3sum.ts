function threeSum(nums: number[]): number[][] {
    const uniqueResult = new Set<string>()
    for(let i = 2; i<nums.length; i++){
        const uniqueNums = new Set<number>([nums[0]])
        for(let j = 1; j<i; j++){
            const target = 0 - (nums[i] + nums[j])
            if(uniqueNums.has(target)) {
                const res = [target, nums[i], nums[j]].sort((a, b) => a-b)
                uniqueResult.add(res.join(','))
            }
            uniqueNums.add(nums[j])
        }
    }
    const result = Array.from(uniqueResult).map(res => res.split(',').map(num => parseInt(num)))
    return result
};