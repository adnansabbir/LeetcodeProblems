/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var permuteUnique = function(nums) {
    const result = {}
    
    const swap = (i1, i2, nums) => {
        const temp = nums[i1]
        nums[i1] = nums[i2]
        nums[i2] = temp
    }
    
    const permute = (idx, nums) => {
        if(idx === nums.length - 1){
            result[nums.join('')] = [...nums]
        }
        
        for(let i = idx; i < nums.length; i++){
            if(i !== idx && nums[i] === nums[idx]) continue
            swap(i, idx, nums)
            permute(idx+1, nums)
            swap(idx, i, nums)
        }
    }
    
    permute(0, nums)
    // console.log(result)
    return Object.values(result)
};