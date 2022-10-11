function increasingTriplet(nums: number[]): boolean {
    if(nums.length < 3) return false
    
    let small = nums[0], medium = null
    
    for(let i = 1; i<nums.length; i++){
        if(nums[i] < small){
            small = nums[i]
        }else if(nums[i] > small && (medium === null || nums[i] < medium)){
            medium = nums[i]
        }else if(medium != null && nums[i] > medium){
            return true
        }
    }
    
    return false
};