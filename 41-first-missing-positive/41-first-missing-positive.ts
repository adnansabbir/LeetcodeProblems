function firstMissingPositive(nums: number[]): number {
    let start = 0
    while(start < nums.length){
        const index = nums[start] - 1
        if(index < 0 || index>=nums.length || start + 1 === nums[start] || nums[index] === index+1){
            start++
            continue
        }
        
        nums[start] = nums[index]
        nums[index] = index + 1
    }
    for(let i = 0; i<nums.length; i++){
        if(nums[i] !== i+1) return i+1
    }
    return nums.length + 1
};