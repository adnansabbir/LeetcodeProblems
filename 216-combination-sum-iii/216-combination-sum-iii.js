/**
 * @param {number} k
 * @param {number} n
 * @return {number[][]}
 */
var combinationSum3 = function(k, n) {
    const nums = [1,2,3,4,5,6,7,8,9]
    let minPossible = (k * (k+1)/2)
    let maxPossible = 45 - ((9-k) * ((9-k)+1)/2)
    if(n < minPossible || n > maxPossible) return []
    
    const result = []
    const getCombinations = (nextIdx, sum, currRes) => {
        if(sum === n && currRes.length === k){
            result.push([...currRes])
            return
        }
        
        if(sum >= n) return
        
        for(let i = nextIdx; i < nums.length; i++){
            currRes.push(nums[i])
            getCombinations(i+1, sum + nums[i], currRes)
            currRes.pop()
        }
    }
    
    for(let i = 0; i <= 9 - k; i++){
            getCombinations(i+1, nums[i], [nums[i]])
    }

    return result
};