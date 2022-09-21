function findDuplicate(nums: number[]): number {
    // Array as hashmap approach
    // As we have one extra number and no 0 will be there, we will try to map the numbers to it's correct index
    // if we find the number is already there then it's a duplicate
    let index = 0
    while(index < nums.length){
        const nextIndex = nums[index]
        if(index === nums[nextIndex]){
            index++
            continue
        }
        if(nums[index] === nums[nextIndex]) return nextIndex
        nums[index] = nums[nextIndex]
        nums[nextIndex] = nextIndex
    }
    
};