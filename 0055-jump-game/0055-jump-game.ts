function canJump(nums: number[]): boolean {
    if(nums.length === 1) return true
    if(nums[0] === 0) return false
    
    let jumpLeft = nums[0]
    for(let i = 1; i<nums.length; i++){
        jumpLeft--
        if(nums[i] > jumpLeft){
            jumpLeft = nums[i]
        }
        if(jumpLeft === 0 && i !== nums.length - 1) return false
    }
    
    return true
};