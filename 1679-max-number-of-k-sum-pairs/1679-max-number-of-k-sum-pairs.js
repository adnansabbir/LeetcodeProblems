/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var maxOperations = function(nums, k) {
    const num_freq = new Proxy({}, {get: (obj, prop) => prop in obj ? obj[prop] : 0})
    
    let operations = 0
    
    nums.forEach(n => {
        const target = k - n
        const tInNums = num_freq[target]
        
        if(tInNums){
            operations++
            num_freq[target]--
        }else{
            num_freq[n]++
        }
    })
    
    return operations
};