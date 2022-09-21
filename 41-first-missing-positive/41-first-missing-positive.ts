function firstMissingPositive(nums: number[]): number {
    // using array itself as hashmap
    
    let start = 0
    // we try to put each num in it's num-1 position
    // if the position is outside of array or
    
    while(start < nums.length){
        const index = nums[start] - 1
        if(index < 0 || index>=nums.length || nums[index] === index+1){
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