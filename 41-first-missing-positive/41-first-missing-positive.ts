function firstMissingPositive(nums: number[]): number {
    // using array itself as hashmap
    
    let start = 0
    // we try to put each num in it's num-1 position
    // if the position is outside of array or
    // if the index already contains currect number we skip and increment start
    // else we swap ne number to it's corrent position and don't increment start
    while(start < nums.length){
        const index = nums[start] - 1
        if(index < 0 || index>=nums.length || nums[index] === index+1){
            start++
            continue
        }
        
        nums[start] = nums[index]
        nums[index] = index + 1
    }
    
    // After this all the numbers within in length of arr will be in corrent position
    // We iterate from 1 to length of nums if the number of index i - 1 is not equal to i this is the smallest missing number
    for(let i = 1; i<=nums.length; i++){
        if(nums[i-1] !== i) return i
    }
    // i.e for case [4,3,2,1] it will be transformed into [1,2,3,4] and no number will be missing in array
    // so the smallest number missing is +1 more than array length
    return nums.length + 1
};