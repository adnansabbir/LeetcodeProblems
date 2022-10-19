function productExceptSelf(nums: number[]): number[] {

    
    const result = new Array<number>(nums.length).fill(0)
    let zeros = 0, firstZero = 0, non_zero_product = 1
    for(let i = 0; i<nums.length; i++){
        if(nums[i] === 0) {
            zeros++
            firstZero = i
            if(zeros >= 2) return result
            continue
        }
        non_zero_product *= nums[i]    
    }
    
    if(zeros === 1){
        result[firstZero] = non_zero_product
        return result
    }
    
    for(let i = 0; i < nums.length; i++){
        result[i] = non_zero_product / nums[i]
    }
    
    return result
};