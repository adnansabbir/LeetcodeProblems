function findDuplicate(nums: number[]): number {
    for(let num of nums){
        const pointer = Math.abs(num)
        if(nums[pointer] < 0){
            return pointer
        }
        
        nums[pointer] *= -1
    }
};