function sortedSquares(nums: number[]): number[] {
    if(nums[0]>= 0) return nums.map(num => num**2)
    if(nums[nums.length-1]<0) return nums.map(num => num**2).reverse()
    
    let right = 0
    while(nums[right] < 0) right++
    let left = right - 1 
    
    const result = []
    while(left >= 0 && right<nums.length){
        if(nums[right]**2 <= nums[left]**2){
            result.push(nums[right++]**2)
        }else{
            result.push(nums[left--]**2)
        }
    }
    
    while(left>=0) result.push(nums[left--]**2)
    while(right<nums.length) result.push(nums[right++]**2)
    
    return result
};