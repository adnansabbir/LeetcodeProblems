/**
 * @param {string} s
 * @param {number} k
 * @return {boolean}
 */

var hasAllCodes = function(s, k) {
    if(s.length < k + 1) return false
    
    const availableNums = new Set()
    for(let i = k; i <= s.length; i++){
        availableNums.add(parseInt(s.substring(i-k, i), 2))
    }
    return availableNums.size === Math.pow(2, k)
};