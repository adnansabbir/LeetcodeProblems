function productExceptSelf(nums: number[]): number[] {
//     1 2 3 4
    
//     1   2   6   24
//     24  24  12   4
//     24  12  8    6
    
    const result = new Array<number>(nums.length).fill(0)
    let zeros = 0
    let firstZero = -1, product = 1
    for(let i = 0; i<nums.length; i++){
        if(nums[i] === 0) {
            zeros++
            firstZero = i
            if(zeros >= 2) return result
        }else{
            product *= nums[i]    
        }
        
    }
    
    if(zeros === 1){
        result[firstZero] = product
        return result
    }
    
    for(let i = 0; i < nums.length; i++){
        result[i] = product / nums[i]
    }
    
    return result
};