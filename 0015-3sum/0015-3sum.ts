function threeSum(nums: number[]): number[][] {
    nums = nums.sort((a, b) => a-b)
    const getTargetWith2Values = (left: number, right: number, target: number): number[][] => {
        const result = []
        while(left < right){
            const sum = nums[left] + nums[right]
            if(sum === target){
                const leftVal = nums[left], rightVal = nums[right]
                result.push([leftVal, rightVal])
                while(nums[left] === leftVal) left++
                while(nums[right] === rightVal) right--
            }
            else if(sum < target) left++
            else if(sum > target) right--
        }
        return result
    }
    
    const result = []
    for(let i = 0; i<nums.length - 2; i++){
        if(i !== 0 && nums[i] === nums[i-1]) continue
        const duplets = getTargetWith2Values(i+1, nums.length - 1, -nums[i])
        if(duplets.length === 0) continue
        duplets.forEach(duplet => {
            result.push([nums[i], duplet[0], duplet[1]])
        })
    }
    
    return result
};