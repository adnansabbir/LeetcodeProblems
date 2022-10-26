function checkSubarraySum(nums: number[], k: number): boolean {
    // sum of moare than 1 nums % k === 0
    // [1,2,3,4,5,6] 6
    // [1,3,6,10,15,21]
    const remainders: Record<number, number> = {0: -1}
    let sum = 0
    for(let i = 0; i<nums.length; i++){
        sum+=nums[i]
        const rem = sum%k
        if(rem in remainders){
            if(i - remainders[rem] >= 2) return true
        }else{
            remainders[rem] = i        
        }
    }
    
    return false
};